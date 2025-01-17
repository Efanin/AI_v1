#pip install requests beautifulsoup4 pillow lxml
#pip install pillow
import requests
from bs4 import BeautifulSoup
from PIL import Image

query = input("Введите запрос: ")
response = requests.get(f"https://www.bing.com/images/search?q={query}")
soup = BeautifulSoup(response.content, 'html.parser').find('img', class_='mimg').get('src')
print(soup)
response = requests.get(soup, stream=True)
Image.open(response.raw).show()
