import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

url = 'https://senkuro.com/anime/one-punch-man/characters'
req = requests.get(url)
soup = BeautifulSoup(req.content, "lxml")

# Находим блоки с персонажами
characters = soup.find_all('a', class_='card card-list card-ind')

for index, character in enumerate(characters):

    name = 'Ванпанчмен'
    poster = 'https://mirai.senkuro.net/anime/55450460120441216/covers' \
             '/9b927d47e770b9bb7b478a5b71b3ef0d10723b76_55607514456166947.jpeg'
    hero = character.find('h3', class_='card-title').text
    url = character.find('img')['src']
    group = 'Аниме'

    data = []

    data.append({
            'index_character': index,
            'name': name,
            'poster': poster,
            'hero': hero,
            'url': url,
            'group': group
    })

url_existing_data = 'https://raw.githubusercontent.com/yupest/guess_who/main/data/data.csv'
existing_data = pd.read_csv(url_existing_data)
df = pd.DataFrame(data)

max_index = existing_data['index'].max()
max_index_world = existing_data['index_world'].max()

new_indices = list(range(max_index + 1, max_index + 1 + len(df)))
new_indices_world = list(range(max_index_world + 1, max_index_world + 1 + len(df)))

df['index'] = new_indices
df['index_world'] = new_indices_world

combined_data = pd.concat([existing_data, df], ignore_index=True)
combined_data.to_csv('combined_dataND1.0.csv', index=False)