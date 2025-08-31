## ⚙️ Setup & Installation

### 1. Clone the repo
git clone git@github.com:letebrhan/mwc3-2024-django-workshop.git
cd mwc3-2024-django-workshop


# 2. Create & activate a virtual environment
python3.12 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create an admin user (follow prompts)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver


# Access
Site: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/