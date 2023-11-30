# Django Task Management

Welcome to the Django Task Management project! This web application helps you manage and keep track of your tasks with a clean and user-friendly interface.

## Table of Contents 📝

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- View all tasks on the homepage.
- Search tasks by title or tag.
- View individual tasks on a separate page.
- Navigation bar for easy access to different sections.
- Clean and modern design using Bootstrap.
- Responsive HTML for optimal viewing on various devices.
- Change UI to the dark version by button.

## Installation 💻

1. Clone the repository:

    ```bash
    git clone https://github.com/shayanpzp/Task_Management.git
    ```

2. Change into the project directory:

    ```bash
    cd Task_Management
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the Task Management application.

## Project Structure 🚀

```plaintext
Src/
    core/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        forms.py
        urls.py
        views.py
    manage.py
    static/
        css/
            dark-mode.css
        js/
            dark-mode.js
    src/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    templates/
        img/
            Alternate_Task_Manager_icon.png
        add_task.html
        base.html
        all_tasks.html
        search_tasks.html
        delete_task.html
        edit_task.html
        view_task.html
    .gitignore
    README.md
    requirements.txt
