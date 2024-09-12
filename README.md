ShambaScape
ShambaScape is a garden design web application tailored for garden enthusiasts who want to design beautiful and functional gardens. It allows users to plan tasks, view plant details, and set reminders, making it easier to manage gardening activities.

Features
Garden Design: Create and manage your garden designs with ease.
Plant Details: Explore details about different plant types, categorized for quick access.
Task Planner: Plan and manage your gardening tasks with due dates and task descriptions.
Reminders: Set reminders for important gardening tasks, so you never miss a beat.
Mobile-Friendly: Designed to work seamlessly across various devices.

Tech Stack
Front-End: HTML, CSS, JavaScript
Back-End: Python, Django Framework
Database: PostgreSQL
Hosting: Heroku
Static File Management: WhiteNoise

Installation
To run this project locally, follow these steps:

    Clone the repository:
        git clone https://github.com/your-username/ShambaScape.git
        cd ShambaScape

    Create a virtual environment:
        python3 -m venv env
        source env/bin/activate  # On Windows use `env\Scripts\activate`

    Install dependencies:
        pip install -r requirements.txt

    Set up environment variables:
    Create a .env file and add the following variables (with appropriate values):
        DJANGO_SECRET_KEY=your_secret_key
        DATABASE_URL=your_postgresql_url

    Run migrations:
        python manage.py migrate

    Start the development server:
        python manage.py runserver
        Now, visit http://127.0.0.1:8000/ to view the app locally.

Usage
Navigate through the Home, Design, Plants, and Planner sections to explore the features.
Add new garden designs, create tasks, view plant details, and set reminders for your gardening needs.

Deployment
ShambaScape is deployed on Heroku. To deploy your own version:

    Install the Heroku CLI:
        curl https://cli-assets.heroku.com/install.sh | sh
    
    Login to Heroku:
        heroku login

    Create a new Heroku app:
    heroku create your-app-name
    
    Add Heroku Postgres:
    heroku addons:create heroku-postgresql:hobby-dev
    
    Deploy to Heroku:
        git push heroku main

    Run database migrations on Heroku:
        heroku run python manage.py migrate
    
    Visit your app:
        heroku open

About
Developed by Geoffrey Gachuiri as part of a garden design portfolio project. Contributions are welcome! Feel free to submit a pull request or suggest improvements.

Visit the live app
GitHub Repository

License
This project is licensed under the MIT License - see the LICENSE file for details.