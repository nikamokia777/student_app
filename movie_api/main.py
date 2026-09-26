from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Movie
from schemas import MovieCreate, MovieUpdate, MovieResponse
import uvicorn



app = FastAPI()


@app.post('/movies', response_model=MovieResponse)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = Movie(
        title=movie.title,
        genre=movie.genre,
        year=movie.year,
        rating=movie.rating,
        description=movie.description
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie


@app.get('/movies', response_model=list[MovieResponse])
def get_movies(
    genre: str = None,
    min_rating: float = None,
    max_rating: float = None,
    year: int = None,
    db: Session = Depends(get_db)
):
    query = db.query(Movie)

    if genre is not None:
        query = query.filter(Movie.genre == genre)

    if min_rating is not None:
        query = query.filter(Movie.rating >= min_rating)

    if max_rating is not None:
        query = query.filter(Movie.rating <= max_rating)

    if year is not None:
        query = query.filter(Movie.year == year)

    return query.all()


@app.get('/movies/search', response_model=list[MovieResponse])
def search_movies(
    q: str,
    db: Session = Depends(get_db)
):
    movies = db.query(Movie).filter(
        Movie.title.ilike(f'%{q}%')
    ).all()

    return movies


@app.get('/movies/{movie_id}', response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail='Movie not found'
        )

    return movie


@app.patch('/movies/{movie_id}', response_model=MovieResponse)
def update_movie(
    movie_id: int,
    movie_data: MovieUpdate,
    db: Session = Depends(get_db)
):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail='Movie not found'
        )

    update_data = movie_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(movie, key, value)

    db.commit()
    db.refresh(movie)

    return movie


@app.delete('/movies/{movie_id}')
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail='Movie not found'
        )

    db.delete(movie)
    db.commit()

    return {'message': 'Movie deleted successfully'}