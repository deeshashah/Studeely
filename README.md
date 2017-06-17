# Studeely

Check out the application [here](http://studeely.herokuapp.com/).

This application is a tutoring system with the focus on dynamic content generation. The application can dynamically fetch content from Wikipedia, given a link, and also can create Multiple Choice Questions (MCQs) based on the same. There is no data storage, and absolutely no human intervention for generation of the content. 

Apart from dynamicity, the application also focuses on the aesthetics and look-and-feel of the user interface. The application itself is written in Python web framework named Django. We have implemented various javascript libraries like `skrollr.js` and `raindrops.js` to enhance the visual appeal of the application. There are custom python scrapers written using `BeautifulSoup` library to fetch content dynamically.

### Technologies used

- Django (Python web framework) for backend
- Python scripts for dynamically scraping content
- Bootstrap and many javascript libraries for frontend

### Setting up

- Clone/Download the repo.

- You must first set up python virtual environment. Refer [this tutorial](https://rikenshah.github.io/articles/setting-up-python-environment/).

- Install dependencies using `pip install -r requirements.txt`.

- In the DjangoProject, start the Django server using `python manage.py runserver` and it will show that the server is running on `localhost:8000`, for example. 

- Open that up in a browser.

### Features

#### Landing Page

We have used beautiful animations to make the landing page attractive. Navbar, Login button, Sliders, Raindrops effect, team image slider, a message sent animation, etc. have been used in order to enhance the visual appeal of the webpage.

![Landing Page](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/landingPage.png)

#### Tour Page

For this, we have used a javascript library named 'skrollr.js'. When the user scrolls down, the effects change and the information is displayed progressively.

![Tour](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/tour.png)


#### Login/Register Page

You can make a new user account, and then login to use the application.

![Login](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/login.png)


#### Profile

Using a material design snippet, we have implemented to use user profile and we plan to extend our application to support customized user experience.

![profile](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/profile.png)

![profile](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/profile2.png)


#### Dashboard

Here the user is displayed with two very simple options to either study or take a test.

![Dashboard](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/Screenshot%20from%202017-06-17%2013-39-27.png)


#### List of Topics

List of topics is displayed on this page.

![List Of Topics](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/topics.png)


#### Study

The topic content is fetched dynamically and the user can see nicely paginated content just not to get overwhelmed and process information in a progressive pattern.

![Study](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/study.png)


#### Test

The questions are formed dynamically using either a bold or hyperlinked word and the random options are selected from the pool of other bold or hyperlinked words. Hence this whole process is dynamic. Also, every time a new set of questions is generated.

![Test](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/test.png)


#### Analysis

After selecting choices, the system evaluates and gives the result to indicate which was correct and which wasn't.

![Analysis](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/analysis.png)


#### Responsive design

The web application being responsive can majorly work on all the devices. The power of 'Bootstrap' is rightly harnessed.

![Responsive](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/responsive2.png)

![Responsive](https://raw.githubusercontent.com/deeshashah/Studeely/master/screenshots/responsive1.png)
