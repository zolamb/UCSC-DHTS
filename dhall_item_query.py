#!/usr/bin/python3.6
# Description:
    # This script checks for dining halls serving specific food items
    # This class is used in another file to keep the flow clean in the 'dhall_service.py' file

import datetime, pytz

class ItemQuery:
	def __init__(self):
	# Initialize all dining halls hours (This should be somewhat constant throughout the year so I'm not going to slow down
	# the program by using another request.get())
	    current_time = datetime.datetime.now(pytz.timezone("US/Pacific"))
# Cowell schedule:
	# Breakfast:
	    self.cowell_breakfast_time_monday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.cowell_breakfast_time_tuesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.cowell_breakfast_time_wednesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.cowell_breakfast_time_thursday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.cowell_breakfast_time_friday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.cowell_breakfast_time_saturday = current_time.replace(hour=7, minute=0, second=0, microsecond=0)
	    self.cowell_breakfast_time_sunday = current_time.replace(hour=7, minute=0, second=0, microsecond=0)
	# Lunch:
	    self.cowell_lunch_time_monday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.cowell_lunch_time_tuesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.cowell_lunch_time_wednesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.cowell_lunch_time_thursday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.cowell_lunch_time_friday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.cowell_lunch_time_saturday = current_time.replace(hour=10, minute=0, second=0, microsecond=0)
	    self.cowell_lunch_time_sunday = current_time.replace(hour=10, minute=0, second=0, microsecond=0)
	# Dinner:
	    self.cowell_dinner_time_monday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.cowell_dinner_time_tuesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.cowell_dinner_time_wednesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.cowell_dinner_time_thursday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.cowell_dinner_time_friday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.cowell_dinner_time_saturday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.cowell_dinner_time_sunday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	# Closing
	    self.cowell_closing_time_monday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.cowell_closing_time_tuesday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.cowell_closing_time_wednesday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.cowell_closing_time_thursday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.cowell_closing_time_friday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	    self.cowell_closing_time_saturday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	    self.cowell_closing_time_sunday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)


