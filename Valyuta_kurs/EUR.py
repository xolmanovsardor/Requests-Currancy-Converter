import requests

def EUR_Valyuta() -> None:
    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/'
    getting = requests.get(url)
    data = getting.json()

    kurs = float(data[0]['Rate'])

    amount = float(input('Yevro: '))
    total = kurs * amount
    print(f"{total:,.2f}")

EUR_Valyuta()
