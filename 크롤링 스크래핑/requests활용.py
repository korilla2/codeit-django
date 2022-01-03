import requests
from fake_useragent import UserAgent

url = 'https://image.zdnet.co.kr/2022/01/01/e601fd8d72cc33ca75cd9d41d3315684.jpg'
agent = UserAgent()
headers = {
    'User-Agent': agent.chrome}

response = requests.get(url, headers=headers)

with open('../크롤링 스크래핑/images/data2.jpg', 'wb') as file:
    file.write(response.content)
