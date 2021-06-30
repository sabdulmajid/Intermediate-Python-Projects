# MultipleWebScraping.py
from re import T
from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")

box = soup.find('article', class_='main-article')

links = [link['href'] for link in box.find_all('a', href=True)]
# print(links)

for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, "lxml")

    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find("div", class_='full-script').get_text(strip=True, separator=" ")

    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)