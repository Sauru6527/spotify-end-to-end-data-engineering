import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # client_id = os.environment.get('client_id')
    # client_secret = os.environment.get('client_secret')
    
    
    client_credentials_manager = SpotifyClientCredentials(client_id = '71a3d331eb60456693297696b0f7e1fe',client_secret = '3eaf067da06048518f5d2ac8e943288c')
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=875f311de02c4415"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    
    spotify_data = sp.playlist_tracks(playlist_URI)
    
    client = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    client.put_object(
        Bucket = "spotify-etl-project-sauru",
        Key = "raw_data/to_processed/" + filename,
        Body = json.dumps(spotify_data)
        )