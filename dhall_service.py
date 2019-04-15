#!/usr/bin/python3.6
# Description:
    # This is the main script which receives, handles, and delivers texts
    # This class is also used to deal with providing menus

from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import dhall_hours_query
import dhall_item_query
import fileinput, sys
import time

app = Flask(__name__)
class DhallService:

	def __init__(self):
	# Initializing menu data
		self.initialize_data()
	# Intializing item query
		self.item_query = dhall_item_query.ItemQuery()
	# Intializing hours query
		self.hours_query = dhall_hours_query.HoursQuery()


	def initialize_data(self):
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

	def fetch_menu(self, file_name, breakfast_list, lunch_list, dinner_list):
	# Create list of all food items
	    breakfast = False
	    lunch = False
	    dinner = False
	    with open(file_name,"r") as file:
		    for line in file:
		        if "--Breakfast--" in line:
		            breakfast = True
		            lunch = False
		            dinner = False
		        if "--Lunch--" in line:
		            breakfast = False
		            lunch = True
		            dinner = False
		        if "--Dinner--" in line:
		            breakfast = False
		            lunch = False
		            dinner = True
		  # line[:-1] gets rid of newline character
		        if breakfast:
		            breakfast_list.append(line[:-1])
		        if lunch:
		            lunch_list.append(line[:-1])
		        if dinner:
		            dinner_list.append(line[:-1])


	def send_menu(self, college, course):
	    if college == "cowell":
	        if not self.dhall_cowell_breakfast:
	            if not self.dhall_cowell_lunch:
	                if not self.dhall_cowell_dinner:
	                    return "This dining hall is closed today"
	    if college == "crown":
	        if not self.dhall_crown_breakfast:
	            if not self.dhall_crown_lunch:
	                if not self.dhall_crown_dinner:
	                    return "This dining hall is closed today"
	    if college == "porter":
	        if not self.dhall_porter_breakfast:
	            if not self.dhall_porter_lunch:
	                if not self.dhall_porter_dinner:
	                    return "This dining hall is closed today"
	    if college == "rachel":
	        if not self.dhall_rachel_breakfast:
	            if not self.dhall_rachel_lunch:
	                if not self.dhall_rachel_dinner:
	                    return "This dining hall is closed today"
	    if college == "nine":
	        if not self.dhall_nine_breakfast:
	            if not self.dhall_nine_lunch:
	                if not self.dhall_nine_dinner:
	                    return "This dining hall is closed today"


	# Checking for just certain meals that are not being served
	    if course == "breakfast":
	    	if college == "cowell":
			    if self.dhall_cowell_breakfast:
				    return "\n".join(self.dhall_cowell_breakfast)
			    else:
				    return "This dining hall is not serving breakfast"
	    	elif college == "crown":
			    if self.dhall_crown_breakfast:
				    return "\n".join(self.dhall_crown_breakfast)
			    else:
				    return "This dining hall is not serving breakfast"
	    	elif college == "porter":
	    		if self.dhall_porter_breakfast:
				    return "\n".join(self.dhall_porter_breakfast)
	    		else:
				    return "This dining hall is not serving breakfast"
	    	elif college == "rachel":
	    		if self.dhall_rachel_breakfast:
				    return "\n".join(self.dhall_rachel_breakfast)
	    		else:
				    return "This dining hall is not serving breakfast"
	    	elif college == "nine":
	    		if self.dhall_nine_breakfast:
				    return "\n".join(self.dhall_nine_breakfast)
	    		else:
				    return "This dining hall is not serving breakfast"

	    elif course == "lunch":
	    	if college == "cowell":
	    		if self.dhall_cowell_lunch:
				    return "\n".join(self.dhall_cowell_lunch)
	    		else:
				    return "This dining hall is not serving lunch"
	    	elif college == "crown":
	    		if self.dhall_crown_lunch:
				    return "\n".join(self.dhall_crown_lunch)
	    		else:
				    return "This dining hall is not serving lunch"
	    	elif college == "porter":
	    		if self.dhall_porter_lunch:
				    return "\n".join(self.dhall_porter_lunch)
	    		else:
				    return "This dining hall is not serving lunch"
	    	elif college == "rachel":
			    if self.dhall_rachel_lunch:
				    return "\n".join(self.dhall_rachel_lunch)
			    else:
				    return "This dining hall is not serving lunch"
	    	elif college == "nine":
	    		if self.dhall_nine_lunch:
				    return "\n".join(self.dhall_nine_lunch)
	    		else:
				    return "This dining hall is not serving lunch"

	    elif course == "dinner":
	    	if college == "cowell":
	    		if self.dhall_cowell_dinner:
				    return "\n".join(self.dhall_cowell_dinner)
	    		else:
				    return "This dining hall is not serving dinner"
	    	elif college == "crown":
	    		if self.dhall_crown_dinner:
				    return "\n".join(self.dhall_crown_dinner)
	    		else:
				    return "This dining hall is not serving dinner"
	    	elif college == "porter":
	    		if self.dhall_porter_dinner:
				    return "\n".join(self.dhall_porter_dinner)
	    		else:
				    return "This dining hall is not serving dinner"
	    	elif college == "rachel":
	    		if self.dhall_rachel_dinner:
				    return "\n".join(self.dhall_rachel_dinner)
	    		else:
				    return "This dining hall is not serving dinner"
	    	elif college == "nine":
	    		if self.dhall_nine_dinner:
				    return "\n".join(self.dhall_nine_dinner)
	    		else:
				    return "This dining hall is not serving dinner"


	def check_new_user(self, number):
	    self.user_exists = False
	# Warning still sends them text saying they are done
	    self.user_limit_reached_warning = False
	# Final just doesnt send back any data
	    self.user_limit_reached_final = False
	# If returning user
	    for line in fileinput.input("user_phone_numbers.txt", inplace=1):
	        if number in line:
	            self.user_exists = True
	            count = int(line[-3:].strip())
	            line = line.replace("| "+str(count),"| "+str(count+1))
	            if count == 20:
	                   self.reply_text = "--Warning--\nThere is a 25 text limit per day, you have 5 texts remaining.\n\n"
	            if count == 25:
	                   self.reply_text = "--Notice--\nYour daily text limit of 25 has been reached, you can continue using the service tomorrow\n\n"
	                   self.user_limit_reached_warning = True
	            if count > 25:
	                self.user_limit_reached_final = True
	        sys.stdout.write(line)
	# If new user
	    if not self.user_exists:
    	     with open("user_phone_numbers.txt","a") as file:
    	           file.write(number+" | 1\n")
    	     self.reply_text = "Welcome to the Dining Hall Texting Service.\n\nTo check whats on the menu for any given dining hall, text the name of the dining hall and which meal you're curious about.\nExample: 'cowell breakfast'\n\nTo check what the current day's hours are, text the name of the dining hall and 'hours'.\nExample: 'porter hours'\n\nYou can also type any food item and we will provide you a list of dining halls currently serving that item\nExample: 'nachos'\nNote: If you do not know the exact name of an item, generic searches work best.\n\nType 'options' if you ever forget how to use the service\n\nTo unsubscribe, type 'stop'\nTo resubscribe, type 'start'\n\nDisclaimer: Only food items that are currently on the official dining hall website will display in a search. Items that all dining halls serve such as ice cream, bread, or fruits won't show up in a search.\n\nMenu's are updated every half hour\n\nThanks for using the Dining Hall Texting Service :)"


	def execute(self, app):
	    #self.app = app
		#self.app = Flask(__name__)
		@app.route('/sms', methods=['POST'])
		def sms():
			number = request.form['From']
			message_body = request.form['Body']
		# Whitelist
			whitelist_status = False
			with open("whitelist.txt","r") as file:
			    for line in file:
			        if number in line:
			            whitelist_status = True
			if not whitelist_status:
			    return ""
		# Removing period from end of text
			message_body_array = message_body.strip().lower().split(" ")
			if message_body_array[-1][-1] == ".":
			    message_body_array[-1] = message_body_array[-1][:-1]
			if message_body[-1] == ".":
			    message_body = message_body[:-1]

			self.reply_text = ""
			response = MessagingResponse()
			self.check_new_user(number)
			if not self.user_exists:
			    response.message(self.reply_text)
			    return str(response)
			if self.user_limit_reached_final:
			    return ""


        # For dining hall strikes
