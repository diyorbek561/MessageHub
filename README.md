# 📬 MessageHub - Django Contact & Message Management System

**MessageHub** — foydalanuvchilardan murojaat va xabarlarni qabul qilish hamda ularni qulay jadval ko'rinishida boshqarish uchun mo'ljallangan Django web-loyihasi.

---

## 🚀 Xususiyatlari

* **Murojaat yuborish:** Foydalanuvchilar ism, familiya, telefon raqami, email va xabar matnini yuborishlari mumkin.
* **Avtomatik yo'naltirish:** Xabar yuborilgandan so'ng birdaniga xabarlar jadvali sahifasiga o'tiladi.
* **Jadval ko'rinishi:** Barcha kelib tushgan xabarlar tartiblangan va zamonaviy Bootstrap 5 jadvalida ko'rinadi.
* **Class-Based Views (CBV):** Kod toza va tez ishlashi uchun `CreateView` hamda `ListView`dan foydalanilgan.
* **Admin Panel:** Kelgan xabarlarni Django admin paneli orqali saralash va qidirish imkoniyati.

---

## 🛠 Ishlatilgan texnologiyalar

* **Backend:** Python 3.12, Django 5.x
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Database:** SQLite3

---

## ⚙️ Loyihani lokal kompyuterda ishga tushirish

### 1. RePO'ni klonlash yoki yuklab olish:
```bash
git clone https://github.com/diyorbek561/MessageHub.git

cd django-messagehub

2. Virtual muhitni yaratish va faollashtirish:

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Kutubxonalarni o'rnatish:

Bash
pip install django

4. Ma'lumotlar bazasini tayyorlash (Migratsiya):

Bash
python manage.py makemigrations
python manage.py migrate

5. Superuser (Admin) yaratish:
Bash
python manage.py createsuperuser

6. Local Serverni ishga tushirish:
Bash
python manage.py runserver
Brauzeringizda quyidagi manzillarga kiring:

Forma (Bosh sahifa): http://127.0.0.1:8000/

Xabarlar jadvali: http://127.0.0.1:8000/xabarlar/

Admin panel: http://127.0.0.1:8000/admin/

📂 Loyiha tuzilishi (Project Structure)

Plaintext
django-messagehub/
│
├── config/              # Asosiy loyiha sozlamalari (settings, urls)
├── post/                # Xabarlar ilovasi (app)
│   ├── migrations/      # Bazaviy migratsiyalar
│   ├── admin.py         # Admin panel sozlamalari
│   ├── forms.py         # PostForm formasi
│   ├── models.py        # Post modeli
│   ├── views.py         # PostCreateView va PostListView
│   └── urls.py          # App yo'nalishlari ('', 'xabarlar/')
│
├── templates/           # HTML shablonlar
│   ├── form.html        # Xabar yuborish formasi
│   └── index.html       # Xabarlar jadvali
│
├── manage.py
└── README.md
👨‍💻 Dasturchi: Diyorbek Berdimurodov (DiyorDev)
