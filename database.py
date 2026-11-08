from pathlib import Path

from tinydb import Query, TinyDB


class SaveStore:
    def __init__(self, path=None):
        if path is None:
            path = Path(__file__).with_name("saves.json")
        self.db = TinyDB(path, indent=2)
        self.accounts = self.db.table("accounts")

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.db.close()

    def find(self, username):
        return self.accounts.get(Query().username == username)

    def register(self, username, salt, password_hash, progress):
        return self.accounts.insert({
            "username": username,
            "salt": salt,
            "password_hash": password_hash,
            "progress": progress,
        })

    def save(self, account_id, progress):
        self.accounts.update({"progress": progress}, doc_ids=[account_id])
