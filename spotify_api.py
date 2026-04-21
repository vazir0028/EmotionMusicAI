import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE

playlists = {
    "happy": "spotify:playlist:37i9dQZF1DXdPec7aLTmlC",
    "sad": "spotify:playlist:37i9dQZF1DX7qK8ma5wgG1",
    "angry": "spotify:playlist:37i9dQZF1DWYNSmSSRFIWg",
    "neutral": "spotify:playlist:37i9dQZF1DX2sUQwD7tbmL",
    "surprise": "spotify:playlist:37i9dQZF1DXa2PvUpywmrr",
    "fear": "spotify:playlist:37i9dQZF1DX4fpCWaHOned"
}

def login_spotify():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE,
            open_browser=True
        )
    )
    return sp

def play_music(sp, emotion):
    devices = sp.devices()["devices"]

    if not devices:
        return False

    device_id = devices[0]["id"]
    uri = playlists.get(emotion, playlists["neutral"])

    sp.start_playback(device_id=device_id, context_uri=uri)
    return True
