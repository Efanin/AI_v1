#pip install requests beautifulsoup4 pillow lxml auto-py-to-exe
import requests
from bs4 import BeautifulSoup
from PIL import Image

query = input("Введите запрос ")
response = requests.get(f"https://www.bing.com/images/search?q={query}")
image = BeautifulSoup(response.content, 'lxml').find('img',class_='mimg').get('src')
print(image)
response = requests.get(image, stream=True)
Image.open(response.raw).show()
