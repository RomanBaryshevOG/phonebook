import csv
import add_delete


def read_file_csv():
    phone_numbers = dict()
    with open('phonebook.csv', encoding='utf=8') as f:
        reader =csv.reader(f, delimiter= ';')
        for line in reader:
            phone_numbers[line[0]] = line[1:]
    return phone_numbers


def write_file_csv():
    with open('phonebook.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(add_delete.add_note())