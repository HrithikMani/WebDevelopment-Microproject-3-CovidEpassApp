# Covid Epass Generation App
The app would generate Epass for people who want to commute from one place to another. Using theis app people can generate a pass. They can show this pass while traveling during this pandemic.

# # Technology Stack
1) Angular
2) Flask
3) MongoDb

# # Deployment Steps
1) Create a Flask Environment in root folder 
2) Install packages namely : flask, image, flask_cors, pymongo, image, qrcode,dotenv, twilio(optional).
3) MongoDb: Create a data base named "epasssystem"
4) navigate to frontend folder, and install all node packages using "npm i"
5) If your using twilio. To setup twilio uncomment Line number(24,25,27,80,81) in app.py. Replace sid, auth with respect to your account. Replace "to" the phone number on line 80.
6) Start the backend server in root folder "flask run"
7) Start the angular server in frontend folder "ng serve"

