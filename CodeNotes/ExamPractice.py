
# The program creates objects for employees' salaries.


class Employee:
	
	def __init__(self : any, name : str, id : str) -> None:
		"""The initializer method sets attributes for employees."""
		self._name = name
		self._id = id
		return None

class Engineer(Employee):

	def __init__(self : any, name : str, id : int, title : str, hours : int) -> None:
		"""The initializer method sets the object with five attributes."""
		Employee.__init__(self, name, id)
		self.__title = title
		self.__hours = hours
		self.__pay_rate = 0
		return None

	def pay(self, title : str) -> int:
		"""The method assigns the employee's pay."""
		# A dictionary for storing the pay rates of each type of engineer:
		self.titles = {
			      "Engineer Intern" : 20,
			      "Senior Engineer" : 45,
			      "Lead Engineer"   : 70 
				      }
		# Assigns the pay to the engineer:
		self.__pay_rate = self.titles[title]
		return self.__pay_rate
		
	def salary(self) -> float:
		"""The method calculates and returns the pay for the employee."""
		# Calculates the hours worked:
		self.over = (self.__hours - 40)
		self.over = (self.over if (self.over >=0) else 0)
		self.regular = (self.__hours - self.over)
		# Calculates the salaries:
		self.salary = (self.regular * self.pay(self.__title))
		self.salary += (self.over * self.pay(self.__title) * 1.5)
		return self.salary

	def __str__(self) -> str:
		"""The method formats the employee's information."""
		# Formats the output:
		format =  f"Payroll Data for the employee {self._id}:\n"
		format += f"{self._name}'s pay this week is: ${self.salary():,.2f}"
		return format

prompts = {
	0 : "Enter the employee's name: ",
	1 : "Enter the employee's ID number: ",
	2 : "Enter the employee's title: ",
	3 : "Enter the number of hours the employee worked this week: ",
	4 : "Invalid. Hours worked can't be negative or greater than 60.",
}

def main(run=False) -> None:
	"""The function drives the program."""
	# Call a function to prompt for the information:
	info = information()
	# Creates an object with its attributes:
	employee = Engineer(info[0], info[1], info[2], info[3])
	# Prints the information:
	print(employee)
	return None
	
def information() -> list:
	"""The function prompts and returns a list with all the input 
	information."""
	# Empty list:
	info = list()
	# Prompts for the first three questions:
	for index in range(3):
		get = input(prompts[index])
		info.append(get)
	# Prompts for the pay:
	hours = int(input(prompts[3]))
	run = (True if (hours > 60 or hours < 0) else False)
	while run:
		print(prompts[4])
		hours = int(input(prompts[3]))
		run = (True if (hours > 60 or hours < 0) else False)
	# Appends the hours to the list:
	info.append(hours)
	return info
	
if __name__ == "__main__":
	main(run=True)