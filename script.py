import requests
import re
import logging
import sys
import time

logging.basicConfig(format='%(levelname)s:%(message)s',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


links = [
    'https://mp3.zemra.org/Muzik-Shqip-2024/',
    'https://mp3.zemra.org/Muzik-Shqip-2023/'
]


def download_link(url: str):

    response = requests.get(url)
    if response.status_code == 200:
        links = re.findall(
            r'<a href="\?dir=([^"]+)">', response.text, re.IGNORECASE | re.MULTILINE)
        for i, link in enumerate(links):
            if i < 4:
                continue
            try:
                song_url = f'{url}?dir={link}'
                logger.info(song_url)
                response = requests.get(song_url)
                if response.status_code == 200:

                    download_song_url = song_url = f'{url}/{link}/{link}.mp3'
                    response = requests.get(download_song_url)
                    if response.status_code == 200:

                        with open(f'./mp3/{link}.mp3', 'wb') as w:
                            w.write(response.content)

                        logger.info(f"Saved {link}")
                    time.sleep(1)

                time.sleep(1)
            except Exception as e:
                logger.error(e)


if __name__ == "__main__":

    for link in links:
        download_link(link)
