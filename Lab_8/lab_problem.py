class Cellphone:
        model = "Iphone"
        def __init__(self, brand, model, fingerprint):

            self.brand = brand
            self.model = model
            self.fingerprint = fingerprint

iphone12 = Cellphone("Apple", "12 Mini", "No")
iphone13 = Cellphone("Apple", "13 Mini", "No")
print (iphone12.model)
print (iphone13.model)
print ("{} Iphone {} Has fingerprint scanner : {}".format(iphone12.brand, iphone12.model, iphone12.fingerprint))
print ("{} Iphone {} Has fingerprint scanner : {}".format(iphone13.brand, iphone13.model, iphone13.fingerprint))



class Phone:
    brand = "Apple"

    def __init__(self, brand, model, fingerprint, faceid, camera, availability):
        self.brand = brand
        self.model = model
        self.fingerprint = fingerprint
        self.faceid = faceid
        self.camera = camera
        self.availability = availability

iphone8 = Phone("Apple", "Iphone 8", "Yes", "No", "12MP", "Yes")
iphone14 = Phone("Apple", "Iphone 14", "No", "Yes", "48MP", "Yes")
print ("{}\n{}\nFingerprint scanner: {}\nFace ID: {}\nCamera megapixels: {}\nAvailability: {}\n\n".format(iphone8.brand, iphone8.model, iphone8.fingerprint, iphone8.faceid, iphone8.camera, iphone8.availability))
print ("{}\n{}\nFingerprint scanner: {}\nFace ID: {}\nCamera megapixels: {}\nAvailability: {}\n\n".format(iphone14.brand, iphone14.model, iphone14.fingerprint, iphone14.faceid, iphone14.camera,iphone14.availability))
iphone8.availability = ("Discontinued")
print ("{}\n{}\nFingerprint scanner: {}\nFace ID: {}\nCamera megapixels: {}\nAvailability: {}\n\n".format(iphone8.brand, iphone8.model, iphone8.fingerprint, iphone8.faceid, iphone8.camera, iphone8.availability))


class Supercar:
    wheels = 4
    seats = 2
    def __init__(self, brand, mpg, speed):
        self.brand = brand
        self.mpg = mpg
        self.speed = speed
    
    def accelerate(self):
        self.speed += 20
    
    def decelerate(self):
        self.speed -= 50

james = Supercar ( "Porsche 911 GT3 RS", 100, 140)
print ("The Super car is a {}, it has {} mpg and is going {} mpg.". format (james.brand, james.mpg, james.speed)) 
print ("The Car has: {} wheels".format(james.wheels))
james.decelerate() 
print ("The Super car is a {}, it has {} mpg and is going {} mpg.". format (james.brand, james.mpg, james.speed)) 