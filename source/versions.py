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