# 			self.reply_text = self.reply_text + "Limited meal options being served until strikes are over.\nDining halls scheduled to stay open (8pm closing time):\nCowell/Stevenson\nNine/Ten\nRachel Carson/Oakes.\n\nNormal texting services should resume Friday."
# 			response.message(self.reply_text)
# 			return str(response)

			self.initialize_data()

		# Return the menu for a specific college
			if "breakfast" in message_body_array:
				if "cowell" in message_body_array or "stevenson" in message_body_array or "cowel" in message_body_array or "cowell/stevenson" in message_body_array or "cowel/stevenson" in message_body_array:
					self.fetch_menu("cowell_menu.txt", self.dhall_cowell_breakfast, self.dhall_cowell_lunch, self.dhall_cowell_dinner)
					self.reply_text = self.reply_text + self.send_menu("cowell", "breakfast")
					response.message(self.reply_text)
					return str(response)
				elif "crown" in message_body_array or "merril" in message_body_array or "merrill" in message_body_array or "crown/merril" in message_body_array or "crown/merrill" in message_body_array:
					self.fetch_menu("crown_menu.txt", self.dhall_crown_breakfast, self.dhall_crown_lunch, self.dhall_crown_dinner)
					self.reply_text = self.reply_text + self.send_menu("crown", "breakfast")
					response.message(self.reply_text)
					return str(response)
				elif "porter" in message_body_array or "kresge" in message_body_array or "porter/kresge" in message_body_array:
					self.fetch_menu("porter_menu.txt", self.dhall_porter_breakfast, self.dhall_porter_lunch, self.dhall_porter_dinner)
					self.reply_text = self.reply_text + self.send_menu("porter", "breakfast")
					response.message(self.reply_text)
					return str(response)
				elif "rachel" in message_body_array or "rcc" in message_body_array or "oakes" in message_body_array or "eight" in message_body_array or "8" in message_body_array or "carson" in message_body_array or "oaks" in message_body_array or "rachel-carson" in message_body_array:
					self.fetch_menu("rachel_menu.txt", self.dhall_rachel_breakfast, self.dhall_rachel_lunch, self.dhall_rachel_dinner)
					self.reply_text = self.reply_text + self.send_menu("rachel", "breakfast")
					response.message(self.reply_text)
					return str(response)
				elif "nine" in message_body_array or "ten" in message_body_array or "9" in message_body_array or "10" in message_body_array or "c9" in message_body_array or "nine/ten" in message_body_array or "9/10" in message_body_array:
					self.fetch_menu("nine_menu.txt", self.dhall_nine_breakfast, self.dhall_nine_lunch, self.dhall_nine_dinner)
					self.reply_text = self.reply_text + self.send_menu("nine", "breakfast")
					response.message(self.reply_text)
					return str(response)
				else:
					self.reply_text = self.reply_text + "Please specify the college in the same text\nExample: 'cowell breakfast'"
					response.message(self.reply_text)
					return str(response)


			elif "lunch" in message_body_array:
				if "cowell" in message_body_array or "stevenson" in message_body_array or "cowel" in message_body_array or "cowell/stevenson" in message_body_array or "cowel/stevenson" in message_body_array:
					self.fetch_menu("cowell_menu.txt", self.dhall_cowell_breakfast, self.dhall_cowell_lunch, self.dhall_cowell_dinner)
					self.reply_text = self.reply_text + self.send_menu("cowell", "lunch")
					response.message(self.reply_text)
					return str(response)
				elif "crown" in message_body_array or "merril" in message_body_array or "merrill" in message_body_array or "crown/merril" in message_body_array or "crown/merrill" in message_body_array:
					self.fetch_menu("crown_menu.txt", self.dhall_crown_breakfast, self.dhall_crown_lunch, self.dhall_crown_dinner)
					self.reply_text = self.reply_text + self.send_menu("crown", "lunch")
					response.message(self.reply_text)
					return str(response)
				elif "porter" in message_body_array or "kresge" in message_body_array or "porter/kresge" in message_body_array:
					self.fetch_menu("porter_menu.txt", self.dhall_porter_breakfast, self.dhall_porter_lunch, self.dhall_porter_dinner)
					self.reply_text = self.reply_text + self.send_menu("porter", "lunch")
					response.message(self.reply_text)
					return str(response)
				elif "rachel" in message_body_array or "rcc" in message_body_array or "oakes" in message_body_array or "eight" in message_body_array or "8" in message_body_array or "carson" in message_body_array or "oaks" in message_body_array or "rachel-carson" in message_body_array:
					self.fetch_menu("rachel_menu.txt", self.dhall_rachel_breakfast, self.dhall_rachel_lunch, self.dhall_rachel_dinner)
					self.reply_text = self.reply_text + self.send_menu("rachel", "lunch")
					response.message(self.reply_text)
					return str(response)
				elif "nine" in message_body_array or "ten" in message_body_array or "9" in message_body_array or "10" in message_body_array or "c9" in message_body_array or "nine/ten" in message_body_array or "9/10" in message_body_array:
					self.fetch_menu("nine_menu.txt", self.dhall_nine_breakfast, self.dhall_nine_lunch, self.dhall_nine_dinner)
					self.reply_text = self.reply_text + self.send_menu("nine", "lunch")
					response.message(self.reply_text)
					return str(response)
				else:
					self.reply_text = self.reply_text + "Please specify the college in the same text\nExample: 'cowell lunch'"
					response.message(self.reply_text)
					return str(response)


			elif "dinner" in message_body_array or "late night" in message_body.lower() or "latenight" in message_body.lower() or "late-night" in message_body.lower():
				if "cowell" in message_body_array or "stevenson" in message_body_array or "cowel" in message_body_array or "cowell/stevenson" in message_body_array or "cowel/stevenson" in message_body_array:
					self.fetch_menu("cowell_menu.txt", self.dhall_cowell_breakfast, self.dhall_cowell_lunch, self.dhall_cowell_dinner)
					self.reply_text = self.reply_text + self.send_menu("cowell", "dinner")
					response.message(self.reply_text)
					return str(response)
				elif "crown" in message_body_array or "merril" in message_body_array or "merrill" in message_body_array or "crown/merril" in message_body_array or "crown/merrill" in message_body_array:
					self.fetch_menu("crown_menu.txt", self.dhall_crown_breakfast, self.dhall_crown_lunch, self.dhall_crown_dinner)
					self.reply_text = self.reply_text + self.send_menu("crown", "dinner")
					response.message(self.reply_text)
					return str(response)
				elif "porter" in message_body_array or "kresge" in message_body_array or "porter/kresge" in message_body_array:
					self.fetch_menu("porter_menu.txt", self.dhall_porter_breakfast, self.dhall_porter_lunch, self.dhall_porter_dinner)
					self.reply_text = self.reply_text + self.send_menu("porter", "dinner")
					response.message(self.reply_text)
					return str(response)
				elif "rachel" in message_body_array or "rcc" in message_body_array or "oakes" in message_body_array or "eight" in message_body_array or "8" in message_body_array or "carson" in message_body_array or "oaks" in message_body_array or "rachel-carson" in message_body_array:
					self.fetch_menu("rachel_menu.txt", self.dhall_rachel_breakfast, self.dhall_rachel_lunch, self.dhall_rachel_dinner)
					self.reply_text = self.reply_text + self.send_menu("rachel", "dinner")
					response.message(self.reply_text)
					return str(response)
				elif "nine" in message_body_array or "ten" in message_body_array or "9" in message_body_array or "10" in message_body_array or "c9" in message_body_array or "nine/ten" in message_body_array or "9/10" in message_body_array:
					self.fetch_menu("nine_menu.txt", self.dhall_nine_breakfast, self.dhall_nine_lunch, self.dhall_nine_dinner)
					self.reply_text = self.reply_text + self.send_menu("nine", "dinner")
					response.message(self.reply_text)
					return str(response)
				else:
					self.reply_text = self.reply_text + "Please specify the college in the same text\nExample: 'cowell dinner'"
					response.message(self.reply_text)
					return str(response)

        # Return the hours for a specific dining hall
			elif "hours" in message_body_array:
				if "cowell" in message_body_array or "stevenson" in message_body_array or "cowel" in message_body_array or "cowell/stevenson" in message_body_array or "cowel/stevenson" in message_body_array:
					self.reply_text = self.reply_text + self.hours_query.send_hours("cowell")
					response.message(self.reply_text)
					return str(response)
				elif "crown" in message_body_array or "merril" in message_body_array or "merrill" in message_body_array or "crown/merril" in message_body_array or "crown/merrill" in message_body_array:
					self.reply_text = self.reply_text + self.hours_query.send_hours("crown")
					response.message(self.reply_text)
					return str(response)
				elif "porter" in message_body_array or "kresge" in message_body_array or "porter/kresge" in message_body_array:
					self.reply_text = self.reply_text + self.hours_query.send_hours("porter")
					response.message(self.reply_text)
					return str(response)
				elif "rachel" in message_body_array or "rcc" in message_body_array or "oakes" in message_body_array or "eight" in message_body_array or "8" in message_body_array or "carson" in message_body_array or "oaks" in message_body_array or "rachel-carson" in message_body_array:
					self.reply_text = self.reply_text + self.hours_query.send_hours("rachel")
					response.message(self.reply_text)
					return str(response)
				elif "nine" in message_body_array or "ten" in message_body_array or "9" in message_body_array or "10" in message_body_array or "c9" in message_body_array or "nine/ten" in message_body_array or "9/10" in message_body_array:
					self.reply_text = self.reply_text + self.hours_query.send_hours("nine")
					response.message(self.reply_text)
					return str(response)
				else:
					self.reply_text = self.reply_text + "Please specify the college in the same text\nExample: 'stevenson hours'"
					response.message(self.reply_text)
					return str(response)


		# Incorrect usage menu
			elif "cowell" in message_body_array or "stevenson" in message_body_array or "crown" in message_body_array or "merrill" in message_body_array or "porter" in message_body_array or "kresge" in message_body_array or "rachel" in message_body_array or "oakes" in message_body_array or "carson" in message_body_array or "rcc" in message_body_array or "oaks" in message_body_array or "nine" in message_body_array or "ten" in message_body_array or "9" in message_body_array or "nine/ten" in message_body_array or "9/10" in message_body_array or "10" in message_body_array or "eight" in message_body_array or "8" in message_body_array:
			    self.reply_text = self.reply_text + "--Incorrect Usage--\nType 'options' to see full list of commands"
			    response.message(self.reply_text)
			    return str(response)

        # Options menu
			elif "options" in message_body.lower():
				self.reply_text = self.reply_text + "--Options--\n1. Type 'cowell hours' to get today's hours for cowell\n2. Type 'oakes lunch' to get the lunch menu at oakes\n3. Type 'nachos' to recieve a list of of dining halls serving nachos\n4. Type 'feedback' to receive a link to our google form where you can leave feedback\n\nDisclaimer: Only food items that are currently on the official dining hall website will display in a search. Items that all dining halls serve such as ice cream, bread, or fruits won't show up in a search.\n\nMenu's are updated every half hour\n\nHappy eating :)"
				response.message(self.reply_text)
				return str(response)

		# Feedback URL
			elif "feedback" in message_body.lower():
				self.reply_text = self.reply_text + "https://goo.gl/forms/oL6Y7AsFx11Iohvg1"
				response.message(self.reply_text)
				return str(response)


        # Easter Eggs, still need to learn how to do emojis
			elif "who are you" in message_body.lower() or "who is this" in message_body.lower():
				self.reply_text = self.reply_text + "My name's Zach. Hopefully this project makes life a little easier for you :D"
				response.message(self.reply_text)
				return str(response)

		# Return the locations where a specific food item is being served
			else:
			# Obtain current data for all dining halls
				self.fetch_menu("cowell_menu.txt", self.dhall_cowell_breakfast, self.dhall_cowell_lunch, self.dhall_cowell_dinner)
				self.fetch_menu("crown_menu.txt", self.dhall_crown_breakfast, self.dhall_crown_lunch, self.dhall_crown_dinner)
				self.fetch_menu("porter_menu.txt", self.dhall_porter_breakfast, self.dhall_porter_lunch, self.dhall_porter_dinner)
				self.fetch_menu("rachel_menu.txt", self.dhall_rachel_breakfast, self.dhall_rachel_lunch, self.dhall_rachel_dinner)
				self.fetch_menu("nine_menu.txt", self.dhall_nine_breakfast, self.dhall_nine_lunch, self.dhall_nine_dinner)
			# Message body is the item and the current_time is for only displaying the item at dhalls which are open and serving the item
				self.reply_text = self.reply_text + self.item_query.send_item_locations(message_body.lower(), self.dhall_cowell_breakfast, self.dhall_cowell_lunch, self.dhall_cowell_dinner,
																self.dhall_crown_breakfast, self.dhall_crown_lunch, self.dhall_crown_dinner,
																self.dhall_porter_breakfast, self.dhall_porter_lunch, self.dhall_porter_dinner,
																self.dhall_rachel_breakfast, self.dhall_rachel_lunch, self.dhall_rachel_dinner,
																self.dhall_nine_breakfast, self.dhall_nine_lunch, self.dhall_nine_dinner)
				response.message(self.reply_text)
				return str(response)


if __name__ == '__main__':
	service.app.run()

service = DhallService()
service.execute(app)
