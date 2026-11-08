from colorama import Fore, Style


def color(text, foreground):
    return f"{foreground}{text}{Style.RESET_ALL}"


def choose(prompt, options):
    while True:
        answer = input(prompt).strip().lower()
        if answer in options:
            return answer
        print(color("Choose one of: " + ", ".join(options), Fore.YELLOW))
