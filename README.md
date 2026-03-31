# 🛒 Shoedog E-commerce

A modern, minimal e-commerce web application built using Django, featuring a clean UI, cart functionality, and dynamic user interactions.

---

## 🚀 Features

* 🏠 Product listing homepage
* 🔐 User authentication (Login / Signup / Logout)
* 🛒 Add to cart functionality
* 🔄 Dynamic quantity updates (AJAX-based)
* 💰 Real-time subtotal calculation
* 📦 Cart management system
* 🎯 Clean and responsive UI (Bootstrap)

---

## 🖼️ Screenshots

### 🏠 Homepage

![Homepage](IMAGE_URL_HERE)

### 🔐 Login Page

![Login](IMAGE_URL_HERE)

### 📝 Signup Page

![Signup](IMAGE_URL_HERE)

### 🛒 Cart Page

![Cart](IMAGE_URL_HERE)

### 💳 Checkout Page

![Checkout](IMAGE_URL_HERE)

---

## 🧑‍💻 Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap
* **JavaScript:** Fetch API (AJAX)
* **Database:** SQLite

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/dchoudhry7/shoedog-ecommerce.git
cd shoedog-ecommerce
```

---

### 2. Create virtual environment

```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run migrations

```bash
python manage.py migrate
```

---

### 5. Run the server

```bash
python manage.py runserver
```

---

## 📂 Project Structure (Simplified)

```
shoedog/
│── store/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│
│── manage.py
│── db.sqlite3
```

---

## 🎯 Key Highlights

* Uses **One-to-One relationship** for user-cart mapping
* Implements **AJAX for seamless UI updates (no page reloads)**
* Clean separation of frontend and backend logic
* Designed with scalability and readability in mind

---

## 🔮 Future Improvements

* Payment gateway integration (Stripe/Razorpay)
* Order history & tracking
* Product search & filters
* Admin dashboard enhancements

---

## 👤 Author

**Dhairya Choudhry**
🔗 GitHub: https://github.com/dchoudhry7

---

## ⭐ Show Your Support

If you found this project useful, consider giving it a ⭐ on GitHub!
