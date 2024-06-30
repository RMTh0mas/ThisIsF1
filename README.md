# This is F1 :racing_car:

#### Video Demo: [Watch on YouTube](https://youtu.be/_XlxGHhDuVw)

## Description
This project is a web application dedicated to showcasing Formula 1 information. It utilizes an external API, the Rapid API, to retrieve and display data about Formula 1 races, drivers, and circuits. The application is built using Python with the Flask framework, integrating HTML, CSS, and JavaScript for dynamic and responsive web pages.

### Features
- **Home Page**: Introduces users to Formula 1 with interactive slides powered by Swiper. It covers basic information about Formula 1, including details about cars, teams like Ferrari and McLaren, and insights into different circuits.
  
- **Drivers Page**: Displays current season driver standings and allows users to filter results by previous seasons up to 2012. Data is fetched from the Rapid API, with user-selected season data stored using localStorage for persistence.
  
- **Circuits Page**: Showcases circuits from the current Formula 1 season with details such as circuit format, location, and dates. The image carousel provides a visual selection similar to a racing game's track menu.

### Technologies Used
- **Python and Flask**: Backend framework for routing and API integration.
- **HTML, CSS, JavaScript**: Frontend development for structure, style, and interactivity.
- **Rapid API**: External data source for real-time Formula 1 information.
- **Bootstrap**: Used for responsive design components like the navbar and select button.

### Implementation Details
- **App.py**: Manages routes for home, circuits, and drivers, fetching and processing data from the Rapid API. Handles rendering of HTML templates and integrates necessary libraries for HTTP requests.
  
- **Layout.html and Layout.css**: Provides a consistent layout across pages, using Bootstrap for the navbar and custom CSS styles for visual elements and fonts like "Anta" from Google Fonts.
  
- **Home.html and Home.css**: Implements Swiper for interactive slides on the home page, with a looping video background to enhance visual appeal. Responsive design ensures compatibility across different devices.
  
- **Drivers.html and Drivers.css**: Allows filtering of driver standings by season, leveraging Bootstrap select buttons and localStorage to maintain user preferences across sessions.
  
- **Circuits.html and Circuits.css**: Displays circuit information using Swiper for image carousels, enhancing user experience with detailed insights into each circuit's characteristics.

### Screenshots
![Home Page](https://github.com/RMTh0mas/ThisIsF1/assets/72501636/1f9cb614-5bd6-40ce-91a4-7597f76318cc)
![Drivers Page](https://github.com/RMTh0mas/ThisIsF1/assets/72501636/9b84be82-778b-4f5d-a1de-3613f8ee83e8)
![Circuits Page](https://github.com/RMTh0mas/ThisIsF1/assets/72501636/ac6cc808-befb-4e32-babf-45cb7940b02e)

### Acknowledgments
- **Swiper**: JavaScript library for creating carousels and slides. https://swiperjs.com/
- **Bootstrap**: Frontend framework for responsive and mobile-first design. https://getbootstrap.com/docs/5.2/components/navbar/
- **Rapid API**: Provides real-time data for Formula 1 races, drivers, and circuits. https://rapidapi.com/api-sports/api/api-formula-1
