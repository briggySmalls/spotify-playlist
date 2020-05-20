"""Console script for birthday_playlist."""
import sys
import logging

import click

from birthday_playlist.birthday_playlist import add_tracks


@click.command()
@click.argument('username')
@click.argument('playlist')
@click.argument('track_file', type=click.File())
def main(username, playlist, track_file):
    """Console script for birthday_playlist."""
    # Setup logger
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Starting...")
    # Read the tracks
    tracks = track_file.read().splitlines()
    logging.debug("Found %d tracks", len(tracks))
    add_tracks(username, playlist, tracks)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
