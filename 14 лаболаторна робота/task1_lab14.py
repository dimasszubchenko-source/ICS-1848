import json
import requests
from bs4 import BeautifulSoup

INPUT_FILE = 'web.txt'
OUTPUT_FILE = 'tables_result.json'
HEADERS = {'User-Agent': 'Mozilla/5.0 (lab14 student script)'}


def read_urls(filename):
    with open(filename, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def count_tables(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f'Помилка запиту до {url}: {e}')
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    return len(soup.find_all('table'))


def main():
    urls = read_urls(INPUT_FILE)
    result = []
    for url in urls:
        n = count_tables(url)
        print(f'{url} -> таблиць: {n}')
        result.append({'url': url, 'tables': n})

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print(f'Результат записано у файл {OUTPUT_FILE}')


if __name__ == '__main__':
    main()
