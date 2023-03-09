from app import *
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html', animename_en = anime_en_name, animename_jp = anime_romaji_name, runtime_start = anime_runtime_start, runtime_end = anime_runtime_end, animebg= anime_bg_img, animeimg = anime_img, format = anime_format, status = anime_status, episodes = anime_episodes, season = anime_season, score = anime_score, genres = anime_genres, description = anime_description, next_ep = anime_next_ep)

if __name__ == "__main__":
  app.run(host='0.0.0.0',  debug=True)