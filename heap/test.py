import csv
from main import Database

# Caminho para o arquivo CSV
csv_file = "test/data/employees.csv"

db = Database()


def import_csv_to_database(csv_file):
    with open(csv_file, mode="r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            param1 = int(row["Age"])
            param2 = int(row["JoiningYear"])
            param3 = row["Education"]
            param4 = row["City"]
            param5 = row["Gender"]
            db.insert(param1, param2, param3, param4, param5)


if __name__ == "__main__":
    import_csv_to_database(csv_file)
    db.select()
