"""Main module."""
import logging
from typing import Sequence

import spotipy
import spotipy.util as util
from environs import Env

logger = logging.getLogger(__name__)
_SCOPE = 'playlist-modify-public'
_MAX_TRACKS_COUNT = 100


def _to_chunks(lst, count) -> Sequence[str]:
    for i in range(0, len(lst), count):
        yield lst[i:i + count]


def add_tracks(username, playlist_id, tracks: Sequence[str]) -> None:
    # Read in .env
    env = Env()
    env.read_env()
    # Create client
    token = util.prompt_for_user_token(username, _SCOPE)
    client = spotipy.Spotify(auth=token)
    client.trace = False
    # Add the tracks, 100 at a time
    for chunk in _to_chunks(tracks, _MAX_TRACKS_COUNT):
        client.user_playlist_add_tracks(username, playlist_id, chunk)
