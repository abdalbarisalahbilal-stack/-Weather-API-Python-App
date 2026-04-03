# 🌤️ Weather API Python App

## 📌 Overview

This project is a simple and powerful Python application that fetches real-time weather data using an external API.

The user enters a city name, and the program returns:

* 🌡️ Temperature
* 🌤️ Weather condition

---

## 🚀 Features

* Fetch real-time weather data
* Clean and simple CLI interface
* Error handling for invalid cities
* Supports Arabic language 🌍
* Easy to extend (Telegram bot, GUI, etc.)

---

## 🛠️ Technologies Used

* Python 🐍
* Requests Library
* REST API (OpenWeather)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-api-python.git
cd weather-api-python
```

### 2. Install dependencies

```bash
pip install requests
```

---

## 🔑 Setup API Key

1. Create an account on OpenWeather
2. Get your API Key
3. Replace it in the code:

```python
api_key = "YOUR_API_KEY_HERE"
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

Then enter a city:

```bash
🌍 اكتب اسم مدينة: Kuala Lumpur
```

### Example Output:

```
📍 المدينة: Kuala Lumpur
🌡️ الحرارة: 30°C
🌤️ الحالة: غائم
```

---

## ⚠️ Error Handling

* ❌ Invalid city → shows error message
* ❌ Invalid API key → shows API error
* ✅ Status code checking implemented

---

## 📁 Project Structure

```
weather-api-python/
│── main.py
│── README.md
```

---

## 🔥 Future Improvements

* 🤖 Convert to Telegram Bot
* 🖥️ Add GUI (Tkinter / PyQt)
* 🌍 Multi-language support
* 📊 Show more weather details

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to open issues for suggestions or bugs.

---

## 📜 License

This project is open-source and free to use.

---

## 💡 Author

Developed by **[Your Name]**

---

## ⭐ Support

If you like this project, give it a star ⭐ on GitHub!

