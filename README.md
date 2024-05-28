# C7430-group3-tracker
Industrial Training project for C7430 course at Aalto University - group 3. A simple tracking service to view location of a mobile phone.

This Flask GPS Tracking System is a prototype designed to demonstrate real-time GPS tracking capabilities using Flask, Python, and OpenStreetMap. The system allows users to continuously monitor and update their GPS coordinates, which are then displayed on an interactive map interface.

## Features
- Real-time GPS tracking: Continuously tracks and updates the GPS coordinates of mobile devices.
- Interactive map interface: Displays device locations on an interactive map powered by OpenStreetMap.
- User-friendly interface: Provides a simple and intuitive interface for users to view and interact with device locations.

## Setup

To run this application locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.

	```bash
	git clone https://github.com/Wojtas1PL/C7430-group3-tracker.git
	```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip.

	```bash
	cd C7430-group3-tracker
	pip install flask
	```

3. **Run the Application**: Execute the Flask application.

	```bash
	python webservice/main.py
	```

## Usage
1. Run the Flask server:
   ```
   python main.py
   ```

2. Open a web browser and navigate to `http://localhost:8000` to access the web application.

3. Use the buttons on the interface to update your location, select preset locations, and toggle map layers.

## Configuration
- The Flask server is configured to run on port 8000 by default. You can change the port in the `main.py` file if needed.
- Ensure that your mobile device has location services enabled to allow the application to fetch GPS coordinates.


## License

This project is licensed under the [MIT License](LICENSE.md).
