# Python 3
# LPThW Exercise 4

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars * space_in_car
average_passengers_per_car = passengers / cars_driven

print("There are ", cars, " availabe.")
print("There are only ", drivers, " available.")
print("There will be ", cars_not_driven, " empty cars today.")
print("We can transport ", carpool_capacity, " people today.")
print("We have ", passengers, " to carpool today.")
print("We need to put about ", average_passengers_per_car,
      " passengers in each car.")
