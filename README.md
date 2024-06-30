# This is F1
#### Video Demo:  https://youtu.be/_XlxGHhDuVw
#### Description:
My project is a web application that displays information about Formula 1. The home screen displays basic information about Formula 1. The second page displays the drivers' current Formula 1 scores and allows the user to filter results from previous seasons. Finally, the third page displays data and images of the current season's tracks via an image carousel.
Most of the information displayed on the screen is consumed from an API, the Rapid API. I chose to consume an API rather than create a database from scratch, as I was always curious to develop a project that consumed information from an external API. Here's the API link: https://rapidapi.com/api-sports/api/api-formula-1
I chose to develop my project in Python using the Flask framework, with HTML, CSS and JavaScript, because as well as being introduced during the course, these are technologies that allow you to work with APIs quickly and efficiently. 

Explaining each file:

App.py: 

Displays information about Formula 1 circuits and drivers. It imports several libraries to manage HTTP requests. The main route ("/") only renders the home page (home.html). On the circuits route ("/circuits"), the script makes a GET request to the rapid api to get data on the 2024 season's races. The data is processed, including date formatting and circuit length calculations. The URLs of the circuit images and their respective backgrounds are replaced with the URLs stored in the circuit_images and circuit_backgrounds dictionaries.
There is also a route to display information about the drivers ("/drivers"). This route obtains the available seasons and driver rankings for a selected season by making requests to the Formula 1 API. The images of the teams and drivers are associated with the returned data using the teams_images and drivers_images dictionaries.
The auxiliary functions get_seasons and get_driver_rankings are used to obtain the available seasons and driver rankings, respectively. Both make requests to the Formula 1 API and manipulate the data returned.

Layout.html and layout.css: 

As with the CS50 activities, I tried to mirror the concept of using an html file as the base layout for the other html files. Mainly because of the navbar that repeats for all the files. In this way, I was able to avoid unnecessary repetition of code. I used a navbar template straight from bootstrap (https://getbootstrap.com/docs/5.2/components/navbar/). 
In the layout.css file there are some basic built-in CSS styles that are repeated for the other pages, such as the "Anta" font that was acquired from Google fonts (Link https://fonts.google.com/specimen/Anta?query=anta). These styles define the appearance of the various elements, such as the body, the color and other properties of the nav buttons.

home.html and home.css: 

The home page shows basic information about Formula 1 which is displayed via a Swiper Slide. My idea has always been for this home page to display introductory information about Formula 1, even if the user doesn't know the sport. I searched the internet for inspiration on how I could display this information and came across Swiper Slide, a popular JavaScript library used to create carousels and interactive slides on web pages. By accessing the swiper documentation (https://swiperjs.com/), I was able to figure out how to implement swiper in my project. 
The first slider shows what Formula 1 is. The second slider shows some information about the cars. The next slider shows the teams, such as Ferrari, McLaren and Mercedes. And the fourth slider shows some information about the circuits.

However, even after implementing the swipper, there was still something that bothered me, which was the background of the page. Because the content displayed wasn't very big, there was a lot of space left on the page. To fill this void, I had the idea of including a looping video in the background of the page, but I didn't know how to implement this type of background either, so I asked ChatGPT if there was an HTML tag that allowed videos to be inserted, and he showed me the video tag. Thanks to this, I was able to implement the looping video in the background of my page. In my case, I had to download the video in order to display it in the background of my project.
In the home.css file there are some basic built-in CSS styles that define the appearance and behavior of the page elements, especially in relation to the background video and the swiper slide. This file also defines responsive styles for different screen widths, ensuring that the interface is suitable for mobile devices and tablets.

Drivers.html and drivers.css:

The second page shows the current drivers' standings for the current season, however, it is also possible to filter by results from previous seasons, up to two thousand twelve. 

The season information was extracted from the rapid api. When I analyzed the api, I realized that they allow you to filter the data for the formula 1 seasons up to 2012, so I had the idea of enabling this filtering on screen, so that when a user selected the year, the information pertinent to that season would be displayed. That's why I included a Bootstrap select button that iterates over the list of seasons from app.py.
Within the main block of drivers.html, there are also JavaScript scripts to handle the selection of the season and save the selected value in localStorage, as this ensures that the value of the season selected by the user continues to be displayed after the page reloads.
In the drivers.css file there are some built-in CSS styles for the page, which define the appearance of the various elements, such as the main container, the driver cards and the titles. This file also defines responsive styles for different screen widths, ensuring that the interface is suitable for mobile devices and tablets.

Circuits.html and circuits.css: 

The circuits.html file shows the circuits of the current Formula 1 season and some information about them, such as the name of the circuit, the format of the circuit, the location of the circuit and the date of the circuit. For this screen, my idea is for the image carousel to work like a track selection menu in a racing game, where the player can see the track format and an image of the actual track. rapid's api doesn't provide good quality images, so I had to search for the link independently. The solution I found to relate the api data to the images was to save the image link in a dictionary and then save it in the json response returned by the api.

Circuits.css defines the style of the page, including the appearance and behavior of various elements, such as the body, each of Swiper's sliders and specific elements. This file also defines responsive styles for different screen widths, ensuring that the interface is suitable for mobile devices and tablets.