from duckduckgo_search import DDGS
from fastcore.all import *
import time, json
from fastdownload import download_url

def search_images(keywords, max_images=200):
    ddgs = DDGS().images(keywords, max_results=max_images)
    return [d['image'] for d in ddgs]

urls = search_images('bird photos', max_images=1)
print(urls[0])

# Download a single test image of a bird
dest = 'bird.jpg'
download_url(urls[0], dest, show_progress=False)

# Dowlnoad 200 images of birds and forests (forest = "not bird")
searches = 'forest','bird'
path = Path('bird_or_not')

for o in searches:
    dest = (path/o)
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest, urls=search_images(f'{o} photo'))
    time.sleep(0.5)
    resize_images(path/o, max_size=400, dest=path/o)

# Remove images failed to download
failed = verify_images(get_image_files(path))
failed.map(Path.unlink)
print(len(failed))
