import sys


def main():
    while True:
        sys.stdout.write("$ ")
        str = input()
        cmd, args = str.split(" ")[0], str.split(" ")[1:]
        if cmd == "exit":
            break
        elif cmd == "echo":
            print(" ".join(args))
        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
