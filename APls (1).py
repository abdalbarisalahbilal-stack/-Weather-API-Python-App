import requests

api_key = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

city = input("🌍 اكتب اسم مدينة: ").strip()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ar"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    print(f"\n📍 المدينة: {city}")
    print(f"🌡️ الحرارة: {temp}°C")
    print(f"🌤️ الحالة: {desc}")


else:
    print("❌ لم يتم العثور على المدينة أو حدث خطأ")