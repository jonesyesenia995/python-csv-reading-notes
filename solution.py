import csv
import io

def solve(value):
    return list(csv.reader(io.StringIO(value, newline="")))
