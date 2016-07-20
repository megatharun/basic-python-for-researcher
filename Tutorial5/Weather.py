
# Weather.py

"""Weather conditions of selected towns in Selangor, Malaysia

    Attributes:
        temp: integer/floating value of temperature
        cond: string of weather condition
        wcond: integer/floating value of wind speed
        prep: integer/floating value of humidity
"""

class Weather(object):
    
    def __init__(self, datalist):
        
        self.temp = float(datalist[0])
        self.cond = datalist[1]
        self.wcond = int(datalist[2])
        self.prep = int(datalist[3])
    
    def changetemperature(self, temp):

        self.temp = float(temp)
        print "The temperature is %.1f%sC" % (self.temp,u"\u00B0")

    # New condition
    def changecondition(self, cond):
        self.cond = cond
        print "The condition is %s" % self.cond

    # New wind speed
    def changewindspeed(self, wcond):
        self.wcond = wcond
        print "The wind speed is %d km/hr" % self.wcond
        
    # New humidity
    def changehumidity(self, prep):
        self.prep = prep
        print "The humidity is %d%s" % (self.prep,u"\u0025")

    # Temperature
    def temperature(self):

        print "The temperature is %.1f%sC" % (self.temp,u"\u00B0")

    # Condition
    def condition(self):

        print "The condition is %s" % self.cond

    # Wind speed
    def windspeed(self):

        print "The wind speed is %d km/hr" % self.wcond
        
    # Humidity
    def humidity(self):

        print "The humidity is %d%s" % (self.prep,u"\u0025")