# TASKR — Mini Task Manager (Django REST Framework)

Full-stack Task Manager using **Django + DRF** on the backend and vanilla HTML/CSS/JS on the frontend.

---

## Project Structure

```
taskr_drf/
├── manage.py
├── requirements.txt
├── index.html                  # Frontend (open in browser)
├── db.sqlite3                  # Auto-created on first migrate
├── taskr_project/
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
└── tasks/
    ├── __init__.py
    ├── models.py               # Task model
    ├── serializers.py          # DRF ModelSerializer
    ├── views.py                # ModelViewSet + stats action
    └── urls.py                 # DRF DefaultRouter
```

---

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations (creates db.sqlite3 + tasks table)
python manage.py migrate

# 3. Start the dev server
python manage.py runserver
```

Backend runs at: `http://localhost:8000`

Then open `index.html` in your browser.

> **Note:** The frontend points to `localhost:5000` by default (Flask version).
> Change the `API` constant at the top of the `<script>` in `index.html` to:
> ```js
> const API = 'http://localhost:8000/api';
> ```

---

## REST API Endpoints

DRF's `DefaultRouter` auto-generates all routes from the `TaskViewSet`:

| Method | Endpoint              | Action              |
|--------|-----------------------|---------------------|
| GET    | /api/tasks            | List all tasks      |
| POST   | /api/tasks            | Create a task       |
| GET    | /api/tasks/:id        | Retrieve one task   |
| PATCH  | /api/tasks/:id        | Partial update      |
| DELETE | /api/tasks/:id        | Delete a task       |
| GET    | /api/tasks/stats      | Summary stats       |

### Example requests

```bash
# Create
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Write tests", "description": "Cover all endpoints"}'

# Toggle complete
curl -X PATCH http://localhost:8000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete
curl -X DELETE http://localhost:8000/api/tasks/1

# Stats
curl http://localhost:8000/api/tasks/stats
```

---

## Key DRF Concepts Used

| Concept | Usage |
|---|---|
| `ModelSerializer` | Auto-maps `Task` model fields to JSON |
| `ModelViewSet` | Provides all 5 CRUD actions in one class |
| `DefaultRouter` | Auto-registers all URL patterns |
| `@action` decorator | Custom `/stats` endpoint on the viewset |
| `django-cors-headers` | Allows frontend to call the API |

---

## Data persistence

Unlike the Flask version (in-memory), this version uses **SQLite** via Django's ORM — tasks persist across server restarts.
