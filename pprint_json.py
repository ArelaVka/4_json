import json
from sys import argv


def load_data(input_file_path):
    try:
        with open(input_file_path, "r", encoding="utf8") as input_file:
            return json.load(input_file)
    except ValueError:
        return False


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    input_data = load_data(argv[1])
    if (len(argv[1]) > 0) and input_data:
        pretty_print_json(input_data)
    else:
        print("Your json file is incorrect or you forgot enter the path")
