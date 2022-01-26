class Lightbulb:
    def __init__(self, wattage:int, is_led:bool, brand_name:str, brightness:int, is_on:bool=False):

        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        is_on = True

    def turn_off(self):
        in_on =False

    def to_string(self, wattage, brand_name):
        print(f"Wattage: {wattage}\nBrand: {brand_name}")

    def set_brightness(self):
        brightness = int(input("Enter Brightness(1-10): "))
        return print("bright level is ", brightness)


led_lightbulb = Lightbulb(250,True,"Phillips",1, False)
led_lightbulb.set_brightness()
