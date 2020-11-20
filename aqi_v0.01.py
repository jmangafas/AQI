import requests
import json
from colorama import init
from colorama import Fore, Back, Style
from os import system, name
from time import sleep

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def world_aqi(url):

    #while True:
        try:
            init(autoreset=True)

            resp = requests.get(url)
            data = resp.json()

            city_aqi = data['data']['aqi']
            city_name = data['data']['city']['name']


            if city_aqi <= 50:
                category = (Fore.LIGHTGREEN_EX +'Good')
                warning = (Fore.GREEN +" Enjoy your day!")
            elif city_aqi <= 100:
                category = (Fore.GREEN +'Moderate')
                warning = (Fore.GREEN +" Enjoy your day!")
            elif city_aqi <= 150:
                category = (Fore.LIGHTYELLOW_EX +'Unhealthy for sensitive groups')
                warning = (Fore.LIGHTYELLOW_EX +" You should consider staying indoors today")
            elif city_aqi <= 200:
                category = (Fore.YELLOW +' Unhealthy')
                warning = (Fore.YELLOW + " Please avoid this location today")
            elif city_aqi <= 300:
                category = (Fore.LIGHTRED_EX +'Very Unhealthy')
                warning = (Fore.LIGHTRED_EX + " Stay away from this location today")
            else:
                category = (Fore.RED +'Hazardous')
                warning = (Fore.LIGHTRED_EX + " The AQI is dangerous here!")



            print('\n\n','==========================')
            print('  Air Quality Index App')
            print(' ==========================')
            print('\n', f'The closest sensor is {city_name} and the AQI for {url1} is {city_aqi} which is considered {category}.')
            print(warning)
            print('\n'' How to interpret the AQI score?')
            print(Fore.LIGHTGREEN_EX +' 0 - 50, Good')
            print(Fore.GREEN +' 51 - 100, Moderate')
            print(Fore.LIGHTYELLOW_EX +' 101 - 150, Unhealthy for sensitive groups')
            print(Fore.YELLOW +' 151 - 200, Unhealthy')
            print(Fore.LIGHTRED_EX +' 201 - 300, Very Unhealthy')
            print(Fore.RED +' 300 and up, Hazardous')

        except:
            print("Sorry, the city was not found.")


while True:
    try:
        url1 = input('\n' "Enter a city name: ")
        url2 = "https://api.waqi.info/feed/"
        url3 = "/?token=83aa82912f08eb427756e3bb9993c56d28f65961"
        #location_ip = "https://api.waqi.info/feed/here/?token=83aa82912f08eb427756e3bb9993c56d28f65961"
        #url = "https://api.waqi.info/feed/randwick/?token=83aa82912f08eb427756e3bb9993c56d28f65961"
        #geo = "https://api.waqi.info/feed/geo:-33.86;151.20/?token=83aa82912f08eb427756e3bb9993c56d28f65961"
        # lat long example - https://api.waqi.info/feed/geo:10.3;20.7/?token=demo
        url = url2 + url1 + url3
        world_aqi(url)
        sleep(3)
        clear()
    except (KeyboardInterrupt, SystemExit):
        print("\n\nExiting program.......\n")
        break
        #raise - the key word "raise" means to print out the traceback error for troubleshooting purposes.
