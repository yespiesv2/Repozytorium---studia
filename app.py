from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, MovieDB, LinkDB, RatingDB, TagDB

app = FastAPI()

# Funkcja pomocnicza: otwiera połączenie z bazą dla każdego zapytania i bezpiecznie je zamyka
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def hello_world():
    return {"hello": "world"}

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    # db.query(...) to odpowiednik SQL-owego "SELECT * FROM movies"
    # Używamy .limit(100), żeby nie zawiesić przeglądarki wypluwaniem tysięcy rekordów na raz
    return db.query(MovieDB).limit(100).all()

@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    return db.query(LinkDB).limit(100).all()

@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    return db.query(RatingDB).limit(100).all()

@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    return db.query(TagDB).limit(100).all()