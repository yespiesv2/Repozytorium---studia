import csv
from fastapi import FastAPI


app = FastAPI()

#Zadanie 1 
@app.get("/")
def hello_world():
    return {'hello': 'world'}

#Zadanie 2 
class Movie:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres

@app.get("/movies")
def get_movies():
    try:
        with open('movies.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            return [Movie(row[0], row[1], row[2]).__dict__ for row in reader if len(row) >= 3]
            
    except FileNotFoundError:
        return {"error": "Brak pliku movies.csv"}

#Zadanie 3 
class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

@app.get("/links")
def get_links():
    try:
        with open('links.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
        
            return [Link(row[0], row[1], row[2]).__dict__ for row in reader if len(row) >= 3]
    except FileNotFoundError:
        return {"error": "Brak pliku links.csv"}

@app.get("/ratings")
def get_ratings():
    try:
        with open('ratings.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            
            return [Rating(row[0], row[1], row[2], row[3]).__dict__ for row in reader if len(row) >= 4]
    except FileNotFoundError:
        return {"error": "Brak pliku ratings.csv"}

@app.get("/tags")
def get_tags():
    try:
        with open('tags.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
           
            return [Tag(row[0], row[1], row[2], row[3]).__dict__ for row in reader if len(row) >= 4]
    except FileNotFoundError:
        return {"error": "Brak pliku tags.csv"}