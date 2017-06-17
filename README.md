# Studeely

This application is a tutoring system with focus on dynamic content generation. The application can dynamically fetch content from wikipedia, given a link, and also can create Multiple Choice Questions (MCQs) based on the same. There is no data storage, and absolutely no human intervention for generation of the content. 

Apart from dynamicity, the application also focuses on the aestheticity and look-and-feel of the user interface. The application itself is written in Python web framework named Django. We have implemented various javascript libraries like `skrollr.js` and `raindrops.js` to enhance the visual appeal of the application. There are custom python scrapers written using `BeautifulSoup` library to fetch content dynamically.

### Setting up

- Clone/Download the repo.

- You must first set up python virtual environment. Refer [this tutorial](https://rikenshah.github.io/articles/setting-up-python-environment/).

- Install dependencies using `pip install -r requirements.txt`.

- In the DjangoProject, start the django server using `python manage.py runserver` and it will show that the server is running on `localhost:8000`, for example. 

- Open that up in a browser.

### Features

- Landing Page with beautiful animations
- Tour Page
- Login/Register Page
- Profile
- Dashboard
- List of Topics
- Study
- Test
- Analysis
- Responsive design