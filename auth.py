import hashlib
import hmac
import re
import secrets
from getpass import getpass

from player import Player
from ui import choose


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256", password.encode(), bytes.fromhex(salt), 600_000
    ).hex()


def sign_in(store):
    while True:
        action = choose("[r]egister, [l]og in, [q]uit: ", ("r", "l", "q"))
        if action == "q":
            return None
        username = input("Username: ").strip().lower()
        account = store.find(username)
        if action == "r":
            if not re.fullmatch(r"[a-z0-9_]{3,20}", username):
                print("Use 3–20 letters, digits, or underscores.")
                continue
            if account is not None:
                print("That username is already taken.")
                continue
            password = getpass("New game password (6+ characters): ")
            if len(password) < 6 or not password.strip():
                print("Choose a password with at least six characters.")
                continue
            salt = secrets.token_hex(16)
            store.register(username, salt, hash_password(password, salt), Player().to_save())
            print("Account created. You are signed in.")
            return store.find(username)

        password = getpass("Password: ")
        if account is not None:
            candidate = hash_password(password, account["salt"])
            if hmac.compare_digest(candidate, account["password_hash"]):
                print(f"Welcome back, {username}.")
                return account
        print("Username or password incorrect.")
