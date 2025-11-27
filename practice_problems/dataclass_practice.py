from collections import namedtuple
from dataclasses import dataclass, field
from math import sqrt
import random
from typing import NamedTuple

# Warm-up Problem 1: Make a namedtuple that contains three readings, print them and sort by temp
# This `namedtuple` returns a subclass of tuple (the type)
Reading = namedtuple('Reading', 'Celsius Location Timestamp')
Reading1 = Reading(98.5, "roof", "2025-01-25")
Reading2 = Reading(100.5, "kitchen", "2025-11-21")
Reading3 = Reading(75.6, "basement", "2025-05-16")
# I can access this by x.Celsius because this is an attr (object) of reading but I could also access by position I think
sorted_nt = sorted([Reading1, Reading2, Reading3], key=lambda x: x.Celsius, reverse=True)

# for reading in sorted_nt:
#     print(reading)

# Warm-up Problem 2: Use typing.NamedTuple with Validation on Type Annotations
class SatCoordinates(NamedTuple):
    # The interpreter will initialize Lat, Lon, Altitude with their init variables (e.g. self.Latitude = Latitude)
    Latitude: float
    Longitude: float
    Altitude: float

    def euclidean_distance(self):
        radius = 6371
        return sqrt((self.Latitude - radius)**2 + (self.Longitude - radius)**2 + self.Altitude**2)

# Warm-up Problem 3: Implement a Battery Pack class using data class
@dataclass
class BatteryPack:
    capacity: float
    current_charge: float
    manufacturer: str = "ACME Energy"

    def percent_remaining(self):
        return (self.current_charge / self.capacity) * 100

# Problem 4: Immutable v. Mutable Spacecraft Position

# Use the NamedTuple for the initial fixed launch state coordinates because we want the coords to be immutable
class InitialCoords(NamedTuple):
    x: float
    y: float
    z: float

# Since we want live_coords to update we want something mutable and @dataclass gives us mutable data structures
@dataclass
class LiveCoords:
    spacecraft_id: int
    initial_coords: InitialCoords = InitialCoords(0, 0, 0)
    live_coords: list = field(default_factory=list)  # Set a default value so that we each time we instance the class there is a new list

    def update_live_location(self):
        new = InitialCoords(
            self.initial_coords.x + random.randint(1, 10),
            self.initial_coords.y + random.randint(1, 8),
            self.initial_coords.z + random.randint(1, 7)
        )
        self.initial_coords = new
        self.live_coords.append(new)
        return self.live_coords

# Problem 6: Validate Spacecraft Component
@dataclass
class SpacecraftComponent:
    name: str
    mass_kg: float
    power_watts: float
    voltage_v: float
    
    # @dataclass takes the attributes given to it and initializes them to an instance attribute 
    # *but* we may need to do more processing after the __init__ (hence __post_init) to validate fields
    # and values before they are used later on by other methods
    def __post_init__(self):
        if not self.name:
            raise ValueError("name of spacecraft component must not be empty")
        if self.mass_kg <= 0:
            raise ValueError(f"Mass kg {self.mass_kg} is cannot be less than zero")
        if self.power_watts < 0:
            raise ValueError(f"Power watts {self.power_watts} cannot be less than 0")
        if self.voltage_v < 0 or self.voltage_v > 100:
            raise ValueError(f"Voltage: {self.voltage_v} is outside range of 0-100")

    def efficiency(self):
        if self.power_watts == 0:
            return 0
        return self.power_watts / self.mass_kg
