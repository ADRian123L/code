"""The program is intended to practice and run class programs."""

# Base class:
class Computer:
    
    def __init__(self : any, memory : float, speed : float) -> None:
        """The initializer method adds attributes that electronic 
        devices have."""
        self.__cpu_speed = speed
        self.__memory = memory
        return None

# Derived class from computer:
class WireLess(Computer):

    def __init__(self : any, memory : float, speed : float) -> None:
        """The initializer method adds attributes for wireless devices."""
        Computer.__init__(self, memory, speed)
        self.__battery = 0.0
        return None

# Derived class from wireless:
class Phone(WireLess):

    def __init__(self : any, screen : float, battery: float) -> None:
        return None

# Derived class from wireless:
class Tablet(WireLess):

    def __init__(self : any, speed : float, memory : float) -> None:
        """The initializer method retrieves the attributes of its base
        classes and adds two more attributes."""
        WireLess.__init__(self, speed, memory)
        self._brand = ""
        self._screen_size = 0.0
        return None

    def __str__(self : any) -> str:
        format = f"The {self.brand} has a cpu memory of {self.cpu_speed} \
and screen size of {self.screen_size}."
        return format

if __name__ == "__main__":
    ipad = Tablet(100.00, 300.00)
    ipad.brand = "Ipad"
    ipad.cpu_speed = 100
    ipad.battery = 300
    ipad.screen_size = 400
    print(ipad)