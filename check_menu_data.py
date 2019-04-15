import update_menu, time

class CheckMenuData:
	def __init__(self):
	    self.update = update_menu.UpdateMenu()
	    self.initialize_old_data()
	    self.initialize_current_data()


	def initialize_old_data(self):
    # Cowell lists
	    self.dhall_cowell_breakfast_old = []
	    self.dhall_cowell_lunch_old = []
	    self.dhall_cowell_dinner_old = []
	# Crown lists
	    self.dhall_crown_breakfast_old = []
	    self.dhall_crown_lunch_old = []
	    self.dhall_crown_dinner_old = []
	# Porter lists
	    self.dhall_porter_breakfast_old = []
	    self.dhall_porter_lunch_old = []
	    self.dhall_porter_dinner_old = []
	# Rachel lists
	    self.dhall_rachel_breakfast_old = []
	    self.dhall_rachel_lunch_old = []
	    self.dhall_rachel_dinner_old = []
	# Nine and ten lists
	    self.dhall_nine_breakfast_old = []
	    self.dhall_nine_lunch_old = []
	    self.dhall_nine_dinner_old = []


	def initialize_current_data(self):
    # Cowell lists
	    self.dhall_cowell_breakfast_current = []
	    self.dhall_cowell_lunch_current = []
	    self.dhall_cowell_dinner_current = []
	# Crown lists
	    self.dhall_crown_breakfast_current = []
	    self.dhall_crown_lunch_current = []
	    self.dhall_crown_dinner_current = []
	# Porter lists
	    self.dhall_porter_breakfast_current = []
	    self.dhall_porter_lunch_current = []
	    self.dhall_porter_dinner_current = []
	# Rachel lists
	    self.dhall_rachel_breakfast_current = []
	    self.dhall_rachel_lunch_current = []
	    self.dhall_rachel_dinner_current = []
	# Nine and ten lists
	    self.dhall_nine_breakfast_current = []
	    self.dhall_nine_lunch_current = []
	    self.dhall_nine_dinner_current = []

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


	def compare_menus(self):
	# Cowell
	    if self.dhall_cowell_breakfast_current != self.dhall_cowell_breakfast_old or self.dhall_cowell_lunch_current != self.dhall_cowell_lunch_old or self.dhall_cowell_dinner_current != self.dhall_cowell_dinner_old:
	        print("cowell menus not equal")
	        self.update.execute()
	        return True
	    elif self.dhall_crown_breakfast_current != self.dhall_crown_breakfast_old or self.dhall_crown_lunch_current != self.dhall_crown_lunch_old or self.dhall_crown_dinner_current != self.dhall_crown_dinner_old:
	        print("crown menus not equal")
	        self.update.execute()
	        return True
	    elif self.dhall_porter_breakfast_current != self.dhall_porter_breakfast_old or self.dhall_porter_lunch_current != self.dhall_porter_lunch_old or self.dhall_porter_dinner_current != self.dhall_porter_dinner_old:
	        print("porter menus not equal")
	        self.update.execute()
	        return True
	    elif self.dhall_rachel_breakfast_current != self.dhall_rachel_breakfast_old or self.dhall_rachel_lunch_current != self.dhall_rachel_lunch_old or self.dhall_rachel_dinner_current != self.dhall_rachel_dinner_old:
	        print("rachel menus not equal")
	        self.update.execute()
	        return True
	    elif self.dhall_nine_breakfast_current != self.dhall_nine_breakfast_old or self.dhall_nine_lunch_current != self.dhall_nine_lunch_old or self.dhall_nine_dinner_current != self.dhall_nine_dinner_old:
	        print("nine menus not equal")
	        self.update.execute()
	        return True
	    else:
	       print("menus are definitely equal")
	       return False

	def execute(self):
    # Obtain old data for all dining halls
		self.fetch_menu("cowell_menu.txt", self.dhall_cowell_breakfast_old, self.dhall_cowell_lunch_old, self.dhall_cowell_dinner_old)
		self.fetch_menu("crown_menu.txt", self.dhall_crown_breakfast_old, self.dhall_crown_lunch_old, self.dhall_crown_dinner_old)
		self.fetch_menu("porter_menu.txt", self.dhall_porter_breakfast_old, self.dhall_porter_lunch_old, self.dhall_porter_dinner_old)
		self.fetch_menu("rachel_menu.txt", self.dhall_rachel_breakfast_old, self.dhall_rachel_lunch_old, self.dhall_rachel_dinner_old)
		self.fetch_menu("nine_menu.txt", self.dhall_nine_breakfast_old, self.dhall_nine_lunch_old, self.dhall_nine_dinner_old)
    # Removing menu label from lists
		self.dhall_cowell_breakfast_old.pop(0)
		self.dhall_cowell_lunch_old.pop(0)
		self.dhall_cowell_dinner_old.pop(0)
		self.dhall_crown_breakfast_old.pop(0)
		self.dhall_crown_lunch_old.pop(0)
		self.dhall_crown_dinner_old.pop(0)
		self.dhall_porter_breakfast_old.pop(0)
		self.dhall_porter_lunch_old.pop(0)
		self.dhall_porter_dinner_old.pop(0)
		self.dhall_rachel_breakfast_old.pop(0)
		self.dhall_rachel_lunch_old.pop(0)
		self.dhall_rachel_dinner_old.pop(0)
		self.dhall_nine_breakfast_old.pop(0)
		self.dhall_nine_lunch_old.pop(0)
		self.dhall_nine_dinner_old.pop(0)
		while(1):
		# Removing data
			self.initialize_current_data()
		# Obtain current data for all dining halls
			self.update.get_current_data("Cowell+Stevenson+Dining+Hall", "05", self.dhall_cowell_breakfast_current, self.dhall_cowell_lunch_current, self.dhall_cowell_dinner_current)
			self.update.get_current_data("Crown+Merrill+Dining+Hall", "20", self.dhall_crown_breakfast_current, self.dhall_crown_lunch_current, self.dhall_crown_dinner_current)
			self.update.get_current_data("Porter+Kresge+Dining+Hall", "25", self.dhall_porter_breakfast_current, self.dhall_porter_lunch_current, self.dhall_porter_dinner_current)
			self.update.get_current_data("Rachel+Carson+Oakes+Dining+Hall", "30", self.dhall_rachel_breakfast_current, self.dhall_rachel_lunch_current, self.dhall_rachel_dinner_current)
			self.update.get_current_data("College+Nine+%26+Ten", "40", self.dhall_nine_breakfast_current, self.dhall_nine_lunch_current, self.dhall_nine_dinner_current)
		# Comparing
			if self.compare_menus():
				self.dhall_cowell_breakfast_old = self.dhall_cowell_breakfast_current
				self.dhall_cowell_lunch_old = self.dhall_cowell_lunch_current
				self.dhall_cowell_dinner_old = self.dhall_cowell_dinner_current
				self.dhall_crown_breakfast_old = self.dhall_crown_breakfast_current
				self.dhall_crown_lunch_old = self.dhall_crown_lunch_current
				self.dhall_crown_dinner_old = self.dhall_crown_dinner_current
				self.dhall_porter_breakfast_old = self.dhall_porter_breakfast_current
				self.dhall_porter_lunch_old = self.dhall_porter_lunch_current
				self.dhall_porter_dinner_old = self.dhall_porter_dinner_current
				self.dhall_rachel_breakfast_old = self.dhall_rachel_breakfast_current
				self.dhall_rachel_lunch_old = self.dhall_rachel_lunch_current
				self.dhall_rachel_dinner_old = self.dhall_rachel_dinner_current
				self.dhall_nine_breakfast_old = self.dhall_nine_breakfast_current
				self.dhall_nine_lunch_old = self.dhall_nine_lunch_current
				self.dhall_nine_dinner_old = self.dhall_nine_dinner_current

			time.sleep(900) # 15 minutes

if __name__ == '__main__':
	check = CheckMenuData()
	check.execute()


