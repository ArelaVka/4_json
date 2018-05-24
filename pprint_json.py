import json
from sys import argv


def load_data(input_file_path):
    try:
        with open(input_file_path, "r", encoding="utf8") as open_file:
            json.load(open_file)
        return json.load(open_file)
    except ValueError:
        return False


def pretty_print_json(input_json_file):
    print(json.dumps(input_json_file, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    path_to_file = argv[1]
    if load_data(path_of_file):
        pretty_print_json(load_data(path_of_data_file))
    else:
        print("Your json file is incorrect")
