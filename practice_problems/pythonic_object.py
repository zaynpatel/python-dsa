# classmethod v. staticmethod
# @classmethod is meant to operate on the class itself while self operates on the instance
# Problem 1: Given a User class implement three constructors using @classmethod
class User:
    def __init__(self, username, email, is_admin=False):
        self.username = username
        self.email = email
        self.is_admin = is_admin
    
    @classmethod
    # classmethod is useful in more complicated situations like if we inherited a class and wanted to use this method
    # because we have `cls` which is not a hard-coded class that we may have if we used self/staticmethod
    def from_string(cls, string):
        username, email, is_admin = string.split("|")
        if is_admin == "True": 
            is_admin = True 
        else: 
            is_admin = False
        return cls(username, email, is_admin)  # We want to return the class...
        
    @classmethod
    def guest(cls):
        username = "guest"
        email = "guest@unknown"
        is_admin = False
        return cls(username, email, is_admin)

    @classmethod
    def admin(cls, username):
        username = username
        email = f"{username}@admin.local"
        is_admin = True
        return cls(username, email, is_admin)

# This creates an instance of the class `User`
# If I used `self` instead of `cls` I would need to change the __init__ to accept other formats like strings
# And then the method would apply the split logic (so I would call this somewhere)
s = User.from_string("zayn|zaynp@gmail.com|True")
# print(s.email)

# Problem 2: Design a class hierarchy to model different types of spacecraft thrusters
class Thruster:
    def __init__(self, power_kw, propellent):
        self.power_kw = power_kw
        self.propellent = propellent
    
    def thrust(self):
        return self.power_kw * 3

    @classmethod
    def choose_propellent(cls, payload_kg):
        if payload_kg < 10:
            return "Type 1"
        elif payload_kg > 10 and payload_kg < 50:
            return "Type 2"
        else:
            return "Type 3"

    @classmethod
    # Recall that classmethod is called an alternate constructor because it creates instances of the class by using cls() instead of an explicit __init__
    def from_mission_profile(cls, distance_km, payload_kg):
        propellent = None
        power_kw = distance_km * 40.0  # I just chose a random float
        propellent = cls.choose_propellent(payload_kg)
        return cls(power_kw, propellent)  # Remember that this gives us an instance of Thruster with power_kw and propellent given by above logic
    
class ChemicalThruster(Thruster):
    # Now if I decide I want to override the propellent I can just override this classmethod
    @classmethod
    def choose_propellent(cls, payload_kg):
        return "Chemical 1"

class IonThruster(Thruster):
    @classmethod
    def choose_propellent(cls, payload_kg):
        return "Chemical 2"
    
class RandomThruster(Thruster):
    pass

# thr = IonThruster.from_mission_profile(50, 100)
# print(thr.propellent)  # This returns "Chemical 2"
# One of the biggest "plusses" of @classmethod is that I can make a subclass and it will have its own instance of Thruster because of
# @classmethod on the mission_profile method in Thruster
# If we just subclassed without cls then we would still have an instance of Thruster and not an instance w.r.t the subclass
# rt = IonThruster.from_mission_profile(500, 30)

# Problem 3: Notice the difference in class behavior with and without special methods
# Class without dunder methods
class SensorPackage:
    def __init__(self, serial_number, mass_kg, range_km, resolution_bits, wavelength_nm, manufacturer):
        self.serial_number = serial_number
        self.mass_kg = mass_kg
        self.range_km = range_km
        self.resolution_bits = resolution_bits
        self.wavelength_nm = wavelength_nm
        self.manufacturer = manufacturer

s = SensorPackage(1, 1, 1, 1, 1, 1)
# print(s)  # default __repr__: <__main__.SensorPackage object at 0x102618830>
t = SensorPackage(1, 1, 1, 1, 1, 1)
# assert s == t  # This fails because the __eq__ in the class compares object identity not the values in the instances
# We can see why the assert fails by printing out the id of the object (memory address)
# print(id(s), id(t)) -> 4306061360 4305995088

# Class with dunder methods
class SensorPackage2:
    def __init__(self, serial_number, mass_kg, range_km, resolution_bits, wavelength_nm, manufacturer):
        self.serial_number = serial_number
        self.mass_kg = mass_kg
        self.range_km = range_km
        self.resolution_bits = resolution_bits
        self.wavelength_nm = wavelength_nm
        self.manufacturer = manufacturer
    
    def __repr__(self):
        return f"Class Name: {__class__.__name__}, SerialNumber:{self.serial_number}, Mass:{self.mass_kg}, Manufacturer:{self.manufacturer}"

    def __eq__(self, other: SensorPackage2):
        # TODO: How do I implement __iter__ so I can have more than two items?
        return tuple((self.serial_number, self.manufacturer)) == tuple((other.serial_number, other.manufacturer))

    def __hash__(self):
        # As I mentioned before __eq__ in the class refers to object identity being equal so when we change it to define
        # value equality we also need to change how we assign has values b/c if we don't change it then __hash__ is None
        # because Python takes __hash__ away when we define custom __eq__ otherwise hash will keep hashing object equality
        # and not value equality
        return hash((self.serial_number, self.manufacturer))
    
    def __lt__(self, other: SensorPackage2):
        return self.mass_kg < other.mass_kg


s2 = SensorPackage2(1, 1, 1, 1, 1, 1)
# print(s2)  new __repr__: Class Name: SensorPackage2, SerialNumber:1, Mass:1, Manufacturer:1
# s3 = SensorPackage2(1, 2, 3, 4, 4, 5)
# s4 = SensorPackage(1, 1, 1, 3, 4, 5)
# assert s3.mass_kg > s4.mass_kg
