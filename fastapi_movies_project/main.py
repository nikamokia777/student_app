from fastapi import FastAPI

import uvicorn

app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "The Matrix",
        "genre": "sci-fi",
        "year": 1999,
        "rating": 8.7
    },
    {
        "id": 2,
        "title": "Inception",
        "genre": "sci-fi",
        "year": 2010,
        "rating": 8.8
    },
    {
        "id": 3,
        "title": "The Hangover",
        "genre": "comedy",
        "year": 2009,
        "rating": 7.7
    },
    {
        "id": 4,
        "title": "The Shawshank Redemption",
        "genre": "drama",
        "year": 1994,
        "rating": 9.3
    },
    {
        "id": 5,
        "title": "Parasite",
        "genre": "drama",
        "year": 2019,
        "rating": 8.5
    }
]

@app.get('/movies')
def read():
    return movies
@app.get('/movies/{movie_id}')
def read_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie 
@app.get('/movies')
def read_movies(genre: str = None, year: int = None, min_rating: float = None, search: str = None):
    filtered_movies = movies

    if genre is not None:
        filtered_movies = []

        for movie in movies:
            if movie['genre'] == genre:
                filtered_movies.append(movie)

    if year is not None:
        filtered_by_year = []

        for movie in filtered_movies:
            if movie['year'] == year:
                filtered_by_year.append(movie)

        filtered_movies = filtered_by_year

    if min_rating is not None:
        filtered_by_minrating = []

        for movie in filtered_movies:
            if movie['rating'] >= min_rating:
                filtered_by_minrating.append(movie)
        filtered_movies = filtered_by_minrating

    if search is not None:
        filtered_by_search = []
        for movie in filtered_movies:
            if movie['title'].lower() == search.lower():
                filtered_by_search.append(movie)
        filtered_movies = filtered_by_search

    return filtered_movies