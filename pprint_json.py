import json
import sys
import os


def load_data(input_file_path):
    try:
        with open(input_file_path, "r", encoding="utf8") as input_file:
            return json.load(input_file)
    except ValueError:
        return False


def pretty_print_json(ugly_input_data):
    return json.dumps(ugly_input_data, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        input_data = load_data(sys.argv[1])
        if input_data:
            print(pretty_print_json(input_data))
        else:
            print("Your json file is incorrect")
    else:
        print("You forgot enter the path to file of file does not exist")
