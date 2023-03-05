from BST_Dictionary import BSTDictionary
import time
if __name__ == "__main__":
    # Create an instance of new BST dictionary
    Dictionary = BSTDictionary()

    from pathlib import Path

    path = Path(__file__).parent / "inputPS09.txt"
    

    # Open the input file and read the commands
    with path.open() as f:
        commands = f.readlines()
    
    #Iterate over commands and execute command
    for command in commands:
        command = command.strip()
        if command.startswith("Dictionary.insert"):
            exec(command)
        elif command == "Dictionary.keys()":
            print(Dictionary.keys())
        elif command == "Dictionary.values()":
            print(list(Dictionary.values()))
        else:
            try:
                exec(command)
            except:
                pass

