import sys
import os
import shlex

def main():
    shell_cmds = ["echo", "type", "exit", "pwd", "cd"]

    while True:
        try:
            sys.stdout.write("$ ")
            line = input()
        except EOFError:
            break

        try:
            tokens = shlex.split(line)
        except ValueError as e:
            print(f"Error parsing command: {e}")
            continue
        
        if not tokens:
            continue

        cmd = tokens[0]
        args = tokens[1:]

        if cmd == "exit":
            break
        elif cmd == "echo":
            print(" ".join(args))
        elif cmd == "pwd":
            print(os.getcwd())
        elif cmd == "cd":
            if len(args) != 1:
                print("cd: usage: cd DIRECTORY")
            else:
                dir = args[0]
                if dir == "~":
                    dir = os.path.expanduser("~")
                try:
                    os.chdir(dir)
                except FileNotFoundError:
                    print(f"cd: {dir}: No such file or directory")
                except NotADirectoryError:
                    print(f"cd: {dir}: Not a directory")
                except PermissionError:
                    print(f"cd: {dir}: Permission denied")
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
                # execute the command
                # a real shell would
                # 1. fork a new process
                # 2. in the child process, replace the process image with the command -> exec
                # 3. in the parent process, wait for the child to finish
                # 4. print the next prompt
                # so shell must not die when executing an external command
                pid = os.fork()
                if pid == 0:
                    os.execv(full_path, [cmd] + args)
                else:
                    os.waitpid(pid, 0)
                    
                # print(f"Program was passed {len(args) + 1} args (including program name).")
                # print(f"Arg #0: {cmd}")
                # for i, arg in enumerate(args):
                #     print(f"Arg #{i + 1} = {arg}")
            else:
                print(f"{cmd}: command not found")

    return 0

if __name__ == "__main__":
    main()
