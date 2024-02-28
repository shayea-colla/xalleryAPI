from termcolor import colored
def debug(message):
    dir_line = "_" * 50,"Dir", "_" * 50
    message_line = "_" * 50,"Message", "_" * 50
    print()
    print(colored(dir_line, "red"))
    print()
    print((colored(dir(message), "magenta")))
    print()
    print(colored(message_line, "red"))
    print()
    print(colored(message, "magenta"))
    print()


def line(message=None):
    message = "_" * 50,message, "_" * 50
    print()
    print(colored(message, "red"))
    print()
