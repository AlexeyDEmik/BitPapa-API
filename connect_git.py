import http.client
import requests
import pyotp

key = ''
totp = pyotp.TOTP('')

def get_ads() -> dict:

    data = requests.get('https://bitpapa.com/api/v1/me/pro', timeout=10, headers={
        'Content-Type': "application/json",
        'X-Access-Token': key
        })
    return data.json()

def search_ads(amount: int, type: str, bank: str, sort) -> dict:
    data = requests.get('https://bitpapa.com/api/v1/pro/search', timeout=10, headers={
        'Content-Type': "application/json",
        'X-Access-Token': key
    },
                        params={
                            "sort": f"{sort}",
                            "country_code": "RU",
                            "amount": f"{amount}",
                            "crypto_currency_code": 'BTC',
                            "currency_code": 'RUB',
                            "type": f"{type}",
                            "payment_method_bank_code": f"{bank}",
                            "limit": '15',
                        })
    return data.json()

def update_ads(id: str, price: int) -> dict:

    data = requests.put(f'https://bitpapa.com/api/v1/pro/{id}', timeout=10, data="{\n \"equation\": %d\n}" % price, headers={
        'Content-Type': "application/json",
        'X-Access-Token': key
    })
    return data.status_code

def contact_list(status: str):
    data = requests.get('https://bitpapa.com/api/v1/trades', timeout=10, headers={
        'Content-Type': "application/json",
        'X-Access-Token': key
    },
                        params={
                                   "status": f"{status}"
                        })
    return data.json()

def chat(trade_id: str):
    data = requests.get(f'https://bitpapa.com/api/v1/trades/{trade_id}/trade_conversation', timeout=10, headers={
        'Content-Type': "application/json",
        'X-Access-Token': key
    })
    return data.json()

def trade_complete(trade_id: str):
    code = totp.now()
    data = requests.post(f'https://bitpapa.com/api/v1/trades/{trade_id}/complete', data="{\n \"code\": %s\n}" % code, headers={
        'Content-Type': "application/json",
        'X-Access-Token': key
    })
    return data.status_code
