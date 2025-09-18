import os
import requests

def send_discord(anime):
    title = anime.get("title", {}).get("romaji")
    anilist_id = anime.get("id")
    url = f"https://anilist.co/anime/{anilist_id}"
    genres = ", ".join(anime.get("genres", []))
    embed = {
        "embeds": [
            {
                "title": title,
                "url": url,
                "color": 0x2e51a2,
                "image": {"url": anime.get("coverImage", {}).get("large", "")},
                "footer": {"text": genres},
            }
        ]
    }
    requests.post(os.getenv("DISCORD_WEBHOOK_URL"), json=embed, headers={"Content-Type": "application/json"})
