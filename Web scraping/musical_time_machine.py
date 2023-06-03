from bs4 import BeautifulSoup
import requests
import spotipy


# Getting response from Billboard WEB page
date = input("Select a date to which you would like to travel (YYYY-MM-DD): ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
selected_date_page = response.text

# Scraping the page for song titles
soup = BeautifulSoup(selected_date_page, "html.parser")
song_titles = soup.find_all('h3', {'id': 'title-of-a-story', 'class': 'c-title a-no-trucate a-font-primary-bold-s '
                                                                      'u-letter-spacing-0021 '
                                                                      'lrv-u-font-size-18@tablet lrv-u-font-size-16 '
                                                                      'u-line-height-125 '
                                                                      'u-line-height-normal@mobile-max '
                                                                      'a-truncate-ellipsis u-max-width-330 '
                                                                      'u-max-width-230@tablet-only'})
song_titles = [title.text.strip() for title in song_titles]

# Spotify authorization
CLIENT_ID_SPOTIFY = "fe9c890541494cbaad8876cc3958a393"
CLIENT_SECRET_SPOTIFY = "0151451c536643919bc3946a2f8e392f"
URL_REDIRECT = "http://example.com"

spotify = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID_SPOTIFY,
                                      client_secret=CLIENT_SECRET_SPOTIFY,
                                      redirect_uri=URL_REDIRECT)
access_token = spotify.get_cached_token()
spotify = spotipy.Spotify(auth=access_token['access_token'])

# Create an empty playlist on Spotify
playlist_name = "My Playlist"  # Replace with your desired playlist name
user_id = spotify.me()["id"]
playlist = spotify.user_playlist_create(user_id, playlist_name)
playlist_id = playlist["id"]

# Add songs to the playlist
for title in song_titles:
    results = spotify.search(q=title, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_uri = track['uri']
        spotify.user_playlist_add_tracks(user_id, playlist_id, [track_uri])