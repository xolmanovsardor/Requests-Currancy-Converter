import requests

def USD_Valyuta()->None:
    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'
    getting = requests.get(url)
    data = getting.json()

    kurs = float(data[0]['Rate'])

    amout = float(input('dollor:'))
    total = kurs * amout
    print(f"{total:,.2f}")

    






