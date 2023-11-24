"""
This script will convert your Json data ti a CSV file.
It takes .json a file as input and provides .csv the file as outout.

Install json library:  pip install json

"""

import json

if __name__ == '__main__':
    try:
        with open('input.json', 'r') as f:
            data = json.load(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]}, {obj["age"]},{obj["birthyear"]}'

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
        