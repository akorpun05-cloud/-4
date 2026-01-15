# TODO импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # TODO считать содержимое csv файла
    data = []

    with open(INPUT_FILENAME, "r", encoding="utf-8") as input_file:
        csv_reader = csv.DictReader(input_file, delimiter=",")

        for row in csv_reader:
            data.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
        json.dump(data, output_file, indent=4)

if __name__ == "__main__":
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")