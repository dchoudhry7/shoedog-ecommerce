# 🛒 Shoedog E-commerce

A clean and minimal e-commerce web application built using Django, featuring product browsing, cart management, and user authentication.

---

## 🚀 Features

* 🏠 Product listing homepage
* 🔐 User authentication (Login / Signup / Logout)
* 🛒 Add to cart functionality
* ➕➖ Quantity management (increase / decrease items)
* 💰 Subtotal and total price calculation
* 📦 Cart page with structured UI
* 🎯 Responsive design using Bootstrap

---

## 🖼️ Screenshots

### 🏠 Homepage

![Homepage](assets/Screenshot%20(866).png)

### 🔐 Login Page

![Login](assets/Screenshot%20(864).png)

### 📝 Signup Page

![Signup](assets/Screenshot%20(865).png)

### 🛒 Cart Page

![Cart](assets/Screenshot%20(867).png)
![Cart](assets/Screenshot%20(868).png)

### 💳 Checkout Page

![Checkout](![Cart](assets/Screenshot%20(869).png))

---

## 🧑‍💻 Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Templating:** Django Templates

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
env\Scripts\activate      # Windows
# source env/bin/activate # Mac/Linux
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

* Uses **One-to-One relationship** to link user and cart
* Implements **server-side rendering with Django templates**
* Clean UI built using Bootstrap
* Modular structure for scalability

---

## 🔮 Future Improvements

* AJAX-based cart updates (no page reloads)
* Payment gateway integration (Stripe/Razorpay)
* Order history & tracking
* Product search & filters

---

## 👤 Author

**Dhairya Choudhry**
🔗 GitHub: https://github.com/dchoudhry7

---

## ⭐ Show Your Support

If you found this project useful, consider giving it a ⭐ on GitHub!