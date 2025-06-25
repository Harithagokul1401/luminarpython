#parent         super      base
#child           sub         derived 
class parent:
    def phone (self):
        print("have a realme phone")

class child(parent):
    pass

c=child()

c.phone()# child ka object hai and usse parent class ka function ko call kiya 