# Crown schedule:
	# Breakfast:
	    self.crown_breakfast_time_monday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.crown_breakfast_time_tuesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.crown_breakfast_time_wednesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.crown_breakfast_time_thursday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.crown_breakfast_time_friday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    # Closed weekends
	    self.crown_breakfast_time_saturday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	    self.crown_breakfast_time_sunday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	# Lunch:
	    self.crown_lunch_time_monday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.crown_lunch_time_tuesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.crown_lunch_time_wednesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.crown_lunch_time_thursday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.crown_lunch_time_friday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
		# Closed weekends
	    self.crown_lunch_time_saturday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	    self.crown_lunch_time_sunday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	# Dinner:
	    self.crown_dinner_time_monday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.crown_dinner_time_tuesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.crown_dinner_time_wednesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.crown_dinner_time_thursday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.crown_dinner_time_friday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
		# Closed weekends
	    self.crown_dinner_time_saturday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	    self.crown_dinner_time_sunday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	# Closing
	    self.crown_closing_time_monday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	    self.crown_closing_time_tuesday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	    self.crown_closing_time_wednesday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	    self.crown_closing_time_thursday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	    self.crown_closing_time_friday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
		# Closed weekends
	    self.crown_closing_time_saturday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	    self.crown_closing_time_sunday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)


	# Porter schedule:
	# Breakfast:
	    self.porter_breakfast_time_monday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.porter_breakfast_time_tuesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.porter_breakfast_time_wednesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.porter_breakfast_time_thursday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.porter_breakfast_time_friday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
		# Closed weekends
	    self.porter_breakfast_time_saturday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	    self.porter_breakfast_time_sunday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	# Lunch:
	    self.porter_lunch_time_monday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.porter_lunch_time_tuesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.porter_lunch_time_wednesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.porter_lunch_time_thursday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.porter_lunch_time_friday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
		# Closed weekends
	    self.porter_lunch_time_saturday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	    self.porter_lunch_time_sunday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	# Dinner:
	    self.porter_dinner_time_monday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.porter_dinner_time_tuesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.porter_dinner_time_wednesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.porter_dinner_time_thursday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.porter_dinner_time_friday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
		# Closed weekends
	    self.porter_dinner_time_saturday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	    self.porter_dinner_time_sunday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	# Closing
	    self.porter_closing_time_monday = current_time.replace(hour=19, minute=0, second=0, microsecond=0)
	    self.porter_closing_time_tuesday = current_time.replace(hour=19, minute=0, second=0, microsecond=0)
	    self.porter_closing_time_wednesday = current_time.replace(hour=19, minute=0, second=0, microsecond=0)
	    self.porter_closing_time_thursday = current_time.replace(hour=19, minute=0, second=0, microsecond=0)
	    self.porter_closing_time_friday = current_time.replace(hour=19, minute=0, second=0, microsecond=0)
		# Closed weekends
	    self.porter_closing_time_saturday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
	    self.porter_closing_time_sunday = current_time.replace(hour=0, minute=0, second=0, microsecond=0)


	# Rachel schedule:
	# Breakfast:
	    self.rachel_breakfast_time_monday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.rachel_breakfast_time_tuesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.rachel_breakfast_time_wednesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.rachel_breakfast_time_thursday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.rachel_breakfast_time_friday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.rachel_breakfast_time_saturday = current_time.replace(hour=7, minute=0, second=0, microsecond=0)
	    self.rachel_breakfast_time_sunday = current_time.replace(hour=7, minute=0, second=0, microsecond=0)
	# Lunch:
	    self.rachel_lunch_time_monday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.rachel_lunch_time_tuesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.rachel_lunch_time_wednesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.rachel_lunch_time_thursday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.rachel_lunch_time_friday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.rachel_lunch_time_saturday = current_time.replace(hour=10, minute=0, second=0, microsecond=0)
	    self.rachel_lunch_time_sunday = current_time.replace(hour=10, minute=0, second=0, microsecond=0)
	# Dinner:
	    self.rachel_dinner_time_monday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.rachel_dinner_time_tuesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.rachel_dinner_time_wednesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.rachel_dinner_time_thursday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.rachel_dinner_time_friday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.rachel_dinner_time_saturday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.rachel_dinner_time_sunday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	# Closing
	    self.rachel_closing_time_monday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.rachel_closing_time_tuesday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.rachel_closing_time_wednesday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.rachel_closing_time_thursday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.rachel_closing_time_friday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	    self.rachel_closing_time_saturday = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	    self.rachel_closing_time_sunday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)


	# Nine schedule:
	# Breakfast:
	    self.nine_breakfast_time_monday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.nine_breakfast_time_tuesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.nine_breakfast_time_wednesday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.nine_breakfast_time_thursday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.nine_breakfast_time_friday = current_time.replace(hour=6, minute=30, second=0, microsecond=0)
	    self.nine_breakfast_time_saturday = current_time.replace(hour=7, minute=0, second=0, microsecond=0)
	    self.nine_breakfast_time_sunday = current_time.replace(hour=7, minute=0, second=0, microsecond=0)
	# Lunch:
	    self.nine_lunch_time_monday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.nine_lunch_time_tuesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.nine_lunch_time_wednesday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.nine_lunch_time_thursday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.nine_lunch_time_friday = current_time.replace(hour=11, minute=30, second=0, microsecond=0)
	    self.nine_lunch_time_saturday = current_time.replace(hour=10, minute=0, second=0, microsecond=0)
	    self.nine_lunch_time_sunday = current_time.replace(hour=10, minute=0, second=0, microsecond=0)
	# Dinner:
	    self.nine_dinner_time_monday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.nine_dinner_time_tuesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.nine_dinner_time_wednesday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.nine_dinner_time_thursday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.nine_dinner_time_friday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.nine_dinner_time_saturday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	    self.nine_dinner_time_sunday = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
	# Closing
	    self.nine_closing_time_monday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.nine_closing_time_tuesday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.nine_closing_time_wednesday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.nine_closing_time_thursday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.nine_closing_time_friday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.nine_closing_time_saturday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
	    self.nine_closing_time_sunday = current_time.replace(hour=23, minute=0, second=0, microsecond=0)





	def check_list(self, list_, dhall):
		if "- "+dhall not in self.item_locations:
			for option in list_:
				if "--Breakfast--" not in option and "--Lunch--" not in option and "--Dinner--" not in option and "--Late Night--" not in option:
					if self.item in option.lower():
						try:# If key already exists, then dont use that food item again
							self.item_dict[option.lower()]
						except:
							self.item = option.lower()
							self.item_locations.append("- "+dhall)
							break

	def check_list_2(self, list_, dhall):
	    if "- "+dhall not in self.item_locations:
	        for option in list_:
	            if "--Breakfast--" not in option and "--Lunch--" not in option and "--Dinner--" not in option and "--Late Night--" not in option:
	                if any(x in option.lower() for x in self.item_array):
	                #for food in self.item_array:
	                    #for food2 in option.lower().split(" "):
	                       #if food2 == food:
	                    try:
	                        self.item_dict[option.lower()]
	                    except:
	                        self.item = option.lower()
	                        self.item_locations.append("- "+dhall)
	                        break

	def send_item_locations(self, item, dhall_cowell_breakfast, dhall_cowell_lunch, dhall_cowell_dinner,
							dhall_crown_breakfast, dhall_crown_lunch, dhall_crown_dinner,
							dhall_porter_breakfast, dhall_porter_lunch, dhall_porter_dinner,
							dhall_rachel_breakfast, dhall_rachel_lunch, dhall_rachel_dinner,
							dhall_nine_breakfast, dhall_nine_lunch, dhall_nine_dinner,):

	# Time
		current_time = datetime.datetime.now(pytz.timezone("US/Pacific"))
	# Day (0-6)(0=monday)
		day = current_time.weekday()
	# Initialize item location list
		self.item_dict = {}
		self.item_array = []
		self.item_locations = []
		for i in range(5):
		    self.item = item
	# Monday
		    if day == 0:
		# Cowell
    			if current_time > self.cowell_breakfast_time_monday and current_time < self.cowell_lunch_time_monday:
	    			self.check_list(dhall_cowell_breakfast, "Cowell & Stevenson")
    			elif current_time > self.cowell_lunch_time_monday and current_time < self.cowell_dinner_time_monday:
		    		self.check_list(dhall_cowell_lunch, "Cowell & Stevenson")
	    		elif current_time > self.cowell_dinner_time_monday and current_time < self.cowell_closing_time_monday:
		    		self.check_list(dhall_cowell_dinner, "Cowell & Stevenson")
		# Crown
	    		if current_time > self.crown_breakfast_time_monday and current_time < self.crown_lunch_time_monday:
		    		self.check_list(dhall_crown_breakfast, "Crown & Merrill")
	    		elif current_time > self.crown_lunch_time_monday and current_time < self.crown_dinner_time_monday:
	    			self.check_list(dhall_crown_lunch, "Crown & Merrill")
	    		elif current_time > self.crown_dinner_time_monday and current_time < self.crown_closing_time_monday:
			    	self.check_list(dhall_crown_dinner, "Crown & Merrill")
		# Porter
		    	if current_time > self.porter_breakfast_time_monday and current_time < self.porter_lunch_time_monday:
		    		self.check_list(dhall_porter_breakfast, "Porter & Kresge")
		    	elif current_time > self.porter_lunch_time_monday and current_time < self.porter_dinner_time_monday:
		    		self.check_list(dhall_porter_lunch, "Porter & Kresge")
		    	elif current_time > self.porter_dinner_time_monday and current_time < self.porter_closing_time_monday:
		    		self.check_list(dhall_porter_dinner, "Porter & Kresge")
		# Rachel
		    	if current_time > self.rachel_breakfast_time_monday and current_time < self.rachel_lunch_time_monday:
	    			self.check_list(dhall_rachel_breakfast, "Rachel Carson & Oakes")
	    		elif current_time > self.rachel_lunch_time_monday and current_time < self.rachel_dinner_time_monday:
	    			self.check_list(dhall_rachel_lunch, "Rachel Carson & Oakes")
	    		elif current_time > self.rachel_dinner_time_monday and current_time < self.rachel_closing_time_monday:
	    			self.check_list(dhall_rachel_dinner, "Rachel Carson & Oakes")
		# Nine
		    	if current_time > self.nine_breakfast_time_monday and current_time < self.nine_lunch_time_monday:
		    		self.check_list(dhall_nine_breakfast, "Nine & Ten")
		    	elif current_time > self.nine_lunch_time_monday and current_time < self.nine_dinner_time_monday:
		    		self.check_list(dhall_nine_lunch, "Nine & Ten")
		    	elif current_time > self.nine_dinner_time_monday and current_time < self.nine_closing_time_monday:
		    		self.check_list(dhall_nine_dinner, "Nine & Ten")

	# Tuesday
		    if day == 1:
		# Cowell
	    	   	if current_time > self.cowell_breakfast_time_tuesday and current_time < self.cowell_lunch_time_tuesday:
			       	    self.check_list(dhall_cowell_breakfast, "Cowell & Stevenson")
		        elif current_time > self.cowell_lunch_time_tuesday and current_time < self.cowell_dinner_time_tuesday:
	    	   		self.check_list(dhall_cowell_lunch, "Cowell & Stevenson")
	    	   	elif current_time > self.cowell_dinner_time_tuesday and current_time < self.cowell_closing_time_tuesday:
	   		        self.check_list(dhall_cowell_dinner, "Cowell & Stevenson")
		# Crown
		        if current_time > self.crown_breakfast_time_tuesday and current_time < self.crown_lunch_time_tuesday:
    			    self.check_list(dhall_crown_breakfast, "Crown & Merril")
		        elif current_time > self.crown_lunch_time_tuesday and current_time < self.crown_dinner_time_tuesday:
		            self.check_list(dhall_crown_lunch, "Crown & Merril")
		        elif current_time > self.crown_dinner_time_tuesday and current_time < self.crown_closing_time_tuesday:
		            self.check_list(dhall_crown_dinner, "Crown & Merril")
		# Porter
		        if current_time > self.porter_breakfast_time_tuesday and current_time < self.porter_lunch_time_tuesday:
		            self.check_list(dhall_porter_breakfast, "Porter & Kresge")
		        elif current_time > self.porter_lunch_time_tuesday and current_time < self.porter_dinner_time_tuesday:
		            self.check_list(dhall_porter_lunch, "Porter & Kresge")
		        elif current_time > self.porter_dinner_time_tuesday and current_time < self.porter_closing_time_tuesday:
		            self.check_list(dhall_porter_dinner, "Porter & Kresge")
		# Rachel
		        if current_time > self.rachel_breakfast_time_tuesday and current_time < self.rachel_lunch_time_tuesday:
		            self.check_list(dhall_rachel_breakfast, "Rachel Carson & Oakes")
		        elif current_time > self.rachel_lunch_time_tuesday and current_time < self.rachel_dinner_time_tuesday:
		            self.check_list(dhall_rachel_lunch, "Rachel Carson & Oakes")
		        elif current_time > self.rachel_dinner_time_tuesday and current_time < self.rachel_closing_time_tuesday:
		            self.check_list(dhall_rachel_dinner, "Rachel Carson & Oakes")
		# Nine
		        if current_time > self.nine_breakfast_time_tuesday and current_time < self.nine_lunch_time_tuesday:
		            self.check_list(dhall_nine_breakfast, "Nine & Ten")
		        elif current_time > self.nine_lunch_time_tuesday and current_time < self.nine_dinner_time_tuesday:
		            self.check_list(dhall_nine_lunch, "Nine & Ten")
		        elif current_time > self.nine_dinner_time_tuesday and current_time < self.nine_closing_time_tuesday:
		            self.check_list(dhall_nine_dinner, "Nine & Ten")

	# Wednesday
		    if day == 2:
		# Cowell
			    if current_time > self.cowell_breakfast_time_wednesday and current_time < self.cowell_lunch_time_wednesday:
			    	self.check_list(dhall_cowell_breakfast, "Cowell & Stevenson")
			    elif current_time > self.cowell_lunch_time_wednesday and current_time < self.cowell_dinner_time_wednesday:
			    	self.check_list(dhall_cowell_lunch, "Cowell & Stevenson")
			    elif current_time > self.cowell_dinner_time_wednesday and current_time < self.cowell_closing_time_wednesday:
			    	self.check_list(dhall_cowell_dinner, "Cowell & Stevenson")
		# Crown
			    if current_time > self.crown_breakfast_time_wednesday and current_time < self.crown_lunch_time_wednesday:
	    			self.check_list(dhall_crown_breakfast, "Crown & Merrill")
			    elif current_time > self.crown_lunch_time_wednesday and current_time < self.crown_dinner_time_wednesday:
				    self.check_list(dhall_crown_lunch, "Crown & Merrill")
			    elif current_time > self.crown_dinner_time_wednesday and current_time < self.crown_closing_time_wednesday:
				    self.check_list(dhall_crown_dinner, "Crown & Merrill")
		# Porter
			    if current_time > self.porter_breakfast_time_wednesday and current_time < self.porter_lunch_time_wednesday:
				    self.check_list(dhall_porter_breakfast, "Porter & Kresge")
			    elif current_time > self.porter_lunch_time_wednesday and current_time < self.porter_dinner_time_wednesday:
				    self.check_list(dhall_porter_lunch, "Porter & Kresge")
			    elif current_time > self.porter_dinner_time_wednesday and current_time < self.porter_closing_time_wednesday:
			    	self.check_list(dhall_porter_dinner, "Porter & Kresge")
		# Rachel
			    if current_time > self.rachel_breakfast_time_wednesday and current_time < self.rachel_lunch_time_wednesday:
				    self.check_list(dhall_rachel_breakfast, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_lunch_time_wednesday and current_time < self.rachel_dinner_time_wednesday:
				    self.check_list(dhall_rachel_lunch, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_dinner_time_wednesday and current_time < self.rachel_closing_time_wednesday:
				    self.check_list(dhall_rachel_dinner, "Rachel Carson & Oakes")
		# Nine
			    if current_time > self.nine_breakfast_time_wednesday and current_time < self.nine_lunch_time_wednesday:
				    self.check_list(dhall_nine_breakfast, "Nine & Ten")
			    elif current_time > self.nine_lunch_time_wednesday and current_time < self.nine_dinner_time_wednesday:
				    self.check_list(dhall_nine_lunch, "Nine & Ten")
			    elif current_time > self.nine_dinner_time_wednesday and current_time < self.nine_closing_time_wednesday:
				    self.check_list(dhall_nine_dinner, "Nine & Ten")



	# Thursday
		    if day == 3:
		# Cowell
			    if current_time > self.cowell_breakfast_time_thursday and current_time < self.cowell_lunch_time_thursday:
				    self.check_list(dhall_cowell_breakfast, "Cowell & Stevenson")
			    elif current_time > self.cowell_lunch_time_thursday and current_time < self.cowell_dinner_time_thursday:
				    self.check_list(dhall_cowell_lunch, "Cowell & Stevenson")
			    elif current_time > self.cowell_dinner_time_thursday and current_time < self.cowell_closing_time_thursday:
			    	self.check_list(dhall_cowell_dinner, "Cowell & Stevenson")
		# Crown
			    if current_time > self.crown_breakfast_time_thursday and current_time < self.crown_lunch_time_thursday:
				    self.check_list(dhall_crown_breakfast, "Crown & Merril")
			    elif current_time > self.crown_lunch_time_thursday and current_time < self.crown_dinner_time_thursday:
				    self.check_list(dhall_crown_lunch, "Crown & Merril")
			    elif current_time > self.crown_dinner_time_thursday and current_time < self.crown_closing_time_thursday:
			    	self.check_list(dhall_crown_dinner, "Crown & Merril")
		# Porter
			    if current_time > self.porter_breakfast_time_thursday and current_time < self.porter_lunch_time_thursday:
				    self.check_list(dhall_porter_breakfast, "Porter & Kresge")
			    elif current_time > self.porter_lunch_time_thursday and current_time < self.porter_dinner_time_thursday:
				    self.check_list(dhall_porter_lunch, "Porter & Kresge")
			    elif current_time > self.porter_dinner_time_thursday and current_time < self.porter_closing_time_thursday:
				    self.check_list(dhall_porter_dinner, "Porter & Kresge")
		# Rachel
			    if current_time > self.rachel_breakfast_time_thursday and current_time < self.rachel_lunch_time_thursday:
				    self.check_list(dhall_rachel_breakfast, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_lunch_time_thursday and current_time < self.rachel_dinner_time_thursday:
				    self.check_list(dhall_rachel_lunch, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_dinner_time_thursday and current_time < self.rachel_closing_time_thursday:
				    self.check_list(dhall_rachel_dinner, "Rachel Carson & Oakes")
		# Nine
			    if current_time > self.nine_breakfast_time_thursday and current_time < self.nine_lunch_time_thursday:
				    self.check_list(dhall_nine_breakfast, "Nine & Ten")
			    elif current_time > self.nine_lunch_time_thursday and current_time < self.nine_dinner_time_thursday:
				    self.check_list(dhall_nine_lunch, "Nine & Ten")
			    elif current_time > self.nine_dinner_time_thursday and current_time < self.nine_closing_time_thursday:
				    self.check_list(dhall_nine_dinner, "Nine & Ten")

	# Friday
		    if day == 4:
		# Cowell
			    if current_time > self.cowell_breakfast_time_friday and current_time < self.cowell_lunch_time_friday:
				    self.check_list(dhall_cowell_breakfast, "Cowell & Stevenson")
			    elif current_time > self.cowell_lunch_time_friday and current_time < self.cowell_dinner_time_friday:
				    self.check_list(dhall_cowell_lunch, "Cowell & Stevenson")
			    elif current_time > self.cowell_dinner_time_friday and current_time < self.cowell_closing_time_friday:
				    self.check_list(dhall_cowell_dinner, "Cowell & Stevenson")
		# Crown
			    if current_time > self.crown_breakfast_time_friday and current_time < self.crown_lunch_time_friday:
				    self.check_list(dhall_crown_breakfast, "Crown & Merrill")
			    elif current_time > self.crown_lunch_time_friday and current_time < self.crown_dinner_time_friday:
				    self.check_list(dhall_crown_lunch, "Crown & Merrill")
			    elif current_time > self.crown_dinner_time_friday and current_time < self.crown_closing_time_friday:
				    self.check_list(dhall_crown_dinner, "Crown & Merrill")
		# Porter
			    if current_time > self.porter_breakfast_time_friday and current_time < self.porter_lunch_time_friday:
				    self.check_list(dhall_porter_breakfast, "Porter & Kresge")
			    elif current_time > self.porter_lunch_time_friday and current_time < self.porter_dinner_time_friday:
				    self.check_list(dhall_porter_lunch, "Porter & Kresge")
			    elif current_time > self.porter_dinner_time_friday and current_time < self.porter_closing_time_friday:
				    self.check_list(dhall_porter_dinner, "Porter & Kresge")
		# Rachel
			    if current_time > self.rachel_breakfast_time_friday and current_time < self.rachel_lunch_time_friday:
				    self.check_list(dhall_rachel_breakfast, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_lunch_time_friday and current_time < self.rachel_dinner_time_friday:
				    self.check_list(dhall_rachel_lunch, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_dinner_time_friday and current_time < self.rachel_closing_time_friday:
				    self.check_list(dhall_rachel_dinner, "Rachel Carson & Oakes")
		# Nine
			    if current_time > self.nine_breakfast_time_friday and current_time < self.nine_lunch_time_friday:
				    self.check_list(dhall_nine_breakfast, "Nine & Ten")
			    elif current_time > self.nine_lunch_time_friday and current_time < self.nine_dinner_time_friday:
				    self.check_list(dhall_nine_lunch, "Nine & Ten")
			    elif current_time > self.nine_dinner_time_friday and current_time < self.nine_closing_time_friday:
			    	self.check_list(dhall_nine_dinner, "Nine & Ten")

	# Saturday
		    if day == 5:
		# Cowell
			    if current_time > self.cowell_breakfast_time_saturday and current_time < self.cowell_lunch_time_saturday:
				    self.check_list(dhall_cowell_breakfast, "Cowell & Stevenson")
			    elif current_time > self.cowell_lunch_time_saturday and current_time < self.cowell_dinner_time_saturday:
				    self.check_list(dhall_cowell_lunch, "Cowell & Stevenson")
			    elif current_time > self.cowell_dinner_time_saturday and current_time < self.cowell_closing_time_saturday:
				    self.check_list(dhall_cowell_dinner, "Cowell & Stevenson")
		# Crown
			    if current_time > self.crown_breakfast_time_saturday and current_time < self.crown_lunch_time_saturday:
				    self.check_list(dhall_crown_breakfast, "Crown & Merrill")
			    elif current_time > self.crown_lunch_time_saturday and current_time < self.crown_dinner_time_saturday:
				    self.check_list(dhall_crown_lunch, "Crown & Merrill")
			    elif current_time > self.crown_dinner_time_saturday and current_time < self.crown_closing_time_saturday:
				    self.check_list(dhall_crown_dinner, "Crown & Merrill")
		# Porter
			    if current_time > self.porter_breakfast_time_saturday and current_time < self.porter_lunch_time_saturday:
				    self.check_list(dhall_porter_breakfast, "Porter & Kresge")
			    elif current_time > self.porter_lunch_time_saturday and current_time < self.porter_dinner_time_saturday:
				    self.check_list(dhall_porter_lunch, "Porter & Kresge")
			    elif current_time > self.porter_dinner_time_saturday and current_time < self.porter_closing_time_saturday:
				    self.check_list(dhall_porter_dinner, "Porter & Kresge")
		# Rachel
			    if current_time > self.rachel_breakfast_time_saturday and current_time < self.rachel_lunch_time_saturday:
				    self.check_list(dhall_rachel_breakfast, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_lunch_time_saturday and current_time < self.rachel_dinner_time_saturday:
				    self.check_list(dhall_rachel_lunch, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_dinner_time_saturday and current_time < self.rachel_closing_time_saturday:
				    self.check_list(dhall_rachel_dinner, "Rachel Carson & Oakes")
		# Nine
			    if current_time > self.nine_breakfast_time_saturday and current_time < self.nine_lunch_time_saturday:
				    self.check_list(dhall_nine_breakfast, "Nine & Ten")
			    elif current_time > self.nine_lunch_time_saturday and current_time < self.nine_dinner_time_saturday:
				    self.check_list(dhall_nine_lunch, "Nine & Ten")
			    elif current_time > self.nine_dinner_time_saturday and current_time < self.nine_closing_time_saturday:
				    self.check_list(dhall_nine_dinner, "Nine & Ten")

	# Sunday
		    if day == 6:
		# Cowell
			    if current_time > self.cowell_breakfast_time_sunday and current_time < self.cowell_lunch_time_sunday:
				    self.check_list(dhall_cowell_breakfast, "Cowell & Stevenson")
			    elif current_time > self.cowell_lunch_time_sunday and current_time < self.cowell_dinner_time_sunday:
				    self.check_list(dhall_cowell_lunch, "Cowell & Stevenson")
			    elif current_time > self.cowell_dinner_time_sunday and current_time < self.cowell_closing_time_sunday:
				    self.check_list(dhall_cowell_dinner, "Cowell & Stevenson")
		# Crown
			    if current_time > self.crown_breakfast_time_sunday and current_time < self.crown_lunch_time_sunday:
				    self.check_list(dhall_crown_breakfast, "Crown & Merrill")
			    elif current_time > self.crown_lunch_time_sunday and current_time < self.crown_dinner_time_sunday:
				    self.check_list(dhall_crown_lunch, "Crown & Merrill")
			    elif current_time > self.crown_dinner_time_sunday and current_time < self.crown_closing_time_sunday:
				    self.check_list(dhall_crown_dinner, "Crown & Merrill")
		# Porter
			    if current_time > self.porter_breakfast_time_sunday and current_time < self.porter_lunch_time_sunday:
				    self.check_list(dhall_porter_breakfast, "Porter & Kresge")
			    elif current_time > self.porter_lunch_time_sunday and current_time < self.porter_dinner_time_sunday:
			    	self.check_list(dhall_porter_lunch, "Porter & Kresge")
			    elif current_time > self.porter_dinner_time_sunday and current_time < self.porter_closing_time_sunday:
				    self.check_list(dhall_porter_dinner, "Porter & Kresge")
		# Rachel
			    if current_time > self.rachel_breakfast_time_sunday and current_time < self.rachel_lunch_time_sunday:
				    self.check_list(dhall_rachel_breakfast, "Rachel Carson & Oakes")
			    elif current_time > self.rachel_lunch_time_sunday and current_time < self.rachel_dinner_time_sunday:
			        self.check_list(dhall_rachel_lunch, "Rachel Carson & Oakes")

			    elif current_time > self.rachel_dinner_time_sunday and current_time < self.rachel_closing_time_sunday:
				    self.check_list(dhall_rachel_dinner, "Rachel Carson & Oakes")
		# Nine
			    if current_time > self.nine_breakfast_time_sunday and current_time < self.nine_lunch_time_sunday:
				    self.check_list(dhall_nine_breakfast, "Nine & Ten")
			    elif current_time > self.nine_lunch_time_sunday and current_time < self.nine_dinner_time_sunday:
				    self.check_list(dhall_nine_lunch, "Nine & Ten")
			    elif current_time > self.nine_dinner_time_sunday and current_time < self.nine_closing_time_sunday:
				    self.check_list(dhall_nine_dinner, "Nine & Ten")

		    if self.item_locations:
		        self.item_dict[self.item] = self.item_locations
		    self.item_locations = []

		if len(self.item_dict) < 5:
			for i in range(5):
				self.item = item
				self.item_array = item.strip().split(" ")
				for idx, food in enumerate(self.item_array):
				    if food[-1] == "s":
				        food = food[:-1]
				        self.item_array[idx] = food
	# Monday
				if day == 0:
			# Cowell
					if current_time > self.cowell_breakfast_time_monday and current_time < self.cowell_lunch_time_monday:
						self.check_list_2(dhall_cowell_breakfast, "Cowell & Stevenson")
					elif current_time > self.cowell_lunch_time_monday and current_time < self.cowell_dinner_time_monday:
						self.check_list_2(dhall_cowell_lunch, "Cowell & Stevenson")
					elif current_time > self.cowell_dinner_time_monday and current_time < self.cowell_closing_time_monday:
						self.check_list_2(dhall_cowell_dinner, "Cowell & Stevenson")
		# Crown
					if current_time > self.crown_breakfast_time_monday and current_time < self.crown_lunch_time_monday:
						self.check_list_2(dhall_crown_breakfast, "Crown & Merrill")
					elif current_time > self.crown_lunch_time_monday and current_time < self.crown_dinner_time_monday:
						self.check_list_2(dhall_crown_lunch, "Crown & Merrill")
					elif current_time > self.crown_dinner_time_monday and current_time < self.crown_closing_time_monday:
						self.check_list_2(dhall_crown_dinner, "Crown & Merrill")
			# Porter
					if current_time > self.porter_breakfast_time_monday and current_time < self.porter_lunch_time_monday:
						self.check_list_2(dhall_porter_breakfast, "Porter & Kresge")
					elif current_time > self.porter_lunch_time_monday and current_time < self.porter_dinner_time_monday:
						self.check_list_2(dhall_porter_lunch, "Porter & Kresge")
					elif current_time > self.porter_dinner_time_monday and current_time < self.porter_closing_time_monday:
						self.check_list_2(dhall_porter_dinner, "Porter & Kresge")
			# Rachel
					if current_time > self.rachel_breakfast_time_monday and current_time < self.rachel_lunch_time_monday:
						self.check_list_2(dhall_rachel_breakfast, "Rachel Carson & Oakes")
					elif current_time > self.rachel_lunch_time_monday and current_time < self.rachel_dinner_time_monday:
						self.check_list_2(dhall_rachel_lunch, "Rachel Carson & Oakes")
					elif current_time > self.rachel_dinner_time_monday and current_time < self.rachel_closing_time_monday:
						self.check_list_2(dhall_rachel_dinner, "Rachel Carson & Oakes")
			# Nine
					if current_time > self.nine_breakfast_time_monday and current_time < self.nine_lunch_time_monday:
						self.check_list_2(dhall_nine_breakfast, "Nine & Ten")
					elif current_time > self.nine_lunch_time_monday and current_time < self.nine_dinner_time_monday:
						self.check_list_2(dhall_nine_lunch, "Nine & Ten")
					elif current_time > self.nine_dinner_time_monday and current_time < self.nine_closing_time_monday:
						self.check_list_2(dhall_nine_dinner, "Nine & Ten")
		# Tuesday
				if day == 1:
			# Cowell
					if current_time > self.cowell_breakfast_time_tuesday and current_time < self.cowell_lunch_time_tuesday:
						self.check_list_2(dhall_cowell_breakfast, "Cowell & Stevenson")
					elif current_time > self.cowell_lunch_time_tuesday and current_time < self.cowell_dinner_time_tuesday:
						self.check_list_2(dhall_cowell_lunch, "Cowell & Stevenson")
					elif current_time > self.cowell_dinner_time_tuesday and current_time < self.cowell_closing_time_tuesday:
						self.check_list_2(dhall_cowell_dinner, "Cowell & Stevenson")
			# Crown
					if current_time > self.crown_breakfast_time_tuesday and current_time < self.crown_lunch_time_tuesday:
						self.check_list_2(dhall_crown_breakfast, "Crown & Merril")
					elif current_time > self.crown_lunch_time_tuesday and current_time < self.crown_dinner_time_tuesday:
						self.check_list_2(dhall_crown_lunch, "Crown & Merril")
					elif current_time > self.crown_dinner_time_tuesday and current_time < self.crown_closing_time_tuesday:
						self.check_list_2(dhall_crown_dinner, "Crown & Merril")
				# Porter
					if current_time > self.porter_breakfast_time_tuesday and current_time < self.porter_lunch_time_tuesday:
						self.check_list_2(dhall_porter_breakfast, "Porter & Kresge")
					elif current_time > self.porter_lunch_time_tuesday and current_time < self.porter_dinner_time_tuesday:
						self.check_list_2(dhall_porter_lunch, "Porter & Kresge")
					elif current_time > self.porter_dinner_time_tuesday and current_time < self.porter_closing_time_tuesday:
						self.check_list_2(dhall_porter_dinner, "Porter & Kresge")
				# Rachel
					if current_time > self.rachel_breakfast_time_tuesday and current_time < self.rachel_lunch_time_tuesday:
						self.check_list_2(dhall_rachel_breakfast, "Rachel Carson & Oakes")
					elif current_time > self.rachel_lunch_time_tuesday and current_time < self.rachel_dinner_time_tuesday:
						self.check_list_2(dhall_rachel_lunch, "Rachel Carson & Oakes")
					elif current_time > self.rachel_dinner_time_tuesday and current_time < self.rachel_closing_time_tuesday:
						self.check_list_2(dhall_rachel_dinner, "Rachel Carson & Oakes")
				# Nine
					if current_time > self.nine_breakfast_time_tuesday and current_time < self.nine_lunch_time_tuesday:
						self.check_list_2(dhall_nine_breakfast, "Nine & Ten")
					elif current_time > self.nine_lunch_time_tuesday and current_time < self.nine_dinner_time_tuesday:
						self.check_list_2(dhall_nine_lunch, "Nine & Ten")
					elif current_time > self.nine_dinner_time_tuesday and current_time < self.nine_closing_time_tuesday:
						self.check_list_2(dhall_nine_dinner, "Nine & Ten")

		# Wednesday
				if day == 2:
			# Cowell
					if current_time > self.cowell_breakfast_time_wednesday and current_time < self.cowell_lunch_time_wednesday:
						self.check_list_2(dhall_cowell_breakfast, "Cowell & Stevenson")
					elif current_time > self.cowell_lunch_time_wednesday and current_time < self.cowell_dinner_time_wednesday:
						self.check_list_2(dhall_cowell_lunch, "Cowell & Stevenson")
					elif current_time > self.cowell_dinner_time_wednesday and current_time < self.cowell_closing_time_wednesday:
						self.check_list_2(dhall_cowell_dinner, "Cowell & Stevenson")
			# Crown
					if current_time > self.crown_breakfast_time_wednesday and current_time < self.crown_lunch_time_wednesday:
						self.check_list_2(dhall_crown_breakfast, "Crown & Merrill")
					elif current_time > self.crown_lunch_time_wednesday and current_time < self.crown_dinner_time_wednesday:
						self.check_list_2(dhall_crown_lunch, "Crown & Merrill")
					elif current_time > self.crown_dinner_time_wednesday and current_time < self.crown_closing_time_wednesday:
						self.check_list_2(dhall_crown_dinner, "Crown & Merrill")
			# Porter
					if current_time > self.porter_breakfast_time_wednesday and current_time < self.porter_lunch_time_wednesday:
						self.check_list_2(dhall_porter_breakfast, "Porter & Kresge")
					elif current_time > self.porter_lunch_time_wednesday and current_time < self.porter_dinner_time_wednesday:
						self.check_list_2(dhall_porter_lunch, "Porter & Kresge")
					elif current_time > self.porter_dinner_time_wednesday and current_time < self.porter_closing_time_wednesday:
						self.check_list_2(dhall_porter_dinner, "Porter & Kresge")
			# Rachel
					if current_time > self.rachel_breakfast_time_wednesday and current_time < self.rachel_lunch_time_wednesday:
						self.check_list_2(dhall_rachel_breakfast, "Rachel Carson & Oakes")
					elif current_time > self.rachel_lunch_time_wednesday and current_time < self.rachel_dinner_time_wednesday:
						self.check_list_2(dhall_rachel_lunch, "Rachel Carson & Oakes")
					elif current_time > self.rachel_dinner_time_wednesday and current_time < self.rachel_closing_time_wednesday:
						self.check_list_2(dhall_rachel_dinner, "Rachel Carson & Oakes")
			# Nine
					if current_time > self.nine_breakfast_time_wednesday and current_time < self.nine_lunch_time_wednesday:
						self.check_list_2(dhall_nine_breakfast, "Nine & Ten")
					elif current_time > self.nine_lunch_time_wednesday and current_time < self.nine_dinner_time_wednesday:
						self.check_list_2(dhall_nine_lunch, "Nine & Ten")
					elif current_time > self.nine_dinner_time_wednesday and current_time < self.nine_closing_time_wednesday:
						self.check_list_2(dhall_nine_dinner, "Nine & Ten")



		# Thursday
				if day == 3:
			# Cowell
					if current_time > self.cowell_breakfast_time_thursday and current_time < self.cowell_lunch_time_thursday:
						self.check_list_2(dhall_cowell_breakfast, "Cowell & Stevenson")
					elif current_time > self.cowell_lunch_time_thursday and current_time < self.cowell_dinner_time_thursday:
						self.check_list_2(dhall_cowell_lunch, "Cowell & Stevenson")
					elif current_time > self.cowell_dinner_time_thursday and current_time < self.cowell_closing_time_thursday:
						self.check_list_2(dhall_cowell_dinner, "Cowell & Stevenson")
			# Crown
					if current_time > self.crown_breakfast_time_thursday and current_time < self.crown_lunch_time_thursday:
						self.check_list_2(dhall_crown_breakfast, "Crown & Merril")
					elif current_time > self.crown_lunch_time_thursday and current_time < self.crown_dinner_time_thursday:
						self.check_list_2(dhall_crown_lunch, "Crown & Merril")
					elif current_time > self.crown_dinner_time_thursday and current_time < self.crown_closing_time_thursday:
						self.check_list_2(dhall_crown_dinner, "Crown & Merril")
			# Porter
					if current_time > self.porter_breakfast_time_thursday and current_time < self.porter_lunch_time_thursday:
						self.check_list_2(dhall_porter_breakfast, "Porter & Kresge")
					elif current_time > self.porter_lunch_time_thursday and current_time < self.porter_dinner_time_thursday:
						self.check_list_2(dhall_porter_lunch, "Porter & Kresge")
					elif current_time > self.porter_dinner_time_thursday and current_time < self.porter_closing_time_thursday:
						self.check_list_2(dhall_porter_dinner, "Porter & Kresge")
			# Rachel
					if current_time > self.rachel_breakfast_time_thursday and current_time < self.rachel_lunch_time_thursday:
						self.check_list_2(dhall_rachel_breakfast, "Rachel Carson & Oakes")
					elif current_time > self.rachel_lunch_time_thursday and current_time < self.rachel_dinner_time_thursday:
						self.check_list_2(dhall_rachel_lunch, "Rachel Carson & Oakes")
					elif current_time > self.rachel_dinner_time_thursday and current_time < self.rachel_closing_time_thursday:
						self.check_list_2(dhall_rachel_dinner, "Rachel Carson & Oakes")
			# Nine
					if current_time > self.nine_breakfast_time_thursday and current_time < self.nine_lunch_time_thursday:
						self.check_list_2(dhall_nine_breakfast, "Nine & Ten")
					elif current_time > self.nine_lunch_time_thursday and current_time < self.nine_dinner_time_thursday:
						self.check_list_2(dhall_nine_lunch, "Nine & Ten")
					elif current_time > self.nine_dinner_time_thursday and current_time < self.nine_closing_time_thursday:
						self.check_list_2(dhall_nine_dinner, "Nine & Ten")

		# Friday
				if day == 4:
			# Cowell
					if current_time > self.cowell_breakfast_time_friday and current_time < self.cowell_lunch_time_friday:
						self.check_list_2(dhall_cowell_breakfast, "Cowell & Stevenson")
					elif current_time > self.cowell_lunch_time_friday and current_time < self.cowell_dinner_time_friday:
						self.check_list_2(dhall_cowell_lunch, "Cowell & Stevenson")
					elif current_time > self.cowell_dinner_time_friday and current_time < self.cowell_closing_time_friday:
						self.check_list_2(dhall_cowell_dinner, "Cowell & Stevenson")
			# Crown
					if current_time > self.crown_breakfast_time_friday and current_time < self.crown_lunch_time_friday:
						self.check_list_2(dhall_crown_breakfast, "Crown & Merrill")
					elif current_time > self.crown_lunch_time_friday and current_time < self.crown_dinner_time_friday:
						self.check_list_2(dhall_crown_lunch, "Crown & Merrill")
					elif current_time > self.crown_dinner_time_friday and current_time < self.crown_closing_time_friday:
						self.check_list_2(dhall_crown_dinner, "Crown & Merrill")
			# Porter
					if current_time > self.porter_breakfast_time_friday and current_time < self.porter_lunch_time_friday:
						self.check_list_2(dhall_porter_breakfast, "Porter & Kresge")
					elif current_time > self.porter_lunch_time_friday and current_time < self.porter_dinner_time_friday:
						self.check_list_2(dhall_porter_lunch, "Porter & Kresge")
					elif current_time > self.porter_dinner_time_friday and current_time < self.porter_closing_time_friday:
						self.check_list_2(dhall_porter_dinner, "Porter & Kresge")
			# Rachel
					if current_time > self.rachel_breakfast_time_friday and current_time < self.rachel_lunch_time_friday:
						self.check_list_2(dhall_rachel_breakfast, "Rachel Carson & Oakes")
					elif current_time > self.rachel_lunch_time_friday and current_time < self.rachel_dinner_time_friday:
						self.check_list_2(dhall_rachel_lunch, "Rachel Carson & Oakes")
					elif current_time > self.rachel_dinner_time_friday and current_time < self.rachel_closing_time_friday:
						self.check_list_2(dhall_rachel_dinner, "Rachel Carson & Oakes")
			# Nine
					if current_time > self.nine_breakfast_time_friday and current_time < self.nine_lunch_time_friday:
						self.check_list_2(dhall_nine_breakfast, "Nine & Ten")
					elif current_time > self.nine_lunch_time_friday and current_time < self.nine_dinner_time_friday:
						self.check_list_2(dhall_nine_lunch, "Nine & Ten")
					elif current_time > self.nine_dinner_time_friday and current_time < self.nine_closing_time_friday:
						self.check_list_2(dhall_nine_dinner, "Nine & Ten")

		# Saturday
				if day == 5:
			# Cowell
					if current_time > self.cowell_breakfast_time_saturday and current_time < self.cowell_lunch_time_saturday:
						self.check_list_2(dhall_cowell_breakfast, "Cowell & Stevenson")
					elif current_time > self.cowell_lunch_time_saturday and current_time < self.cowell_dinner_time_saturday:
						self.check_list_2(dhall_cowell_lunch, "Cowell & Stevenson")
					elif current_time > self.cowell_dinner_time_saturday and current_time < self.cowell_closing_time_saturday:
						self.check_list_2(dhall_cowell_dinner, "Cowell & Stevenson")
			# Crown
					if current_time > self.crown_breakfast_time_saturday and current_time < self.crown_lunch_time_saturday:
						self.check_list_2(dhall_crown_breakfast, "Crown & Merrill")
					elif current_time > self.crown_lunch_time_saturday and current_time < self.crown_dinner_time_saturday:
						self.check_list_2(dhall_crown_lunch, "Crown & Merrill")
					elif current_time > self.crown_dinner_time_saturday and current_time < self.crown_closing_time_saturday:
						self.check_list_2(dhall_crown_dinner, "Crown & Merrill")
			# Porter
					if current_time > self.porter_breakfast_time_saturday and current_time < self.porter_lunch_time_saturday:
						self.check_list_2(dhall_porter_breakfast, "Porter & Kresge")
					elif current_time > self.porter_lunch_time_saturday and current_time < self.porter_dinner_time_saturday:
						self.check_list_2(dhall_porter_lunch, "Porter & Kresge")
					elif current_time > self.porter_dinner_time_saturday and current_time < self.porter_closing_time_saturday:
						self.check_list_2(dhall_porter_dinner, "Porter & Kresge")
			# Rachel
					if current_time > self.rachel_breakfast_time_saturday and current_time < self.rachel_lunch_time_saturday:
						self.check_list_2(dhall_rachel_breakfast, "Rachel Carson & Oakes")
					elif current_time > self.rachel_lunch_time_saturday and current_time < self.rachel_dinner_time_saturday:
						self.check_list_2(dhall_rachel_lunch, "Rachel Carson & Oakes")
					elif current_time > self.rachel_dinner_time_saturday and current_time < self.rachel_closing_time_saturday:
						self.check_list_2(dhall_rachel_dinner, "Rachel Carson & Oakes")
			# Nine
					if current_time > self.nine_breakfast_time_saturday and current_time < self.nine_lunch_time_saturday:
						self.check_list_2(dhall_nine_breakfast, "Nine & Ten")
					elif current_time > self.nine_lunch_time_saturday and current_time < self.nine_dinner_time_saturday:
						self.check_list_2(dhall_nine_lunch, "Nine & Ten")
					elif current_time > self.nine_dinner_time_saturday and current_time < self.nine_closing_time_saturday:
						self.check_list_2(dhall_nine_dinner, "Nine & Ten")

		# Sunday
				if day == 6:
			# Cowell
					if current_time > self.cowell_breakfast_time_sunday and current_time < self.cowell_lunch_time_sunday:
						self.check_list_2(dhall_cowell_breakfast, "Cowell & Stevenson")
					elif current_time > self.cowell_lunch_time_sunday and current_time < self.cowell_dinner_time_sunday:
						self.check_list_2(dhall_cowell_lunch, "Cowell & Stevenson")
					elif current_time > self.cowell_dinner_time_sunday and current_time < self.cowell_closing_time_sunday:
						self.check_list_2(dhall_cowell_dinner, "Cowell & Stevenson")
			# Crown
					if current_time > self.crown_breakfast_time_sunday and current_time < self.crown_lunch_time_sunday:
						self.check_list_2(dhall_crown_breakfast, "Crown & Merrill")
					elif current_time > self.crown_lunch_time_sunday and current_time < self.crown_dinner_time_sunday:
						self.check_list_2(dhall_crown_lunch, "Crown & Merrill")
					elif current_time > self.crown_dinner_time_sunday and current_time < self.crown_closing_time_sunday:
						self.check_list_2(dhall_crown_dinner, "Crown & Merrill")
			# Porter
					if current_time > self.porter_breakfast_time_sunday and current_time < self.porter_lunch_time_sunday:
						self.check_list_2(dhall_porter_breakfast, "Porter & Kresge")
					elif current_time > self.porter_lunch_time_sunday and current_time < self.porter_dinner_time_sunday:
						self.check_list_2(dhall_porter_lunch, "Porter & Kresge")
					elif current_time > self.porter_dinner_time_sunday and current_time < self.porter_closing_time_sunday:
						self.check_list_2(dhall_porter_dinner, "Porter & Kresge")
			# Rachel
					if current_time > self.rachel_breakfast_time_sunday and current_time < self.rachel_lunch_time_sunday:
						self.check_list_2(dhall_rachel_breakfast, "Rachel Carson & Oakes")
					elif current_time > self.rachel_lunch_time_sunday and current_time < self.rachel_dinner_time_sunday:
						self.check_list_2(dhall_rachel_lunch, "Rachel Carson & Oakes")

					elif current_time > self.rachel_dinner_time_sunday and current_time < self.rachel_closing_time_sunday:
						self.check_list_2(dhall_rachel_dinner, "Rachel Carson & Oakes")
			# Nine
					if current_time > self.nine_breakfast_time_sunday and current_time < self.nine_lunch_time_sunday:
						self.check_list_2(dhall_nine_breakfast, "Nine & Ten")
					elif current_time > self.nine_lunch_time_sunday and current_time < self.nine_dinner_time_sunday:
						self.check_list_2(dhall_nine_lunch, "Nine & Ten")
					elif current_time > self.nine_dinner_time_sunday and current_time < self.nine_closing_time_sunday:
						self.check_list_2(dhall_nine_dinner, "Nine & Ten")

				if self.item_locations:
					self.item_dict[self.item] = self.item_locations
				self.item_locations = []

				if len(self.item_dict) == 5:
				    break

		if self.item_dict:
		    return_string = "Dining halls currently serving:\n"
		    count = 1
		    for key in self.item_dict:
		        return_string = return_string + str(count)+". " + key +"\n" + "\n".join(self.item_dict[key]) + "\n"
		        count += 1
		    return return_string
		else:
		    return "No dining halls are currently serving " + self.item