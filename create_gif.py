from urllib import response
import requests
from PIL import Image
from io import BytesIO

URL = 'https://api.github.com/repos/awhipp/100mb-daily-random-text/releases?per_page=100'
previous_charts = []
page = 1

while True:
    response = requests.get(f'{URL}&page={page}')
    response.raise_for_status()

    payload = response.json()

    if len(payload) == 0:
        break

    for obj in payload:
        assets = obj['assets']
        for asset in assets:
            if 'png' in asset['browser_download_url']:
                previous_charts.append( asset['browser_download_url'])
    page += 1

previous_charts = previous_charts[::-1]

imgs = []
for idx, chart in enumerate(previous_charts):
    print(f'Retrieving ({idx} of {len(previous_charts)}): {chart}')
    response = requests.get(chart)
    img = Image.open(BytesIO(response.content))
    imgs.append(img)

chart = 'current_distribution.png'
print(f'Retrieving ({len(previous_charts)} of {len(previous_charts)}): {chart}')
img = Image.open(chart)
imgs.append(img)

imgs[0].save(fp="current_distribution.gif", save_all=True, append_images=imgs[1:], optimize=True, duration=200, loop=0)

print('Done.')
