#!/usr/bin/python3.6
# Description:
    # This script provides daily schedules for dining hall
    # This class is used in another file to keep the flow clean in the 'dhall_service.py' file

import datetime, pytz


class HoursQuery:
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




    def send_hours(self, dhall):
	# Day (0-6)(0=monday)
	    current_time = datetime.datetime.now(pytz.timezone("US/Pacific"))
	    day = current_time.weekday()
	# Monday
	    if day == 0:
		# Cowell
	    	if dhall == "cowell":
			    if current_time < self.cowell_closing_time_monday and current_time > self.cowell_breakfast_time_monday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Monday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.cowell_breakfast_time_monday.strftime("%I:%M %p")+"\nLunch   "+self.cowell_lunch_time_monday.strftime("%I:%M %p")+" \nDinner   "+self.cowell_dinner_time_monday.strftime("%I:%M %p")+"\nClosing   "+self.cowell_closing_time_monday.strftime("%I:%M %p")
		# Crown
	    	if dhall == "crown":
			    if current_time < self.crown_closing_time_monday and current_time > self.crown_breakfast_time_monday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Monday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.crown_breakfast_time_monday.strftime("%I:%M %p")+"\nLunch   "+self.crown_lunch_time_monday.strftime("%I:%M %p")+" \nDinner   "+self.crown_dinner_time_monday.strftime("%I:%M %p")+"\nClosing   "+self.crown_closing_time_monday.strftime("%I:%M %p")
        # Porter
	    	if dhall == "porter":
			    if current_time < self.porter_closing_time_monday and current_time > self.porter_breakfast_time_monday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Monday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.porter_breakfast_time_monday.strftime("%I:%M %p")+"\nLunch   "+self.porter_lunch_time_monday.strftime("%I:%M %p")+" \nDinner   "+self.porter_dinner_time_monday.strftime("%I:%M %p")+"\nClosing   "+self.porter_closing_time_monday.strftime("%I:%M %p")
        # Rachel
	    	if dhall == "rachel":
			    if current_time < self.rachel_closing_time_monday and current_time > self.rachel_breakfast_time_monday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Monday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.rachel_breakfast_time_monday.strftime("%I:%M %p")+"\nLunch   "+self.rachel_lunch_time_monday.strftime("%I:%M %p")+" \nDinner   "+self.rachel_dinner_time_monday.strftime("%I:%M %p")+"\nClosing   "+self.rachel_closing_time_monday.strftime("%I:%M %p")
        # Nine
	    	if dhall == "nine":
			    if current_time < self.nine_closing_time_monday and current_time > self.nine_breakfast_time_monday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Monday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.nine_breakfast_time_monday.strftime("%I:%M %p")+"\nLunch   "+self.nine_lunch_time_monday.strftime("%I:%M %p")+" \nDinner   "+self.nine_dinner_time_monday.strftime("%I:%M %p")+"\nClosing   "+self.nine_closing_time_monday.strftime("%I:%M %p")







	# Tuesday
	    elif day == 1:
		# Cowell
	    	if dhall == "cowell":
			    if current_time < self.cowell_closing_time_tuesday and current_time > self.cowell_breakfast_time_tuesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Tuesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.cowell_breakfast_time_tuesday.strftime("%I:%M %p")+"\nLunch   "+self.cowell_lunch_time_tuesday.strftime("%I:%M %p")+" \nDinner   "+self.cowell_dinner_time_tuesday.strftime("%I:%M %p")+"\nClosing   "+self.cowell_closing_time_tuesday.strftime("%I:%M %p")
		# Crown
	    	if dhall == "crown":
			    if current_time < self.crown_closing_time_tuesday and current_time > self.crown_breakfast_time_tuesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Tuesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.crown_breakfast_time_tuesday.strftime("%I:%M %p")+"\nLunch   "+self.crown_lunch_time_tuesday.strftime("%I:%M %p")+" \nDinner   "+self.crown_dinner_time_tuesday.strftime("%I:%M %p")+"\nClosing   "+self.crown_closing_time_tuesday.strftime("%I:%M %p")
        # Porter
	    	if dhall == "porter":
			    if current_time < self.porter_closing_time_tuesday and current_time > self.porter_breakfast_time_tuesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Tuesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.porter_breakfast_time_tuesday.strftime("%I:%M %p")+"\nLunch   "+self.porter_lunch_time_tuesday.strftime("%I:%M %p")+" \nDinner   "+self.porter_dinner_time_tuesday.strftime("%I:%M %p")+"\nClosing   "+self.porter_closing_time_tuesday.strftime("%I:%M %p")
        # Rachel
	    	if dhall == "rachel":
			    if current_time < self.rachel_closing_time_tuesday and current_time > self.rachel_breakfast_time_tuesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Tuesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.rachel_breakfast_time_tuesday.strftime("%I:%M %p")+"\nLunch   "+self.rachel_lunch_time_tuesday.strftime("%I:%M %p")+" \nDinner   "+self.rachel_dinner_time_tuesday.strftime("%I:%M %p")+"\nClosing   "+self.rachel_closing_time_tuesday.strftime("%I:%M %p")
        # Nine
	    	if dhall == "nine":
			    if current_time < self.nine_closing_time_tuesday and current_time > self.nine_breakfast_time_tuesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Tuesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.nine_breakfast_time_tuesday.strftime("%I:%M %p")+"\nLunch   "+self.nine_lunch_time_tuesday.strftime("%I:%M %p")+" \nDinner   "+self.nine_dinner_time_tuesday.strftime("%I:%M %p")+"\nClosing   "+self.nine_closing_time_tuesday.strftime("%I:%M %p")




	# Wednesday
	    elif day == 2:
		# Cowell
	    	if dhall == "cowell":
			    if current_time < self.cowell_closing_time_wednesday and current_time > self.cowell_breakfast_time_wednesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Wednesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.cowell_breakfast_time_wednesday.strftime("%I:%M %p")+"\nLunch   "+self.cowell_lunch_time_wednesday.strftime("%I:%M %p")+" \nDinner   "+self.cowell_dinner_time_wednesday.strftime("%I:%M %p")+"\nClosing   "+self.cowell_closing_time_wednesday.strftime("%I:%M %p")
		# Crown
	    	if dhall == "crown":
			    if current_time < self.crown_closing_time_wednesday and current_time > self.crown_breakfast_time_wednesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Wednesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.crown_breakfast_time_wednesday.strftime("%I:%M %p")+"\nLunch   "+self.crown_lunch_time_wednesday.strftime("%I:%M %p")+" \nDinner   "+self.crown_dinner_time_wednesday.strftime("%I:%M %p")+"\nClosing   "+self.crown_closing_time_wednesday.strftime("%I:%M %p")
        # Porter
	    	if dhall == "porter":
			    if current_time < self.porter_closing_time_wednesday and current_time > self.porter_breakfast_time_wednesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Wednesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.porter_breakfast_time_wednesday.strftime("%I:%M %p")+"\nLunch   "+self.porter_lunch_time_wednesday.strftime("%I:%M %p")+" \nDinner   "+self.porter_dinner_time_wednesday.strftime("%I:%M %p")+"\nClosing   "+self.porter_closing_time_wednesday.strftime("%I:%M %p")
        # Rachel
	    	if dhall == "rachel":
			    if current_time < self.rachel_closing_time_wednesday and current_time > self.rachel_breakfast_time_wednesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Wednesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.rachel_breakfast_time_wednesday.strftime("%I:%M %p")+"\nLunch   "+self.rachel_lunch_time_wednesday.strftime("%I:%M %p")+" \nDinner   "+self.rachel_dinner_time_wednesday.strftime("%I:%M %p")+"\nClosing   "+self.rachel_closing_time_wednesday.strftime("%I:%M %p")
        # Nine
	    	if dhall == "nine":
			    if current_time < self.nine_closing_time_wednesday and current_time > self.nine_breakfast_time_wednesday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Wednesday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.nine_breakfast_time_wednesday.strftime("%I:%M %p")+"\nLunch   "+self.nine_lunch_time_wednesday.strftime("%I:%M %p")+" \nDinner   "+self.nine_dinner_time_wednesday.strftime("%I:%M %p")+"\nClosing   "+self.nine_closing_time_wednesday.strftime("%I:%M %p")



	# Thursday
	    elif day == 3:
		# Cowell
	    	if dhall == "cowell":
			    if current_time < self.cowell_closing_time_thursday and current_time > self.cowell_breakfast_time_thursday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Thursday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.cowell_breakfast_time_thursday.strftime("%I:%M %p")+"\nLunch   "+self.cowell_lunch_time_thursday.strftime("%I:%M %p")+" \nDinner   "+self.cowell_dinner_time_thursday.strftime("%I:%M %p")+"\nClosing   "+self.cowell_closing_time_thursday.strftime("%I:%M %p")
		# Crown
	    	if dhall == "crown":
			    if current_time < self.crown_closing_time_thursday and current_time > self.crown_breakfast_time_thursday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Thursday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.crown_breakfast_time_thursday.strftime("%I:%M %p")+"\nLunch   "+self.crown_lunch_time_thursday.strftime("%I:%M %p")+" \nDinner   "+self.crown_dinner_time_thursday.strftime("%I:%M %p")+"\nClosing   "+self.crown_closing_time_thursday.strftime("%I:%M %p")
        # Porter
	    	if dhall == "porter":
			    if current_time < self.porter_closing_time_thursday and current_time > self.porter_breakfast_time_thursday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Thursday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.porter_breakfast_time_thursday.strftime("%I:%M %p")+"\nLunch   "+self.porter_lunch_time_thursday.strftime("%I:%M %p")+" \nDinner   "+self.porter_dinner_time_thursday.strftime("%I:%M %p")+"\nClosing   "+self.porter_closing_time_thursday.strftime("%I:%M %p")
        # Rachel
	    	if dhall == "rachel":
			    if current_time < self.rachel_closing_time_thursday and current_time > self.rachel_breakfast_time_thursday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Thursday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.rachel_breakfast_time_thursday.strftime("%I:%M %p")+"\nLunch   "+self.rachel_lunch_time_thursday.strftime("%I:%M %p")+" \nDinner   "+self.rachel_dinner_time_thursday.strftime("%I:%M %p")+"\nClosing   "+self.rachel_closing_time_thursday.strftime("%I:%M %p")
        # Nine
	    	if dhall == "nine":
			    if current_time < self.nine_closing_time_thursday and current_time > self.nine_breakfast_time_thursday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Thursday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.nine_breakfast_time_thursday.strftime("%I:%M %p")+"\nLunch   "+self.nine_lunch_time_thursday.strftime("%I:%M %p")+" \nDinner   "+self.nine_dinner_time_thursday.strftime("%I:%M %p")+"\nClosing   "+self.nine_closing_time_thursday.strftime("%I:%M %p")



	# Friday
	    elif day == 4:
		# Cowell
	    	if dhall == "cowell":
			    if current_time < self.cowell_closing_time_friday and current_time > self.cowell_breakfast_time_friday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Friday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.cowell_breakfast_time_friday.strftime("%I:%M %p")+"\nLunch   "+self.cowell_lunch_time_friday.strftime("%I:%M %p")+" \nDinner   "+self.cowell_dinner_time_friday.strftime("%I:%M %p")+"\nClosing   "+self.cowell_closing_time_friday.strftime("%I:%M %p")
		# Crown
	    	if dhall == "crown":
			    if current_time < self.crown_closing_time_friday and current_time > self.crown_breakfast_time_friday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Friday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.crown_breakfast_time_friday.strftime("%I:%M %p")+"\nLunch   "+self.crown_lunch_time_friday.strftime("%I:%M %p")+" \nDinner   "+self.crown_dinner_time_friday.strftime("%I:%M %p")+"\nClosing   "+self.crown_closing_time_friday.strftime("%I:%M %p")
        # Porter
	    	if dhall == "porter":
			    if current_time < self.porter_closing_time_friday and current_time > self.porter_breakfast_time_friday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Friday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.porter_breakfast_time_friday.strftime("%I:%M %p")+"\nLunch   "+self.porter_lunch_time_friday.strftime("%I:%M %p")+" \nDinner   "+self.porter_dinner_time_friday.strftime("%I:%M %p")+"\nClosing   "+self.porter_closing_time_friday.strftime("%I:%M %p")
        # Rachel
	    	if dhall == "rachel":
			    if current_time < self.rachel_closing_time_friday and current_time > self.rachel_breakfast_time_friday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Friday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.rachel_breakfast_time_friday.strftime("%I:%M %p")+"\nLunch   "+self.rachel_lunch_time_friday.strftime("%I:%M %p")+" \nDinner   "+self.rachel_dinner_time_friday.strftime("%I:%M %p")+"\nClosing   "+self.rachel_closing_time_friday.strftime("%I:%M %p")
        # Nine
	    	if dhall == "nine":
			    if current_time < self.nine_closing_time_friday and current_time > self.nine_breakfast_time_friday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Friday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.nine_breakfast_time_friday.strftime("%I:%M %p")+"\nLunch   "+self.nine_lunch_time_friday.strftime("%I:%M %p")+" \nDinner   "+self.nine_dinner_time_friday.strftime("%I:%M %p")+"\nClosing   "+self.nine_closing_time_friday.strftime("%I:%M %p")




	# Saturday
	    elif day == 5:
		# Cowell
	    	if dhall == "cowell":
			    if current_time < self.cowell_closing_time_saturday and current_time > self.cowell_breakfast_time_saturday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Saturday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.cowell_breakfast_time_saturday.strftime("%I:%M %p")+"\nLunch   "+self.cowell_lunch_time_saturday.strftime("%I:%M %p")+" \nDinner   "+self.cowell_dinner_time_saturday.strftime("%I:%M %p")+"\nClosing   "+self.cowell_closing_time_saturday.strftime("%I:%M %p")
		# Crown
	    	if dhall == "crown":
			    if current_time < self.crown_closing_time_saturday and current_time > self.crown_breakfast_time_saturday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Saturday Hours--\nClosed today"
        # Porter
	    	if dhall == "porter":
			    if current_time < self.porter_closing_time_saturday and current_time > self.porter_breakfast_time_saturday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Saturday Hours--\nClosed today"
        # Rachel
	    	if dhall == "rachel":
			    if current_time < self.rachel_closing_time_saturday and current_time > self.rachel_breakfast_time_saturday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Saturday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.rachel_breakfast_time_saturday.strftime("%I:%M %p")+"\nLunch   "+self.rachel_lunch_time_saturday.strftime("%I:%M %p")+" \nDinner   "+self.rachel_dinner_time_saturday.strftime("%I:%M %p")+"\nClosing   "+self.rachel_closing_time_saturday.strftime("%I:%M %p")
        # Nine
	    	if dhall == "nine":
			    if current_time < self.nine_closing_time_saturday and current_time > self.nine_breakfast_time_saturday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Saturday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.nine_breakfast_time_saturday.strftime("%I:%M %p")+"\nLunch   "+self.nine_lunch_time_saturday.strftime("%I:%M %p")+" \nDinner   "+self.nine_dinner_time_saturday.strftime("%I:%M %p")+"\nClosing   "+self.nine_closing_time_saturday.strftime("%I:%M %p")




	# Sunday
	    elif day == 6:
		# Cowell
	    	if dhall == "cowell":
			    if current_time < self.cowell_closing_time_sunday and current_time > self.cowell_breakfast_time_sunday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Sunday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.cowell_breakfast_time_sunday.strftime("%I:%M %p")+"\nLunch   "+self.cowell_lunch_time_sunday.strftime("%I:%M %p")+" \nDinner   "+self.cowell_dinner_time_sunday.strftime("%I:%M %p")+"\nClosing   "+self.cowell_closing_time_sunday.strftime("%I:%M %p")
		# Crown
	    	if dhall == "crown":
			    if current_time < self.crown_closing_time_sunday and current_time > self.crown_breakfast_time_sunday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Sunday Hours--\nClosed today"
        # Porter
	    	if dhall == "porter":
			    if current_time < self.porter_closing_time_sunday and current_time > self.porter_breakfast_time_sunday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Sunday Hours--\nClosed today"
        # Rachel
	    	if dhall == "rachel":
			    if current_time < self.rachel_closing_time_sunday and current_time > self.rachel_breakfast_time_sunday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Sunday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.rachel_breakfast_time_sunday.strftime("%I:%M %p")+"\nLunch   "+self.rachel_lunch_time_sunday.strftime("%I:%M %p")+" \nDinner   "+self.rachel_dinner_time_sunday.strftime("%I:%M %p")+"\nClosing   "+self.rachel_closing_time_sunday.strftime("%I:%M %p")
        # Nine
	    	if dhall == "nine":
			    if current_time < self.nine_closing_time_sunday and current_time > self.nine_breakfast_time_sunday:
			        self.open_status = "open"
			    else:
			        self.open_status = "closed"
			    return "--Sunday Hours--\nCurrently "+self.open_status+"\nBreakfast   "+self.nine_breakfast_time_sunday.strftime("%I:%M %p")+"\nLunch   "+self.nine_lunch_time_sunday.strftime("%I:%M %p")+" \nDinner   "+self.nine_dinner_time_sunday.strftime("%I:%M %p")+"\nClosing   "+self.nine_closing_time_sunday.strftime("%I:%M %p")
