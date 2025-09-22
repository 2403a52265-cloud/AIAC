import csv

# Define PII columns to redact
PII_COLUMNS = {'name', 'email', 'phone'}

def redact_csv(input_path, output_path):
    with open(input_path, newline='', encoding='utf-8') as infile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            for col in PII_COLUMNS:
                if col in row:
                    row[col] = 'REDACTED'
            writer.writerow(row)

# Example usage:
redact_csv('input.csv', 'output.csv')