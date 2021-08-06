from pyowm import OWM
from pyowm.utils import config, timestamps

# owm = OWM('7678100b2f98c17be5c133d7086b72d5')
owm = OWM('fdf01c05a5538e7f2b1655bf69cbc5d5')
manager = owm.weather_manager()

observe = manager.weather_at_place('Enugu, NG')
enugu = observe.weather

# print(enugu.temperature('celsius'))

celsius = enugu.temperature('celsius')
for temp, value in celsius.items():
    print(f"{temp} => {value}")
