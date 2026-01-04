import sys


def main():
    while True:
        sys.stdout.write("$ ")
        cmd = input()
        if cmd == "exit":
            break
        print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
