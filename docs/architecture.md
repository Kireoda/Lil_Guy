# System Architecture

## Architecture Overview

Lil_Guy has two main parts: the physical creature and the web application hosted on AWS. The Raspberry Pi 5 controls the creature's behaviour and communicates with the backend through an MQTT broker. The backend handles device events, stores information in a database and allows users to interact with Lil_Guy through the website.

## Architecture Diagram

## Data Flow

### Device to Web Application

1. The touch sensor detects whether Lil_Guy is being poked or petted, while the light and PIR sensors detect changes in light levels and movement.
2. The Raspberry Pi processes these inputs and updates Lil_Guy's mood. For example, a short poke could make him annoyed, a longer touch could make him happy, and darkness could make him sleepy.
3. The Raspberry Pi updates the OLED display to show the new expression and activates the buzzer or LEDs if needed.
4. The device publishes an MQTT message containing details such as the interaction type, current mood and timestamp.
5. The FastAPI backend receives the message through its MQTT subscription and saves the relevant mood and interaction information to the database.
6. The website retrieves the latest stored information to show Lil_Guy's reported mood and recent interactions.

### Web Application to Device

1. The user can use the dashboard to rename Lil_Guy, change his personality type or set his preferred sleep and wake times. They can also view his current mood and recent interactions.
2. FastAPI checks that the user is logged in and validates any changes they request.
3. The backend saves settings, such as Lil_Guy's name, personality and sleep routine, to the database. If a change affects the creature's behaviour, the backend also publishes the updated setting or command to the relevant MQTT topic.
4. The Raspberry Pi receives the message through its MQTT subscription, checks that it is valid and applies the change to Lil_Guy's behaviour or display.

## Communication and Security

- **Browser to web server:** The website will use HTTPS to encrypt communication between the user's browser and the server. Users must log in to access protected features.

- **Raspberry Pi to MQTT broker:** The Raspberry Pi will use MQTT over TLS to send events and receive commands securely. Authentication and topic permissions will control which messages the device is allowed to send and receive.

- **Backend to database:** FastAPI will use SQLAlchemy to store and retrieve user details, creature settings and interaction history. Database access will be restricted so it cannot be accessed directly from the public internet.

- **Backend to MQTT broker:** FastAPI will subscribe to messages from the creature and publish commands or updated settings to the relevant MQTT topics. The connection will use authentication and TLS.

Credentials, passwords and other sensitive information will be kept out of the GitHub repository and stored using appropriate security measures.

## Design Decisions

- **Local processing:** The Raspberry Pi will handle Lil_Guy's basic reactions itself, so he can still respond to sensors if the internet disconnects.

- **MQTT publish-subscribe:** MQTT will allow the Raspberry Pi and backend to exchange messages without needing to communicate directly with each other.

- **FastAPI backend:** FastAPI will handle the website, user authentication, database operations and communication with the creature.

- **Cloud hosting:** The website will be hosted on AWS and accessed through a custom domain using HTTPS, as required by the CA.

- **Limited initial scope:** I'll focus on getting the sensors, mood system, OLED display, MQTT communication and secure website working first. Extra features, such as notifications and more customisation options, will depend on how much time is left.

## Outstanding Decisions

The following details still need to be decided during development:

- Which MQTT broker to use and where it will be hosted.
- How the database will be configured and kept persistent on AWS.
- Which MQTT topics and message formats will be used for events and commands.
- How the device will handle missed events or commands after an internet disconnection.
- The final hardware wiring and whether any additional components are needed.