import requests
import json

# استفاده از Navasan API (متن‌باز و مناسب بازار ایران)
url = "https://api.navasan.tech/latest/?api_key=free&item=usd_sell"

try:
    response = requests.get(url, timeout=30)
    data = response.json()

    # استخراج قیمت فروش دلار (به ریال)
    # ساختار پاسخ ممکن است متفاوت باشد، این را بررسی کنید
    price_rial = data.get("usd_sell") or data.get("value")

    if price_rial:
        # تبدیل ریال به تومان (تقسیم بر 10)
        toman_price = float(price_rial) / 10
        with open("price.txt", "w") as f:
            f.write(str(toman_price))
        print(f"Saved: {toman_price} Toman")
    else:
        print(f"Price not found in response: {data}")
except Exception as e:
    print(f"Exception: {e}")
