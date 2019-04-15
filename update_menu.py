#!/usr/bin/python3.6
# Description:
    # This script updates the text files on server with the current dining hall menus
    # This script runs at night at 12:15 am, and then at 5:15 am and every 5 hours after that until 3:15 pm

from bs4 import BeautifulSoup
import requests


class UpdateMenu:
    def __init__(self):

# Initializing lists
	# Cowell lists
        self.dhall_cowell_breakfast = []
        self.dhall_cowell_lunch = []
        self.dhall_cowell_dinner = []
	# Crown lists
        self.dhall_crown_breakfast = []
        self.dhall_crown_lunch = []
        self.dhall_crown_dinner = []
	# Porter lists
        self.dhall_porter_breakfast = []
        self.dhall_porter_lunch = []
        self.dhall_porter_dinner = []
	# Rachel lists
        self.dhall_rachel_breakfast = []
        self.dhall_rachel_lunch = []
        self.dhall_rachel_dinner = []
	# Nine and ten lists
        self.dhall_nine_breakfast = []
        self.dhall_nine_lunch = []
        self.dhall_nine_dinner = []

    def get_current_data(self, dhall_url, location_num, breakfast, lunch, dinner):
	# Create list of all food items
	    list = []
	    breakfast_index = 0
	    lunch_index = 0
	    dinner_index = 0
	    page = requests.get('http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum='+location_num+'&locationName='+dhall_url+'&sName=&naFlag=')
	    soup = BeautifulSoup(page.content, 'html.parser')
	    for tag in soup.findAll('div'):
	    	list.append(''.join(tag.findAll(text=True)))
	# Remove non-essential <div> information
	    list.pop(0)
	    list.pop(0)
	    list.pop()
	    list.pop()
	    while '\xa0' in list:
	    	list.remove('\xa0')
	#Find index of meals
	    i = 0
	    for item in list:
		    if item == 'Breakfast':
		    	breakfast_index = i # breakfast index
		    if item == 'Lunch':
		    	lunch_index = i # lunch index
		    if item == 'Dinner':
		    	dinner_index = i # dinner index
		    i += 1
	# Generating breakfast, lunch, and dinner lists
	    if lunch_index:
		    for i in range(breakfast_index + 1, lunch_index):
		    	breakfast.append(list[breakfast_index + 1])
		    	breakfast_index += 1
	    else:
	    	for i in range(breakfast_index + 1, len(list)):
	    		breakfast.append(list[breakfast_index + 1])
	    		breakfast_index += 1
	    	return
	    if dinner_index:
	        for i in range(lunch_index + 1, dinner_index):
	            lunch.append(list[lunch_index + 1])
	            lunch_index += 1
	    else:
	        for i in range(lunch_index + 1, len(list)):
    		    lunch.append(list[lunch_index + 1])
    		    lunch_index += 1
	        return
	    for i in range(dinner_index + 1, len(list)):
		    dinner.append(list[dinner_index + 1])
		    dinner_index += 1


    def remove_current_data(self):
    # Cowell
        with open("cowell_menu.txt","w") as file:
            file.write("")
    # Crown
        with open("crown_menu.txt","w") as file:
            file.write("")
    # Porter
        with open("porter_menu.txt","w") as file:
            file.write("")
    # Rachel
        with open("rachel_menu.txt","w") as file:
            file.write("")
    # Nine
        with open("nine_menu.txt","w") as file:
            file.write("")

    def store_current_data(self):
        self.remove_current_data()
    # Cowell
        with open("cowell_menu.txt","a") as file:
            if self.dhall_cowell_breakfast:
                file.write("--Breakfast--\n")
                for option in self.dhall_cowell_breakfast:
                    file.write(option+"\n")
            if self.dhall_cowell_lunch:
                file.write("--Lunch--\n")
                for option in self.dhall_cowell_lunch:
                    file.write(option+"\n")
            if self.dhall_cowell_dinner:
                file.write("--Dinner--\n")
                for option in self.dhall_cowell_dinner:
                    if option == "Late Night":
                        file.write("\n--" + option + "--\n")
                    else:
                        file.write(option+"\n")
    # Crown
        with open("crown_menu.txt","a") as file:
            if self.dhall_crown_breakfast:
                file.write("--Breakfast--\n")
                for option in self.dhall_crown_breakfast:
                    file.write(option+"\n")
            if self.dhall_crown_lunch:
                file.write("--Lunch--\n")
                for option in self.dhall_crown_lunch:
                    file.write(option+"\n")
            if self.dhall_crown_dinner:
                file.write("--Dinner--\n")
                for option in self.dhall_crown_dinner:
                    if option == "Late Night":
                        file.write("\n--" + option + "--\n")
                    else:
                        file.write(option+"\n")
    # Porter
        with open("porter_menu.txt","a") as file:
            if self.dhall_porter_breakfast:
                file.write("--Breakfast--\n")
                for option in self.dhall_porter_breakfast:
                    file.write(option+"\n")
            if self.dhall_porter_lunch:
                file.write("--Lunch--\n")
                for option in self.dhall_porter_lunch:
                    file.write(option+"\n")
            if self.dhall_porter_dinner:
                file.write("--Dinner--\n")
                for option in self.dhall_porter_dinner:
                    if option == "Late Night":
                        file.write("\n--" + option + "--\n")
                    else:
                        file.write(option+"\n")
    # Rachel
        with open("rachel_menu.txt","a") as file:
            if self.dhall_rachel_breakfast:
                file.write("--Breakfast--\n")
                for option in self.dhall_rachel_breakfast:
                    file.write(option+"\n")
            if self.dhall_rachel_lunch:
                file.write("--Lunch--\n")
                for option in self.dhall_rachel_lunch:
                    file.write(option+"\n")
            if self.dhall_rachel_dinner:
                file.write("--Dinner--\n")
                for option in self.dhall_rachel_dinner:
                    if option == "Late Night":
                        file.write("\n--" + option + "--\n")
                    else:
                        file.write(option+"\n")
    # Nine
        with open("nine_menu.txt","a") as file:
            if self.dhall_nine_breakfast:
                file.write("--Breakfast--\n")
                for option in self.dhall_nine_breakfast:
                    file.write(option+"\n")
            if self.dhall_nine_lunch:
                file.write("--Lunch--\n")
                for option in self.dhall_nine_lunch:
                    file.write(option+"\n")
            if self.dhall_nine_dinner:
                file.write("--Dinner--\n")
                for option in self.dhall_nine_dinner:
                    if option == "Late Night":
                        file.write("\n--" + option + "--\n")
                    else:
                        file.write(option+"\n")



    def execute(self):
    # Update all menu data
        self.get_current_data("Cowell+Stevenson+Dining+Hall", "05", self.dhall_cowell_breakfast, self.dhall_cowell_lunch, self.dhall_cowell_dinner)
        self.get_current_data("Crown+Merrill+Dining+Hall", "20", self.dhall_crown_breakfast, self.dhall_crown_lunch, self.dhall_crown_dinner)
        self.get_current_data("Porter+Kresge+Dining+Hall", "25", self.dhall_porter_breakfast, self.dhall_porter_lunch, self.dhall_porter_dinner)
        self.get_current_data("Rachel+Carson+Oakes+Dining+Hall", "30", self.dhall_rachel_breakfast, self.dhall_rachel_lunch, self.dhall_rachel_dinner)
        self.get_current_data("College+Nine+%26+Ten", "40", self.dhall_nine_breakfast, self.dhall_nine_lunch, self.dhall_nine_dinner)
    # Main dhall_service.py file uses 'fetch_data()' to get this information
        self.store_current_data()

if __name__ == "__main__":
    update = UpdateMenu()
    update.execute()















