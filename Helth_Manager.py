from time import time
from datetime import datetime
from pygame import mixer

print("Welcome to the office Sir/Mam")
print("Please enter your name")
user_name = input().upper()
print("Alarm is valid for 11:00:00 AM to 7:00:00 PM.\n")
d = datetime.now()
store_datetime = d.hour

if 11 <= d.hour < 19:
    print("The alarm has started succesfully.\n")
    print("Alarm will ask you to be ready \nTo drink water every 30 minutes. \nEvery 40 minutes for an eyes workout. \nEvery 50 minutes for an physical exercise.\n")

if 11 <= store_datetime < 19:
    if 11 <= store_datetime:
        print(f"{user_name} alarm has started at {d.hour}:{d.minute}:{d.second} PM {d.date()}\n")
        with open("user_data_am", "a") as user_data_am:
            user_data_am.write(f"{user_name} started alarm at {d.hour}:{d.minute}:{d.second} AM {d.date()} \n")
    else:
        print(f"{user_name} alarm has started at {d.hour}:{d.minute}:{d.second} AM {d.date()}\n")
        with open("user_data_pm", "a") as user_data_pm:
            user_data_pm.write(f"{user_name} started alarm at {d.hour}:{d.minute}:{d.second} PM {d.date()} \n")


def song_loop(file, str):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input = input(f"press '{str}' for stop the music -> ").lower()
        if user_input == str:
            mixer.music.stop()
            print(f"\n{user_name} you have done it.")
            if str == 'drank':
                print(f"{user_name} you drank water succesfully.\n")
            elif str == 'protect':
                print(f"{user_name} you have succesfully done eyes exercise.\n")
            elif str == 'secure':
                print(f"{user_name} you completed your physical exercise.\n")

            break
        else:
            print("\nPress correct value to stop the music.\n")
            continue


water_time = time()
eyes_time = time()
physical_time = time()

if 11 <= d.hour < 19:
    while True:
        dte = datetime.now()
        if 11 <= dte.hour < 19:
            if time() - water_time >= 1800:  # 30min
                print("Drink some water now\n")
                song_loop("water.mp3", "drank")
                water_time = time()
                with open("water.txt", "a") as water:
                    water.write(f"{user_name} drink the water at {datetime.now()}\n")

            elif time() - eyes_time >= 2400:  # 40min
                print("Start eyes exercise\n")
                song_loop("eyes.mp3", "protect")
                eyes_time = time()
                with open("eyes.txt", "a") as eyes:
                    eyes.write(f"{user_name} did the eyes exercise at {datetime.now()}\n")

            elif time() - physical_time >= 3000:  # 50min
                print("Time of physical activity\n")
                song_loop("physical.mp3", "secure")
                physical_time = time()
                with open("physical.txt", "a") as physical:
                    physical.write(f"{user_name} did the physical exrcise at {datetime.now()}\n")

                print("Do you want to exit this alarm")
                print("'y' for exit the alarm 'n' for continue the alarm")
                exit = input("type here y/n-> ").lower()
                print("")
                if exit == "y":
                    print("\nThank you for using vijay's alarm")
                    break
                elif exit == "n":
                    continue
                else:
                    print("Enter correct key to continue the alarm or exit the alarm.\n")
                    print("If you do not press any key,the alarm will remain on. \n")
        else:
            print("This programme is valid from 11:00:00 AM to 7:00:00 PM.")
            break

elif d.hour < 11:
    print("It starts working from 11:00:00 AM")

elif d.hour >= 19:
    print("This programme is valid from 11:00:00 AM to 7:00:00 PM.")
