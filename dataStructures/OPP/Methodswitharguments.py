class Circle:
    pi=3.14
    def area(self, radius):
        return Circle.pi*radius**2
circle=Circle()
pizza_area=circle.area(12/2)
print (pizza_area)
teaching_table_area=circle.area(36/2)
print (teaching_table_area)
round_room_area=circle.area(11460/2)
print(round_room_area)
