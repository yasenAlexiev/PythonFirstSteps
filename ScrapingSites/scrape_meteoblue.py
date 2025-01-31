import requests
import bs4

python_req = requests.get("https://www.meteoblue.com/en/weather/week/sofia_bulgaria_727011")

soup = bs4.BeautifulSoup(python_req.text, "lxml")
images = soup.select(".weather-pictogram ")
for image in images:
    image_url = image['src']
    image_req = requests.get(image_url)
    image_name = image_url.split('/')[-1]
    f = open(image_name, 'wb')
    f.write(image_req.content)
    f.close()
