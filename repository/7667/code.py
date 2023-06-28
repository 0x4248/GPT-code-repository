import requests
import random

API_KEY = 'YOUR_API_KEY'  # Replace with your Last.fm API key

def get_top_artists(limit=10):
    """Fetches the top artists based on user preferences."""
    params = {
        'method': 'user.getTopArtists',
        'user': 'YOUR_USERNAME',  # Replace with your Last.fm username
        'api_key': API_KEY,
        'format': 'json',
        'limit': limit
    }
    response = requests.get('http://ws.audioscrobbler.com/2.0/', params=params)
    data = response.json()
    artists = [artist['name'] for artist in data['topartists']['artist']]
    return artists

def get_similar_artists(artist, limit=5):
    """Fetches similar artists based on the given artist."""
    params = {
        'method': 'artist.getSimilar',
        'artist': artist,
        'api_key': API_KEY,
        'format': 'json',
        'limit': limit
    }
    response = requests.get('http://ws.audioscrobbler.com/2.0/', params=params)
    data = response.json()
    similar_artists = [artist['name'] for artist in data['similarartists']['artist']]
    return similar_artists

def generate_playlist(genres, mood):
    """Generates a playlist based on user-defined genres and mood."""
    playlist = []
    for genre in genres:
        params = {
            'method': 'tag.getTopTracks',
            'tag': genre,
            'api_key': API_KEY,
            'format': 'json',
            'limit': 10
        }
        response = requests.get('http://ws.audioscrobbler.com/2.0/', params=params)
        data = response.json()
        tracks = [track['name'] for track in data['tracks']['track']]
        playlist.extend(tracks)

    random.shuffle(playlist)
    return playlist

# Main program
if __name__ == '__main__':
    genres = ['rock', 'pop', 'electronic']
    mood = 'upbeat'
    
    top_artists = get_top_artists()
    for artist in top_artists:
        similar_artists = get_similar_artists(artist)
        genres.extend(similar_artists)

    playlist = generate_playlist(genres, mood)
    print(f"Generated playlist ({len(playlist)} tracks):")
    for track in playlist:
        print(track)
