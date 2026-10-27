import csv
from database import engine, Base, SessionLocal
from database import MovieDB, LinkDB, RatingDB, TagDB

Base.metadata.create_all(bind=engine)
db = SessionLocal()

print("Rozpoczynanie filmów...")
with open('data/movies.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        movie = MovieDB(id=int(row[0]), title=row[1], genres=row[2])
        db.add(movie)
db.commit()

print("Ładowanie linków...")
with open('data/links.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        # Używamy "movieid" bez podłogi, tak jak zapisałeś w database.py
        link = LinkDB(movieid=int(row[0]), imdb_id=row[1], tmdb_id=row[2])
        db.add(link)
db.commit()

print("Ładowanie ocen...")
with open('data/ratings.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        rating = RatingDB(user_id=int(row[0]), movie_id=int(row[1]), rating=float(row[2]), timestamp=row[3])
        db.add(rating)
db.commit()

print("Ładowanie tagów...")
with open('data/tags.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        tag = TagDB(user_id=int(row[0]), movie_id=int(row[1]), tag=row[2], timestamp=row[3])
        db.add(tag)
db.commit()

print("Wszystkie dane zostały załadowane do bazy!")