import requests

# این آدرس رو عوض نکن
url = "https://api.priceto.day/v1/latest/irr/usd"

try:
    response = requests.get(url, timeout=30)
    data = response.json()
    # استخراج قیمت
    price = data.get("price")
    if price:
        with open("price.txt", "w") as f:
            f.write(str(price))
        print(f"Saved: {price}")
    else:
        print("Price not found")
except Exception as e:
    print(f"Error: {e}")
