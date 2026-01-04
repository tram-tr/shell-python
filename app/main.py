import sys
import os

def main():
    shell_cmds = ["echo", "type", "exit"]
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
                if command in shell_cmds:
                    print(f"{command} is a shell builtin")
                else:
                    found = False
                    path_env = os.environ.get("PATH", "")
                    # go through each directory in PATH
                    for dir in path_env.split(os.pathsep):
                        if dir == "":
                            dir = "."
                        full_path = os.path.join(dir, command) 
                        # check if the file exists and is executable
                        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                            found = True
                            break
                    if found:
                        print(f"{command} is {full_path}")
                    else:
                        print(f"{command}: not found")
        else:
            found = False
            path_env = os.environ.get("PATH", "")
            for dir in path_env.split(os.pathsep):
                if dir == "":
                    dir = "."
                full_path = os.path.join(dir, cmd)
                if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                    found = True
                    break

            if found: 
                os.execv(full_path, [cmd] + args)
                print(f"Program was passed {len(args) + 1} args (including program name).")
                print(f"Arg #0: {cmd}")
                for i, arg in enumerate(args):
                    print(f"Arg #{i + 1} = {arg}")
            else:
                print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
