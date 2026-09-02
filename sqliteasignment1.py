import sqlite3


conn = sqlite3.connect("orgdb.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

# Open mbox.txt
fname = "mbox.txt"
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"Error: Make sure '{fname}' is in the same folder as this script.")
    quit()

# Process each email organization
for line in fh:
    if not line.startswith("From: "):
        continue

    pieces = line.split()
    email = pieces[1]
    org = email.split("@")[1]

    cur.execute("SELECT count FROM Counts WHERE org = ? ", (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (org,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))

# Commit outside the loop for fast execution
conn.commit()

# Print top 10 results to verify IUPUI count is 536
sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"
print("Counts:")
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
