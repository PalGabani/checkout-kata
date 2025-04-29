# 🛒 Checkout Kata — Django Project

This is a Django-based implementation of a **Supermarket Checkout System** that calculates the total price of items added to the cart, applying individual prices and bundle discount offers.

---

## 📦 Features

- 💡 Implements the **MVT Design Pattern**.
- 🧠 Uses **Object-Oriented Programming (OOP)** principles — checkout logic is encapsulated in a dedicated class.
- 🧾 Clean and professional project structure.
- 💻 User-friendly web interface to calculate total price.

---

## ⚙️ Project Setup

### Prerequisites:
- Python 3.x installed
- `pip` installed

---

### 🐍 1️⃣ Clone the Project

```bash
git clone <your-repo-link>
cd task_assesment
```

### 🐍 2️⃣ Create & Activate Virtual Environment
```bash
Copy
python -m venv venv
```
**Windows:**

```bash
Copy
venv\Scripts\activate
```
**Linux/Mac:**

```bash
Copy
source venv/bin/activate
```

### 🐍 3️⃣ Install Django
```bash
pip install django
```

### 🐍 4️⃣ Run Database Migrations
```bash
python manage.py migrate
```

### 🐍 5️⃣ Start the Django Development Server
```bash
python manage.py runserver
```
**Open your browser and visit:**

```cpp
http://127.0.0.1:8000/
```

---
**🧪 Testing Instructions**

### 💡 How to Use:
Open the webpage.

Enter a string of item codes (A, B, C, D...) in the input box.

Click "Calculate Total".

The total price will be displayed according to the pricing and discount rules.

### 💸 Product Price List:
```Item	Price	Discount Offer
A	₹50	3 for ₹130
B	₹30	2 for ₹45
C	₹20	No Discount
D	₹15	No Discount
```
### 💡 Example Test Cases:
```Input	Meaning	Output
""	No items	₹0
A	1xA	₹50
AB	1xA + 1xB	₹80
CDBA	C, D, B, A	₹115
AAABBD	3xA, 2xB, 1xD	₹190
AAAAAA	6xA (2 offers)	₹260
```

### ✅ Notes:
Input should be uppercase letters: A, B, C, D without spaces.

The system will automatically apply applicable discounts.

### 💼 Project Structure Overview
```
task_assesment/
├── checkout_project/
│   ├── settings.py
│   └── urls.py
├── cart/
│   ├── checkout.py      # OOP logic (Checkout class)
│   ├── views.py         # Handles request logic
│   ├── urls.py          # URL routing
│   └── templates/
│       └── cart/
│           └── checkout.html
├── manage.py
├── venv/
└── README.md
```

### Author:
Pal Gabani
palgabani03@gmail.com
