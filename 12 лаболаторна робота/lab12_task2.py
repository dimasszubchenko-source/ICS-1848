# функція повертає домен 1-го рівня для URL-адреси
def get_domain(url):
    url = url.strip()
    # відкидаємо протокол (http://, https://)
    if "://" in url:
        url = url.split("://")[1]
    # залишаємо тільки адресу сайту (до першого /)
    host = url.split("/")[0]
    # останній елемент після крапки і є домен 1-го рівня
    return host.split(".")[-1]

f = open("urls.txt", "r", encoding="utf-8")
print("Домени 1-го рівня:")
for line in f:
    if line.strip() != "":
        print(line.strip(), "->", get_domain(line))
f.close()
