import os
import requests

def send_discord(anime):
    title = anime.get("title", {}).get("romaji")
    mal_id = anime.get("idMal")
    url = f"https://myanimelist.net/anime/{mal_id}"
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
