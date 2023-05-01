from fastapi import FastAPI
import pandas as pd
import xgboost as xgb
from pydantic import BaseModel
# import joblib

app = FastAPI()
df = pd.read_csv("./netflix_titles_2.csv", index_col=0)
df_template = pd.read_csv("./df_template.csv", index_col=0)

# model = joblib.load('model.pkl')

@app.get('/genres')
def get_genres():
    genres = []
    for cell in df["listed_in"]:
        if str(cell) != 'nan' :
            for genre in str(cell).split(", "):
                genres.append(genre)
    genres = list(set(genres))
    return {"genres": genres}

@app.get('/countries')
def get_countries():
    countries = []
    for cell in df["country"]:
        if str(cell) != 'nan' :
            for country in str(cell).split(", "):
                countries.append(country)
    countries = list(set(countries))
    return {"countries": countries}

@app.get('/release_years')
def get_release_years():
    release_years = []
    for year in df["release_year"]:
        if str(year) != 'nan' :
            release_years.append(year)
    release_years = list(set(release_years))
    return {"release_years": release_years}

class UserMovieData(BaseModel):
    genre: str
    country: str
    release_year: int

@app.post('/predict')
def predict(user_movie_data: UserMovieData):
    fake_data = []

    for col in df_template.columns.values:
        fake_data.append(0)

    data = pd.DataFrame([fake_data], columns=df_template.columns)

    data["release_year"] = user_movie_data.release_year
    data[user_movie_data.genre] = 1
    data[user_movie_data.country] = 1

    model = xgb.XGBRegressor()
    model.load_model("./model.json")
    predict = model.predict(data.to_numpy())
    print(predict)
    return {"predict": predict}
