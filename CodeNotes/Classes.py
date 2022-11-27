"""The program is intended to practice and run class programs."""

numbers : list = list(range(0, 7))
print(numbers)

# Base class:
class Computer:
    
    def __init__(self : any, memory : float, speed : float) -> None:
        """The initializer method adds attributes that electronic 
        devices have."""
        self.__cpu_speed : float = speed
        self.__memory : float = memory
        return None

# Derived class from computer:
class WireLess(Computer):

    def __init__(self : any, memory : float, speed : float) -> None:
        """The initializer method adds attributes for wireless devices."""
        Computer.__init__(self, memory, speed)
        self.__battery : float = 0.0
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
        self._brand : str = ""
        self._screen_size : float = 0.0
        return None

    def __str__(self : any) -> str:
        format : str = f"The {self.brand} has a cpu memory of {self.cpu_speed} \
and screen size of {self.screen_size}."
        return format

if __name__ == "__main__":
    ipad = Tablet(100.00, 300.00)
    ipad.brand : str = "Ipad"
    ipad.cpu_speed : str = 100
    ipad.battery : int = 300
    ipad.screen_size : int = 400
    print(ipad)