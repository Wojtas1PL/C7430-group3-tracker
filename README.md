# C7430-group3-tracker
Industrial Training project for C7430 course at Aalto University - group 3. A simple tracking service to view location of a mobile phone.


To test this out, once the web service is running, use this cURL command in the CMD to move the marker around (set your own X and Y values):

curl -d "X=50&Y=-30" -X POST http://localhost:8000/data
