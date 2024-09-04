import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks_from_url(playlist_url):
    # Set up your Spotify credentials
    client_id = 'da6b139e19754cbcb15f6ce202f54746'
    client_secret = '3d00001e4ba14ba68c9a0c7c9af332e3'

    # Authenticate
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Extract playlist ID from URL
    playlist_id = playlist_url.split('/')[-1].split('?')[0]

    # Fetch playlist tracks
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    # Get track names
    track_names = [track['track']['name'] for track in tracks]
    return track_names

# Example usage
playlist_url = 'https://open.spotify.com/playlist/4jrqpB0oAqwHXezHhZThgH?si=ca72d0d4394945a6'
song_names = get_playlist_tracks_from_url(playlist_url)
print(song_names)
