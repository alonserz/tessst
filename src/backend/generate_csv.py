import csv
import random

def generate_string(range_, alphabet = 'actg'):
    for _ in range(100_000):
        string = ''
        for _ in range(range_):
            string += random.choice(alphabet)
        yield string

def generate():
    with open('./data/data.csv', 'w', newline = '') as file:
        for _ in range(100_000):
            string = generate_string(random.randint(10, 101))
            writer = csv.writer(file, delimiter = ',')
            writer.writerow([_, next(string)])

generate()
