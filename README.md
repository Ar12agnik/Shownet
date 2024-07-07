---

# Netflix Clone using Django

A simple Netflix clone built with Django, allowing you to add and watch movies on localhost.

## Features
- Add movies through the Django admin interface.
- Watch movies without needing to log in.

## Prerequisites
- Python 3.x
- Django 3.x or later
- SQLite (default database for Django)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/netflix-clone.git
   cd netflix-clone
   ```


2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Adding Movies

1. **Access the admin interface:**
   Open your web browser and go to `http://127.0.0.1:8000/admin`.

2. **Log in:**
   Use the superuser credentials you created earlier.

3. **Add Movies:**
   - In the admin interface, navigate to the Movies section.
   - Click "Add Movie" and fill in the required details.
   - Save the movie. Repeat this step for all movies you want to add.

## Watching Movies

1. **Open your browser:**
   Navigate to `http://127.0.0.1:8000`.

2. **Browse and watch:**
   You should see a list of movies. Click on a movie to start watching.


## Contributing
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

## License
This project is open source and available under the [MIT License](LICENSE).

---
