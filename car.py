class Car:
    def __init__(self,name,color,miles):
        self.name = name
        self.color = color
        self.miles = miles
    def __str__(self):
        return f"The {self.color} has {self.miles} miles"
blue_car = Car(name='blue',color='blue',miles='20,000')
red_car = Car(name ='red',color = 'red',miles='30,000')
print(blue_car);
print(red_car);