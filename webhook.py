import os
import requests

def send_discord(anime):
    title = anime.get("title", {}).get("romaji")
    anilist_id = anime.get("id")
    url = f"https://anilist.co/anime/{anilist_id}"
    cover_url = anime.get("coverImage", {}).get("large", "")
    trailer = anime.get("trailer")
    trailer_url = f"https://www.youtube.com/watch?v={trailer.get('id')}" if trailer and trailer.get("site") == "youtube" else None
    genres = ", ".join(anime.get("genres", []))
    
    embed = {
        "title": title,
        "url": url,
        "color": 0x2e51a2,
        "image": {"url": cover_url},
        "footer": {"text": genres},
    }

    payload = {
        "embeds": [embed],
    }

    if trailer_url:
        payload["components"] = [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "style": 5,
                        "label": "Trailer",
                        "url": trailer_url
                    }
                ]
            }
        ]

    requests.post(os.getenv("DISCORD_WEBHOOK_URL"), json=payload, headers={"Content-Type": "application/json"})
