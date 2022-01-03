import requests
import bs4

for i in range(1, 11):
    url = f'https://movie.naver.com/movie/point/af/list.naver?&page={i}'
    response = requests.get(url)
    html = response.text
    review = bs4.BeautifulSoup(html, 'html.parser')

    search = {
        'class': 'title'
    }

    td_elements = review.find_all('td', attrs=search)
    print('=' * 20)
    print(f'{i} 시작')
    for element in td_elements:
        li = element.text.split("\n")
        print(f'{li[1]}')
        print(f'{li[3]}')
        print(f'{li[5]}')
        print()
    print(f'{i} 종료')
    print('=' * 20)
