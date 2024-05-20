class Vehicle:
    
    def __init__(self, wheel_size, wheel_number): #These instances initialize with a wheel size and number.
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
        
    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"    
