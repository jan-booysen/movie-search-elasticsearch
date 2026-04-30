import csv
import json
import re
from collections import defaultdict

MOVIES_FILE = "data/ml-latest-small/movies.csv"
TAGS_FILE = "data/ml-latest-small/tags.csv"
OUTPUT_FILE = "data/movies_final.json"

def clean_title(title):
    return re.sub(r" \(.*\)$", "", title.replace('"', ''))

def extract_year(title):
    year = title[-5:-1]
    return int(year) if year.isdigit() else None

def load_tags():
    tags_map = defaultdict(set)

    with open(TAGS_FILE, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            movie_id = row["movieId"]
            tag = row["tag"].strip().lower()

            if tag:
                tags_map[movie_id].add(tag)

    return tags_map

def merge():
    tags_map = load_tags()

    with open(MOVIES_FILE, encoding="utf-8") as movies, \
         open(OUTPUT_FILE, "w", encoding="utf-8") as out:

        reader = csv.DictReader(movies)

        for row in reader:
            movie_id = row["movieId"]
            title = clean_title(row["title"])
            year = extract_year(row["title"])
            genres = row["genres"].split("|") if row["genres"] else []

            tags = list(tags_map.get(movie_id, []))

            doc = {
                "movie_id": int(movie_id),
                "title": title,
                "year": year,
                "genres": genres,
                "tags": tags,
                "tag_count": len(tags)
            }

            action = {
                "index": {
                    "_index": "movies",
                    "_id": movie_id
                }
            }

            out.write(json.dumps(action) + "\n")
            out.write(json.dumps(doc) + "\n")

    print(f"✅ Created {OUTPUT_FILE}")

if __name__ == "__main__":
    merge()