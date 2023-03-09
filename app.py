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
anime_description = anime['desc']
anime_next_ep = anime['next_airing_ep']

anime_info = f"English Name: {anime_en_name}\n\nJapanese Name: {anime_romaji_name}\n\nRunning Status: {anime_runtime_start} - {anime_runtime_end}\n\nFormat: {anime_format}\n\nStatus: {anime_status}\n\nEpisodes: {anime_episodes}\n\nSeason: {anime_season}\n\nScore: {anime_score}\n\nGenres: {anime_genres}\n\nSynopsis: \n{anime_description}"

