import requests

# استفاده از exchangerate-api.com (نسخه رایگان بدون key)
url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url, timeout=30)
    data = response.json()
    
    # نرخ ریال
    irr_rate = data.get("rates", {}).get("IRR")
    
    if irr_rate:
        # تبدیل ریال به تومان (تقسیم بر 10)
        toman_price = irr_rate / 10
        with open("price.txt", "w") as f:
            f.write(str(toman_price))
        print(f"Saved: {toman_price} Toman")
    else:
        print(f"IRR not found. Full data: {data}")
except Exception as e:
    print(f"Exception: {e}")
