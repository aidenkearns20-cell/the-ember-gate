from colorama import just_fix_windows_console

from auth import sign_in
from database import SaveStore
from game import Game


def main():
    just_fix_windows_console()
    print("THE EMBER GATE")
    print("The Ember Gate has gone dark. Without its ward, monsters are moving")
    print("into the valley. Warden Mira is waiting for you in Lantern Village.")
    try:
        with SaveStore() as store:
            account = sign_in(store)
            if account is not None:
                Game(store, account).run()
    except (EOFError, KeyboardInterrupt):
        print("\nSession ended. Your last completed action was saved.")
    except (OSError, ValueError) as error:
        print(f"Could not read or write your save: {error}")


if __name__ == "__main__":
    main()
