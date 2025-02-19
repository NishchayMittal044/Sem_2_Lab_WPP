# Write a class called Converter. The user will pass a length and a unit when declaring an object
# from the class—for example, c = Converter(9,'inches'). The possible units are inches, feet,
# yards, miles, kilometers, meters, centimeters, and millimeters. For each of these units there
# should be a method that returns the length converted into those units. For example, using the
# Converter object created above, the user could call c.feet() and should get 0.75 as the result.

class Converter:#CONVERSION FACTORS TO CONVERT ALL TO METER
    conversion_factors = {
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.34,
        "kilometers": 1000,
        "meters": 1,
        "centimeters": 0.01,
        "millimeters": 0.001
    }

    def __init__(self,length,unit):
        if(unit not in self.conversion_factors):
            return "Inavlid Unit"
        self.length_metre = length * self.conversion_factors[unit]
        #CONVERTED EVERY LENGTH TO METER
    #FINDING EVERY LENGTH
    def inches(self):
        return self.length_metre / self.conversion_factors["inches"]
    
    def feet(self):
        return self.length_metre / self.conversion_factors["feet"]
    
    def yards(self):
        return self.length_metre / self.conversion_factors["yards"]
    
    def miles(self):
        return self.length_metre / self.conversion_factors["miles"]
    
    def kilometers(self):
        return self.length_metre / self.conversion_factors["kilometers"]
    
    def meters(self):
        return self.length_metre / self.conversion_factors["meters"]
    
    def centimeters(self):
        return self.length_metre / self.conversion_factors["centimeters"]
    
    def millimeters(self):
        return self.length_metre / self.conversion_factors["millimeters"]


c = Converter(9,"inches")
print(c.miles())
print(c.meters())