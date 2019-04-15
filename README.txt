Dining Hall Texting Service
-----------------------------
Date Created - August, 2018
Author - Zachary Lamb

Background:
	This project began August, 2018 and lasted through December, 2018.
	A number of factors led me to end this project but the experience 
	provided me with many useful lessons that I will hopefully be able
	to apply to future buisness ventures.

Overview:
	This program allows users to send a text to a specified phone number controlled by 'Twilio', which
	redirects the data to a flask application contained in 'dhall_service.py' (this being hosted by 
	PythonAnywhere.com). 'dhall_service.py' then parses the user's request and gathers the necessary information
	to send a response. The response text is handled using Twilio's API within dhall_service.py.

Dhall_service.py 
	This is the main file containing the 'flask' application. It is in charge of receiving the SMS data, gathering
	the request meal information, and sending back a text through Twilio's API.

Dhall_item_query.py
	This script fetches meal data requested by dhall_service.py. It is simply in charge of accessing the correct 
	dining hall text files to gather the correct information to send back to the user.

Dhall_hours_query.py
	This script fetches dining hall hour data that is hard coded into the program. It then gives the requested
	data back to dhall_service.py to send to the user.

Update_menu.py
	This script accesses UCSC's dining hall pages and scrapes them for relevant menu data. This data is then stored
	in each dining halls respective text files. This script is run multiple times throughout the day by scheduled
	tasks on PythonAnywhere.

Check_menu_data.py
	This script makes sure the menu data is up to date. It is called multiple times throughout the day by a scheduled 
	tasks manager in PythonAnywhere.

Reset_user_counts.py
	There is a limit for each user on how many texts they can send per day. If a user gets to a point of being 5 texts
	away from the max, they receive a warning. If a user reaches the max, they receive a message telling them
	they cannot text again until tomorrow. This script will reset the count at 12am every day.
