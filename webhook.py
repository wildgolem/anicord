import os
import requests

def send_discord(anime):
    title = anime.get("title", {}).get("romaji")
    anilist_id = anime.get("id")
    url = f"https://anilist.co/anime/{anilist_id}"
    cover_url = anime.get("coverImage", {}).get("large", "")
    genres = ", ".join(anime.get("genres", []))
    
    embed = {
        "title": title,
        "url": url,
        "color": 0x0B1622,
        "image": {"url": cover_url},
        "footer": {"text": genres},
    }

    payload = {
        "embeds": [embed],
    }

    requests.post(os.getenv("DISCORD_WEBHOOK_URL"), json=payload, headers={"Content-Type": "application/json"})
