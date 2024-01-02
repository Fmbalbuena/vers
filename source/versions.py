class version:
    def __init__(self):
        pass
    class version_0_0_0():
        def run():
            while True:
                line = input(" > ")
                if line == "help":
                    print("help")
                    print("to print this help page")
                    print("update")
                    print("to update")
                    print("exit")
                    print("to exit this console")
                elif line == "update":
                    return True
                elif line == "exit":
                    return False
                else:
                    print("Please type \"help\" to see the commands list")
    class version_0_0_1():
        def run():
            while True:
                line = input(" > ")
                if line == "help":
                    print("help")
                    print("to print this help page")
                    print()
                    print("update <arg>")
                    print("to update")
                    print("<arg> is useless, it only reads the first 7 characters anyway")
                    print("Note that it must include update and a space")
                    print()
                    print("exit")
                    print("to exit this console")
                elif len(line) >= 6 and line[6:] == "update":
                    return True
                elif line == "exit":
                    return False
                else:
                    print("Please type \"help\" to see the commands list")
