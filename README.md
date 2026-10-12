# Lil_Guy

## Project Overview
Lil_Guy is an interactive digital companion inspired by virtual pet applications such as Pou. The project combines a physical creature with a web application, allowing users to interact with their companion in the real world and monitor its mood online.

The physical creature will be housed in a small plastic enclosure and use an OLED display to show facial expressions. Touch, light and motion sensors will influence its behaviour, while a buzzer and LEDs will provide additional feedback. A cloud-connected web application will allow users to view their creature's status and access selected customisation features.

The project is being developed as an IOT CA.

## Project Objectives
- Develop an interactive physical companion using a Raspberry Pi 5 and electronic components.
- Implement a simple personality and mood system that responds to sensor input and user interactions.
- Establish secure communication between the physical device and a cloud-hosted web application using MQTT.
- Develop a web application that allows users to view their creature's current mood and interaction history.
- Store relevant device and user information in a database.
- Deploy the web application on AWS using a custom domain and HTTPS.
- Apply appropriate security measures to protect user accounts, device communication and stored data.

## Planned Features
### Physical Creature
- Display facial expressions and moods using an OLED screen.
- React differently to short touches and longer interactions.
- Become sleepy depending on light conditions.
- Wake up when motion is detected.
- Use simple buzzer sounds and LEDs to communicate its mood.
- Display the current time?, subject to the final implementation.

### Web Application
- Display the creature's current mood and device status.
- Show basic information and a history of interactions.
- Allow limited customisation, such as changing its name or selecting from predefined options.
- Provide a foundation for sleep and wake reminders, depending on the development time.

### Planned Extensions
Additional features may include scheduled sleep and wake behaviours, morning wake-up animations, evening yawns and browser notifications. These will be considered after the main hardware, application and communication requirements are working.

## Technologies Used
- Python: Device behaviour, sensor handling and backend development.
- FastAPI: Web application and backend API.
- SQLAlchemy: Database access and object-relational mapping.
- SQLite: Initial database implementation.
- HTML, CSS and Jinja2: Web interface and server-rendered pages.
- CSS framework: To be selected //TODO
- MQTT: Publish-subscribe messaging between the physical device and cloud application.
- AWS: Cloud hosting.
- Nginx and HTTPS/TLS: Web server configuration and secure browser communication.

Tech choices may change.

## Hardware Components
The planned physical prototype includes:

- Raspberry Pi 5 (2 GB) and starter kit.
- OLED display for facial expressions.
- Capacitive touch sensor.
- Photo-transistor light sensor.
- PIR motion sensor.
- Piezo buzzer.
- LEDs and suitable resistors.
- Breadboard and jumper wires.
- Plastic enclosure for the creature.

## System Architecture
The system will have two main parts: the physical creature and the cloud application.

The Raspberry Pi will manage the sensors, mood logic, display, buzzer and LEDs locally. It will communicate with the backend through an MQTT publish-subscribe broker. The backend will store relevant information in a database and provide a secure web interface through which users can view their creature and send supported commands.

//TODO
Add in architecture here

## Security
Security will be considered throughout development. Planned measures include authenticated access to protected web application endpoints, securely hashed passwords, encrypted HTTPS and MQTT communications, restricted database access, and secure storage of credentials. The cloud server and MQTT broker will be configured to avoid unauthorised access.

## Project Status
Current stage: Initial planning and repository setup.

## Documentation
Detailed documentation will be maintained in the docs/ directory, including architecture, hardware wiring, security decisions and test results.