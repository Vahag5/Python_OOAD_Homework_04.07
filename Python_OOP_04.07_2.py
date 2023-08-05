class Car:
	total_cars = 0
	def __init__(self,model,year,seria):
		self._model = model
		self._year = year 
		self._seria = seria
		Car.total_cars += 1
	def set_model(self, model):
		self._model = model
	def get_model(self):
		return self._model
	def set_year(self, year):
		self._year = year
	def get_year(self):
		return self._year
	def set_seria(self,seria):
		self._seria = seria
	def get_seria(self):
		return self._seria  
	def __str__(self):
		return f"Car: {self._model} {self._year} {self._seria}"
	@classmethod
	def display_total_cars(cls):
		return f"Total Cars: {cls.total_cars}"

car1 = Car("BMW","2001","M3_E46")
car2 = Car("Mercedes_Benz","1995","W124")
car3 = Car("Infinity", "2000","QX4")

print(car1)
print(car2)
print(car3)

print(Car.display_total_cars())

# Car: BMW 2001 M3_E46
# Car: Mercedes_Benz 1995 W124
# Car: Infinity 2000 QX4
# Total Cars: 3