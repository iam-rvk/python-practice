# remove_duplicates_large_file.py
# Removes duplicate lines from a large file without loading whole file into memory.
# Keeps the first occurrence of each line.

import sqlite3

input_file = "input.txt"
output_file = "output.txt"
db_file = "seen_lines.db"

conn = sqlite3.connect(db_file)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS seen (line TEXT PRIMARY KEY)")
conn.commit()

with open(input_file, "r", encoding="utf-8", errors="ignore") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        try:
            cur.execute("INSERT INTO seen(line) VALUES (?)", (line,))
            fout.write(line)  # write only if it was not seen before
        except sqlite3.IntegrityError:
            pass  # duplicate line, skip

conn.commit()
conn.close()

print(f"Done. Unique lines written to {output_file}")