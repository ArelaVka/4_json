import json
from sys import argv


def load_data(input_file_path):
    try:
        with open(input_file_path, "r", encoding="utf8") as input_file:
            return json.load(input_file)
    except:
        return False


def pretty_print_json(ugly_input_data):
    return json.dumps(ugly_input_data, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    if len(argv) > 1 and load_data(argv[1]):
        print(pretty_print_json(load_data(argv[1])))
    else:
        print("Your json file is incorrect or you forgot enter the path")
