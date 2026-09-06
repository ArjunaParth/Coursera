import csv
import os
import sqlite3

# 1. Verify tracks.csv exists in the current directory
csv_file = 'tracks.csv'
if not os.path.exists(csv_file):
    print(
        f"ERROR: '{csv_file}' not found in {os.getcwd()}! Please put the CSV file here."
    )
    exit()

# 2. Connect to database
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# 3. Create fresh tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);
''')

# 4. Read CSV and insert records
rows_inserted = 0
with open(csv_file, 'r', encoding='utf-8') as handle:
  reader = csv.reader(handle)
  for row in reader:
    # Standard format: Title(0), Artist(1), Album(2), Count(3), Rating(4), Length(5), Genre(6)
    if len(row) < 7:
      continue

    title = row[0]
    artist = row[1]
    album = row[2]
    count = row[3]
    rating = row[4]
    length = row[5]
    genre = row[6]

    # Insert Artist
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert Genre
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert Album
    cur.execute(
        'INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)',
        (album, artist_id),
    )
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    # Insert Track
    cur.execute(
        '''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES (?, ?, ?, ?, ?, ?)''',
        (title, album_id, genre_id, length, rating, count),
    )
    rows_inserted += 1

# 5. Commit and save
conn.commit()
print(
    f"Successfully inserted {rows_inserted} tracks into 'trackdb.sqlite'."
)

# 6. Run validation check automatically
print("\n--- Validation Query Output ---")
query = """
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
   AND Album.artist_id = Artist.id
ORDER BY Artist.name LIMIT 3;
"""
for result in cur.execute(query):
  print(result)

cur.close()
conn.close()
