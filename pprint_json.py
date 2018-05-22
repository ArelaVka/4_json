import json


def is_json(input_file_path):
    try:
        json.load(open(input_file_path, "r", encoding="utf8"))
        return True
    except ValueError:
        return False


def load_data(input_file_path):
    with open(input_file_path, "r", encoding="utf8") as f:
        all_data = json.load(f)
    return all_data


def pretty_print_json(input_data):
    print(json.dumps(input_data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    path_of_data_file = "alco_shops.json"
    if is_json(path_of_data_file):
        pretty_print_json(load_data(path_of_data_file))
    else:
        print("Your json file is incorrect")
