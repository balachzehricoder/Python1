from pytube import Playlist
import sys


def download_playlist(playlist_url):
    try:
        # Verify the URL
        if 'list=' not in playlist_url:
            raise ValueError("Invalid playlist URL. Please ensure the URL contains 'list='.")

        # Create a Playlist object
        playlist = Playlist(playlist_url)
        print(f'Downloading playlist: {playlist.title}')

        # Iterate through the videos and download them
        for video in playlist.videos:
            print(f'Downloading {video.title}...')
            video.streams.get_highest_resolution().download()
            print(f'Finished downloading {video.title}')

        print('All videos have been downloaded.')
    except ValueError as ve:
        print(f'ValueError: {ve}')
    except KeyError as ke:
        print(f'KeyError: {ke}')
    except Exception as e:
        print(f'An error occurred: {e}')
        sys.exit(1)


if __name__ == "__main__":
    playlist_url = input("Enter your playlist URL: ")
    download_playlist(playlist_url)
