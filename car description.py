class Vehicle:
    name = ""
    value = 100.00
    color = ""
    kind = ""

    def description(self):
        desc_str = "%s is a %s %s worth  %s" % (self.name, str(self.value), self.color, self.kind)
        return desc_str


car1 = Vehicle()
car1.name = "Lamborghini"
car1.value = 60000.00
car1.color = "Green"
car1.kind = "Lamborghini"

car2 = Vehicle()
car2.name = "Suv"
car2.value = 40000.00
car2.color = "blue"
car2.kind = "Ferrari"

print(car1.description())
print(car2.description())
