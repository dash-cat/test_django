# Django Company Structure

## Описание

Этот проект представляет веб-приложение для управления иерархической структурой отделов и сотрудников в компании. Использует Django в качестве backend-фреймворка, SQLite в качестве базы данных и нативный JavaScript для отображения древовидной структуры.

## Функционал

- Отображение иерархической структуры подразделений и сотрудников.
- CRUD-управление сотрудниками и отделами через Django Admin.
- API для получения структуры данных в JSON.
- Автоматическое заполнение базы данных 50 000 сотрудников и 25 подразделений.

## Требования

- Python 3.5+
- Django 3+
- SQLite (по умолчанию) или другая БД
- Faker (для генерации тестовых данных)

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <репозиторий>
cd company_structure
```

### 2. Создание виртуального окружения и установка зависимостей

```bash
python3 -m venv .venv
source .venv/bin/activate  # Для Linux/macOS
.venv\Scripts\activate  # Для Windows
pip install -r requirements.txt
```

### 3. Применение миграций

```bash
python manage.py makemigrations employees
python manage.py migrate
```

### 4. Создание суперпользователя (для доступа в Django Admin)

```bash
python manage.py createsuperuser
```

### 5. Заполнение базы тестовыми данными

```bash
python3 populate_db.py
```

### 6. Запуск сервера разработки

```bash
python manage.py runserver
```

Откройте в браузере:

- `http://127.0.0.1:8000/` — древовидное отображение структуры.
- `http://127.0.0.1:8000/admin/` — Django Admin для управления записями.

## API

- `GET /api/departments/` — Возвращает JSON с иерархией подразделений и сотрудников.

## Структура проекта

```
company_structure/
│── company_structure/   # Основной проект
│   ├── settings.py
│   ├── urls.py
│── employees/          # Приложение сотрудников
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   ├── index.html
│   ├── static/
│   │   ├── js/
│   │   │   ├── tree.js
│── manage.py
│── populate_db.py
│── requirements.txt
│── README.md
```
