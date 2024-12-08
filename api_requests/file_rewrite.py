import json
from pprint import pprint


def main():
    files = ["answer.json", "location.json"]

    for filename in files:
        with open(filename, "r", encoding="utf-8") as file:
            data = eval(
                file.read()
                .replace("true", "True")
                .replace("false", "False")
                .replace("null", "None")
            )
        pprint(data)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file)


if __name__ == "__main__":
    main()
