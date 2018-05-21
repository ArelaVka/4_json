#coding:utf-8
import json


def load_data(file_path):
    jfile = json.load(open(file_path, "r", encoding="utf8"))
    print(jfile)
    return jfile


def pretty_print_json(input_file):
    print(json.dumps(input_file, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    path = "alco_shops.json"
    load_data(path)
    pretty_print_json(load_data(path))
