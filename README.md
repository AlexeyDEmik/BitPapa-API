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

### 1. Get your ads list:
```
import connect
data = connect.get_ads()
print(data)
```
Print all your ads (ads_id, bank_code, type etc...)

### 2. Get public ads list:
```
connect.search_ads(summ, type, bank, sort)
```

summ - How amount in fiat (default fiat - RUB, maybe change in connect.py code)

type - Type of ads ('Ad::Sell' or 'Ad::Buy')

bank - BitPapa Bank code ('B1'-Sberbank, 'B3'-Tinkoff etc...) 

sort - How to sort ads ('price' or '-price') 

```
import connect

con = connect.search_ads(5000, 'Ad::Sell', 'B3', 'price')
ads = con['ads']
print(ads)
```
### 3. Update ads price:
```
connect.update_ads(ads, price)
```

ads - Ads "id" (copy ads_id from your ads list)

price - New price for your ads

```
import connect

connect.update_ads('32b130f4-633f-5bfe-bf61-1e2382bf2c84', 1234567)
```
### 4. Trades list:
```
connect.contact_list(status)
```
status - Filter of your trades ('dispute', 'opened', 'closed', 'cancelled', 'paid')

```
import connect

data = connect.contact_list('opened')
print(data['trades'])
```


### 5. Complete trade:
```
connect.trade_complete(id)
```
id - ID of the deal to be finished

