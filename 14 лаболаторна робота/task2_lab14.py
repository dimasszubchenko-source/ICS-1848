import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

INPUT_FILE = 'webpages.txt'
OUTPUT_FILE = 'links_result.txt'
HEADERS = {'User-Agent': 'Mozilla/5.0 (lab14 student script)'}


def read_urls(filename):
    with open(filename, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def is_com_link(page_url, href):
    """True, якщо href веде на сайт у домені .com."""
    full = urljoin(page_url, href)          # відносні посилання -> абсолютні
    parsed = urlparse(full)
    if parsed.scheme not in ('http', 'https'):
        return False                        # mailto:, javascript: тощо
    host = parsed.hostname or ''
    return host.endswith('.com')


def count_com_links(url):
    """Повертає кількість посилань на .com на сторінці або None при помилці."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f'Помилка запиту до {url}: {e}')
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    count = 0
    for link in soup.find_all('a'):
        if 'href' in link.attrs and is_com_link(url, link.attrs['href']):
            count += 1
    return count


def main():
    urls = read_urls(INPUT_FILE)
    lines = []
    total = 0
    for url in urls:
        n = count_com_links(url)
        if n is None:
            lines.append(f'{url} - сторінка недоступна')
        else:
            lines.append(f'{url} - посилань на .com: {n}')
            total += n
    lines.append(f'Усього посилань на сайти домену .com: {total}')

    text = '\n'.join(lines)
    print(text)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(text + '\n')


if __name__ == '__main__':
    main()
