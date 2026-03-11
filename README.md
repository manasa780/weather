# 🌦 Weather Forecast Web Application

## 📌 Project Overview

The **Weather Forecast Web Application** is a web-based project that allows users to check real-time weather information for any city.
The application retrieves weather data from an external weather API and displays details such as temperature, humidity, wind speed, and weather conditions in a user-friendly interface.

This project demonstrates integration of **backend APIs, frontend UI, and external data services**.

---

## 🚀 Features

* 🌍 Search weather by **city name**
* 🌡 Display **current temperature**
* ☁ Show **weather condition** (cloudy, sunny, rainy, etc.)
* 💧 Show **humidity level**
* 💨 Display **wind speed**
* 🕒 Real-time weather updates using API
* 📱 Simple and responsive interface

---

## 🛠 Technologies Used

**Frontend**

* HTML
* CSS
* JavaScript
* Bootstrap (optional)

**Backend**

* Python
* Django / Django REST Framework

**API**

* OpenWeatherMap API (or any weather API)

---

## 📂 Project Structure

```
weather_project/
│
├── weather_app/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation and Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/weather-project.git
cd weather-project
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Linux/Mac

```
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Development Server

```
python manage.py runserver
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:8000
```

---

## 🔑 API Configuration

1. Create an account on a weather API provider.
2. Generate an **API key**.
3. Add the API key in the project settings or environment variables.

Example:

```
API_KEY = "your_api_key_here"
```

---


---

## 🎯 Learning Outcomes

This project helps in understanding:

* API integration
* Backend development using Django
* Handling HTTP requests and responses
* Frontend and backend communication
* Building real-world web applications

---

## 👩‍💻 Author

**Manasa**

Python Full Stack Developer (Fresher)
Interested in Web Development, Cloud Technologies, and Backend Engineering.

---

## 📄 License

This project is open-source and available for learning and educational purposes.
