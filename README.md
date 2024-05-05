# C7430-group3-tracker
Industrial Training project for C7430 course at Aalto University - group 3. A simple tracking service to view location of a mobile phone.

This web service utilizes Flask, a lightweight web application framework in Python, to create an application that displays the map location of a mobile device using OpenStreetMap.

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

4. **Access the Application**: Open your web browser and go to `http://localhost:8000` to view the application.

5. **Update Location Manually**: Once the web service is running, update your location and see how the application responds.
	```bash
	curl -d "X=60.18476992596687&Y=24.82209498028948" -X POST http://localhost:8000/data
	```
	Use this cURL command in the CMD to move the marker around (set your own X and Y values).

## License

This project is licensed under the [MIT License](LICENSE.md).
