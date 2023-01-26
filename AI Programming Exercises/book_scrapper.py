import csv
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Whale/3.18.154.7 Safari/537.36'}

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    return soup

def extract_book_info():
    result = []

    for page in range(1, 3):
        url = f'http://www.yes24.com/24/category/bestseller?CategoryNumber=001001003031&sumgb=09&PageNumber={page}'
        soup = create_soup(url)

        books = soup.find_all('td', attrs={'class':'goodsTxtInfo'})

        for book in books:
            link = 'http://www.yes24.com' + book.find('a')['href']

            book_soup = create_soup(link)

            title = book_soup.find('h2', attrs={'class':'gd_name'}).get_text().strip()
            author = book_soup.find('span', attrs={'class': 'gd_auth'}).get_text().strip()
            publisher = book_soup.find('span', attrs={'class': 'gd_pub'}).get_text().strip()
            year = book_soup.find('span', attrs={'class': 'gd_date'}).get_text().strip()
            isbn = book_soup.find_all('td', attrs={'class':'txt lastCol'})[2].get_text().strip()

            book_data = {
                'title': title,
                'author': author[:author.find('저')],
                'publisher': publisher,
                'year': year[:year.find('년')],
                'isbn': isbn
            }

            result.append(book_data)
            
    return result

books = extract_book_info()

f = open('books.csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

title = ['도서명', '저자', '출판사', '출판년도', 'ISBN']
writer.writerow(title)

for book in books:
    writer.writerow(list(book.values()))

f.close()
