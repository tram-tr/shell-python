import sys


def main():
    while True:
        sys.stdout.write("$ ")
        str = input()
        cmd, args = str.split(" ")[0], str.split(" ")[1:]
        if cmd == "exit":
            break
        elif cmd == "echo":
            if len(args) == 0:
                print()
            print(" ".join(args))
        elif cmd == "type":
            if len(args) != 1:
                print("type: usage: type COMMAND")
            else:
                command = args[0]
                if command == "echo":
                    print(f"{command} is a shell builtin")
                elif command == "type":
                    print(f"{command} is a shell builtin")
                elif command == "exit":
                    print(f"{command} is a shell builtin")
                else:
                    print(f"{command}: not found")
        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
