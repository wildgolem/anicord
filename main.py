import time
from storage import load_ids, save_ids
from api import fetch_anime
from webhook import send_discord

def main():
    existing_ids = load_ids()
    anime_list = fetch_anime()
    new_ids = set()
    for anime in reversed(anime_list):
        ani_id = anime.get("id")
        if (
            ani_id
            and ani_id not in existing_ids
            and anime.get("countryOfOrigin") == "JP"
            and anime.get("format") not in {"MUSIC", "TV_SHORT"}
        ):
            send_discord(anime)
            new_ids.add(ani_id)
            time.sleep(0.5)
    if new_ids:
        save_ids(existing_ids.union(new_ids))

if __name__ == "__main__":
    main()
