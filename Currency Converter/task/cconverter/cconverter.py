import requests


def dictionary(want_currency):
    cash.update({want_currency: float(r[want_currency]['rate'])})
    return cash


currency = input().lower()
r = requests.get(f'http://www.floatrates.com/daily/{currency}.json').json()
cash = {}

if currency != 'usd':
    dictionary('usd')
    dictionary('eur')
elif currency == 'usd':
    dictionary('eur')
else:
    dictionary('usd')

while True:
    want_currency = input().lower()

    if want_currency == '':
        break

    money = float(input())

    print('Checking the cache...')

    if want_currency in cash:
        print('Oh! It is in the cache!')

        print(f'You received {round(cash[want_currency] * money, 2)} {str(want_currency).upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        dictionary(want_currency)
        print(f'You received {round(cash[want_currency] * money, 2)} {str(want_currency).upper()}.')

