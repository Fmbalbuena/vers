import memory
import versions

while True:
    if memory.values["version"] == "0.0.0":
        version_index = 0
        vers = versions.version()
        if vers.version_0_0_0.run():
            print("sd")
            version_index += 1
            if len(memory.version_order) >= version_index:
                print("You have reached the lastest version.")
                print("To play again (in the lastest version), please insert \"Y\".")
                print("Anything else will exit the program, but will save the version.")
                confirmation = input(" > ")
                if confirmation == "Y":
                    version_index -= 1
                else:
                    break