from BST_Dictionary import BSTDictionary
from pathlib import Path
import time
import sys

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
        if command.startswith("Dictionary.insert"):
            exec(command)
            # Dictionary.print_tree(str(counter))
            # counter=counter+1
        elif command == "Dictionary.keys()":
            print(str(Dictionary.keys()), file=output_file)
        elif command == "Dictionary.values()":
            print(str(Dictionary.values()), file=output_file)
        else:
            try:
                key = int(command.split('[')[1].removesuffix(']'))
                print(str(Dictionary[key]), file=output_file)
            except:
                pass


def addValue(dictionary: BSTDictionary, key, data):
    dictionary.addValue(key, data)
