import requests

# API جایگزین: open.er-api.com (بلاک نمی‌کنه گیت‌هاب رو)
url = "https://open.er-api.com/v6/latest/USD"

try:
    response = requests.get(url, timeout=30)
    data = response.json()
    
    if data.get("result") == "success":
        irr_rate = data.get("rates", {}).get("IRR")
        if irr_rate:
            # تبدیل ریال به تومان
            toman_price = irr_rate / 10
            with open("price.txt", "w") as f:
                f.write(str(toman_price))
            print(f"Saved: {toman_price} Toman")
        else:
            print("IRR rate not found")
    else:
        print(f"API error: {data}")
except Exception as e:
    print(f"Exception: {e}")
