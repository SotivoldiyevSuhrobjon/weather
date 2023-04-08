import requests
from bs4 import BeautifulSoup as bs
from data.config import IP
import aiohttp


# teacher in write weatherman
# async def get_current_weather_api(city):
#     url = f'https://www.timeanddate.com/weather/?type=ext&query={city}'
#     r = requests.get(url)
#     # print(r.status_code)
#     soup = bs(r.content, 'html.parser')
#     s = soup.find('td', attrs={'class': 'r'})
#     n = soup.find('td', attrs={'class' : 'rbi'})
#     a = soup.find('strong', attrs={'id': 'ctu'})
#     return n.text, s.text, a.text


async def get_current_weather_api(city):
    url  =f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={IP}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            s = await response.json()
            return s