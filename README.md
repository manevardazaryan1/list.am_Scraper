<h1><a id="top">list.am_Scraper</a></h1>

## Description:
### This Django application is designed to scrape information from the list.am website using a provided page URL. It extracts relevant data and makes it accessible within your Django project.

![list.am_Scraper collage](main/static/main/images/README-collage.jpg "list.am_Scraper app")

## Key Features:

- **URL-based Scraping:** Accepts a list.am page URL as input and fetches data.
- **Data Extraction:** Extracts desired information from the specified page. (Please note that scraping practices should be aligned with the website's terms and conditions.)
- **Django Integration:** Seamlessly integrates with your Django project, allowing you to process and utilize the scraped data.

## To run this application, you'll need the following software installed on your system:

- **Git:** Ensure you have Git installed on your system. You can download it from https://git-scm.com/downloads.
- **Python:** Verify that you have Python 3.x installed. Check the version using python3 --version in your terminal. If you don't have it, download the appropriate installer from https://www.python.org/downloads/.
- **pip:** Pip is the package installer for Python. Use python3 -m ensurepip to install it if necessary.

## To run this application follow these steps

1. **Clone this repository:**
   git clone [https://github.com/manevardazaryan1/list.am_Scraper]

2. **Create a Virtual Environment (Recommended):**
    **Using venv (Python 3.3+):**
    cd [REPOSITORY_NAME]  # Navigate to your project directory
    python3 -m venv venv  # Create a virtual environment named 'venv'
    source venv/bin/activate  # Activate the virtual environment

    **Using virtualenv (Older Python versions or external package manager):**
    cd [REPOSITORY_NAME]  # Navigate to your project directory
    virtualenv venv  # Create a virtual environment named 'venv'
    source venv/bin/activate  # Activate the virtual environment

3. **Install Dependencies:**
    pip install -r requirements.txt

4. **Start the Development Server:**
    cd [list.am_Scraper]
    python manage.py runserver

This command starts the Django development server, typically running at http://127.0.0.1:8000/ by default. You can access your Django application in a web browser at this URL.

[Tap to Top ⬆](#top)