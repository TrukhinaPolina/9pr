import csv
import sys

a = 'a.csv'
with open(a, newline='') as f:
    reader = csv.reader(f)
try:
    b = 0
    with open(a, "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        next(reader)
        print("Нужно купить:")
        for item, count, price in reader:
            b += int(price) * int(count)
            print(f" {item} - {count} шт. за {price} руб.")
        print(f"Итого: {b} руб.")
except csv.Error as e:
    sys.exit(f'file {a}, line {reader.line_num}: {e}')


