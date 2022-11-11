# class

# class Car:
#     color = "Grey"
#     wheels = 4
#
# car1 = Car()
# car1.color = "Blue"
# car2 = Car()
# car2.number = "B312"
# print(car1.__dict__)
# print(car2.__dict__)
# print(Car.__dict__)


# class House:
#     fundament = "beton"
#     wall = 4
#     roof = "White"
#     def __init__(self,
#                  count_window, count_room,
#                  count_door, color_house):
#         self.count_window = count_window
#         self.count_room = count_room
#         self.count_door = count_door
#         self.color_house = color_house
#         self.count_floor = 0
#
#     def get_info(self):
#         print(f"window: {self.count_window}, room: {self.count_room}, "
#               f"door: {self.count_door}, color: {self.color_house}, "
#               f"floor: {self.count_floor}, fundament: {self.fundament}")
#
#     def build_floor(self):
#         self.count_floor += 1
#
#
#
# house_2 = House(15, 5, 5, "black")
# house_19 = House(115, 50, 75, "black")
# house_19.build_floor()
# house_19.build_floor()
# house_2.build_floor()
# house_2.get_info()
# house_19.get_info()
# print(house_2.__dict__)
# print(house_2.count_floor)
# print(house_19.__dict__)
# print(house_19.count_floor)


# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type ):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def discribe_restaurant(self):
#         print(f"restaurant_name: {self.restaurant_name}, cuisine_type: {self.cuisine_type}")
#
#     def open_restaurant(self):
#         print(f"Ресторан открыт")
#
# restaurant = Restaurant("Abesov's yummy fish", "Rissian")
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.discribe_restaurant()
# restaurant.open_restaurant()





# class Car:
#     def __init__(self, brand, model, color, avr_consume, price):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.avr_consume = avr_consume
#         self.price = price
#         self.fuel = 0
#         self.odometer = 0
#
#     def describe_car(self):
#         print(
#             f"brand: {self.brand}, model: {self.model}, color: {self.color}, average_consume: {self.avr_consume}, price: {self.price}")
#
#     def add_fuel(self, litr):
#         self.fuel += litr
#     def drive(self, km,):
#         self.odometer += km
#         if self.fuel <= 0:
#             print("У вас пустой бак")
#         elif (km / 100 * self.avr_consume) > self.fuel:
#             print("Не хватает бензина")
#         elif (km / 100 * self.avr_consume) <= self.fuel:
#             print("Хватает бензина")
#
#
#
#
# toyota = Car("toyota", "camry70", "white", 12, 20000)
# print(toyota.describe_car())
# toyota.add_fuel(55)
# print(toyota.odometer)
# toyota.drive(250)



def start_a(func):
    def wrapper(*args, **kwargs):
        names = func(*args, **kwargs)
        filtered = [x for x in names if x.lower().startswith('a')]
        return filtered
    return wrapper

@start_a
def list_of_name():
    return ['Aman', 'Askat', 'Kanat']

print(list_of_name())