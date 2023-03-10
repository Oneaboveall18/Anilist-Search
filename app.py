from AnilistPython import Anilist

anilist = Anilist()

anime = anilist.get_anime("Death Note")

anime_en_name = anime['name_english']
anime_romaji_name = anime['name_romaji']
anime_runtime_start = anime['starting_time']
anime_runtime_end = anime['ending_time']
anime_bg_img = anime['banner_image']
anime_img = anime['cover_image']
anime_format = anime['airing_format']
anime_status = anime['airing_status']
anime_episodes = anime['airing_episodes']
anime_season = anime['season']
anime_score = anime['average_score']
anime_genres = anime['genres']
anime_next_ep = anime['next_airing_ep']
anime_description = anime['desc']
anime_description = anime_description.replace("<br>", "")
anime_description = anime_description.replace("<i>", "")
anime_description = anime_description.replace("</i>", "")
