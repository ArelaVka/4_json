import json
from sys import argv


def load_data(input_file_path):
    try:
        with open(input_file_path, "r", encoding="utf8") as input_file:
            return json.load(input_file)
    except ValueError:
        return False


def pretty_print_json(input_data):
    print(json.dumps(input_data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    path_of_file = argv[1]
    if (len(path_of_file)>0) and load_data(path_of_file):
        pretty_print_json(load_data(path_of_file))
    else:
        print("Your json file is incorrect or you forgot enter the path")
