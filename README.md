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

- Landing Page
![Landing Page](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/landingPage.png)

- Tour Page
![Tour](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/tour.png)

- Login/Register Page
![Login](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/login.png)

- Profile
![profile](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/profile.png)

![profile](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/profile2.png)

- Dashboard
![Dashboard](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/Screenshot%20from%202017-06-17%2013-39-27.png)

- List of Topics
![List Of Topics](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/topics.png)

- Study
![Study](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/study.png)

- Test
![Test](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/test.png)

- Analysis
![Analysis](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/analysis.png)

- Responsive design
![Responsive](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/responsive2.png)

![Responsive](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/responsive1.png)
