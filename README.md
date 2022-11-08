# BitPapa
Simple lib for connect to API p2p crypto-market "Bitpapa". 
It is unofficial lib for bitpapa.com API

## Dependencies:

```
pip install requests
pip install pyotp
```

## Authentication:
Put keys in connect.py

```
key = '<Your API key>'
totp = pyotp.TOTP('<Your 2fa code>')
```

## Examples:

1.Get ads list:

connect.search_ads(summ, type, bank, sort)

summ - How amount in fiat (default fiat - RUB, maybe change in connect.py code)
type - Type of ads ('Ad::Sell' or 'Ad:Buy')
bank - BitPapa Bank code ('B1'-Sberbank, 'B3'-Tinkoff etc...) 
sort - How to sort ads ('price' or '-price') 

```
import connect

con = connect.search_ads(5000, 'Ad::Sell', 'B3', 'price')
ads = con['ads']
print(ads)
```
