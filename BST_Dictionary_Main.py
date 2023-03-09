from BST_Dictionary import BSTDictionary
from pathlib import Path
import time
import sys

def addValue(Dictionary, key, value):
    Dictionary.addValue(key, value)

if __name__ == "__main__":

    # Create an instance of new BST dictionary
    Dictionary = BSTDictionary(True)

    path = Path(__file__).parent / "inputPS09.txt"
    counter = 1

    # Open the input file and read the commands
    with path.open() as f:
        commands = f.readlines()

    outputPath = Path(__file__).parent / "outputPS09.txt"
    output_file = open(outputPath, 'w+')
    newlinestr = "\r\n"

    # Iterate over commands and execute command
    for command in commands:
        command = command.strip()
        if command.startswith("addValue"):
            try:
                exec(command)
            except:
                print("Invalid addValue command : ", command, ". No action", file=output_file )
        elif command == "Dictionary.keys()":
            print(str(Dictionary.keys()), file=output_file)
        elif command == "Dictionary.values()":
            print(str(Dictionary.values()), file=output_file)
        elif command.startswith("Dictionary["): # overload index-operator ([])
            try:
                if command.__contains__("="): # set dictionary value
                    exec(command)
                else: 
                    key = int(command.split('[')[1].removesuffix(']'))
                    print(str(Dictionary[key]), file=output_file)
            except:
                print("Invalid usage of operator([]) command : ", "command", ". No action", file=output_file )
        else:
            print("Invalid command : ", command, ". No action", file=output_file )





