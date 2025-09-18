import requests

def fetch_anime(limit=25):
    query = """
    query ($page: Int, $perPage: Int) {
      Page(page: $page, perPage: $perPage) {
        media(
          type: ANIME,
          status: FINISHED,
          sort: END_DATE_DESC,
          genre_not_in: ["Hentai"]
        ) {
          id
          format
          title {
            romaji
          }
          genres
          coverImage {
            large
          }
          countryOfOrigin
        }
      }
    }
    """
    variables = {"page": 1, "perPage": limit}
    response = requests.post("https://graphql.anilist.co", json={"query": query, "variables": variables})
    if response.status_code != 200:
        return []
    data = response.json()
    if "errors" in data:
        return []
    return data.get("data", {}).get("Page", {}).get("media", [])
