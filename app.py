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