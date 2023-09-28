from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_movies = pd.read_csv(r"./database/movies.csv")

@app.get("/")
def getAllMovies():
    return df_movies.set_index(df_movies.index).T.to_dict()