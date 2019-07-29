from google.appengine.ext import ndb
class Car(ndb.Model):
    make = ndb.StringProperty(required = True)
    model = ndb.StringProperty(required = True)
    color = ndb.StringProperty(required = True)

    def printCarInfo(self):
        print(self.make + " " + self.model + " " + self.color)
car1 = Car(make="ford", model="mustang", color="green")
car1.printCarInfo()
