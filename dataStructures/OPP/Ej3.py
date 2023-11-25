class circle: 

    pi= 3.14
    def _init_(self,diameter):
        print(´Creating circle with diameter (d)´, format(d=diameter))

        self.radius = diameter/2

    def circumference(self):
        return 2*self.pi*self.radius

medium_pizza = circle(12)
teaching_table = circle(36)
round_room = circle(11460)
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
