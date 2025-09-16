## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone git@github.com:letebrhan/mwc3-2024-django-workshop.git
cd mwc3-2024-django-workshop
```

### 2. Create & activate a virtual environment
```bash
# Linux/macOS
python3.12 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py makemigrations tickets
python manage.py migrate
```

### 5. (Optional) Create an admin user
```bash
python manage.py createsuperuser
```

### 6. (Optional) Add sample tickets
```bash
python manage.py shell
```
```python
from tickets.models import Ticket
Ticket.objects.create(name="Fix login redirect", description="Check redirect after login", priority=1, completed=False)
Ticket.objects.create(name="Docs polish", description="Update README formatting", priority=3, completed=True)
exit()
```

### 7. Run the server
```bash
python manage.py runserver
```

### Access
- Site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
