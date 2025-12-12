import csv
import os
from datetime import datetime

def create_dummy_csv(filename):
    data = [
        ["operation", "amount"],
        ["CREDIT", "100"],
        ["DEBIT", "50"],
        ["CREDIT", "200"],
        ["ERROR_TEST", "0"]
    ]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

class BatchProcessor:
    def __init__(self, csv_filename, log_filename):
        self.csv_filename = csv_filename
        self.log_filename = log_filename
        self.csv_file = None
        self.log_file = None

    def __enter__(self):
        self.csv_file = open(self.csv_filename, "r", newline="")
        self.log_file = open(self.log_filename, "a")
        
        timestamp = datetime.now()
        self.log_file.write(f"[{timestamp}] START processing {self.csv_filename}\n")
        
        reader = csv.DictReader(self.csv_file)
        return reader, self.log_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        timestamp = datetime.now()
        if exc_type:
            self.log_file.write(f"[{timestamp}] ERROR: {exc_val}\n")
        else:
            self.log_file.write(f"[{timestamp}] END SUCCESS\n")

        if self.csv_file:
            self.csv_file.close()
        if self.log_file:
            self.log_file.close()

if __name__ == "__main__":
    csv_file = "data.csv"
    log_file = "journal.log"

    create_dummy_csv(csv_file)

    print("--- Test Normal ---")
    with BatchProcessor(csv_file, log_file) as (reader, logger):
        for row in reader:
            op = row["operation"]
            amt = row["amount"]
            print(f"Traitement: {op} valeur {amt}")
            if op == "ERROR_TEST":
                print("Simulation erreur...")
                raise ValueError("Operation invalide detectee")

    print("\n--- Contenu du journal.log ---")
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            print(f.read())

    if os.path.exists(csv_file):
        os.remove(csv_file)
    if os.path.exists(log_file):
        os.remove(log_file)