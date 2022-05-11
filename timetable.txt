import time

print("ck tedam university of tech. and applied sci. timetable portal.".upper())
print(time.strftime("%B %d,%Y %I:%M:%S %p\n%A"))
print("*" * 65)

available_time = ["7AM - 9AM", "9:10AM - 10:10AM", "11AM - 1PM", "1:30PM - 2:30PM", "3PM - 5PM", "6PM - 7PM",
                  "5:15PM - 7:15PM", "7:20PM - 8:20PM"]

halls = {
    "NH1": {
        "capacity": 200,
        "available_time": "7AM - 9AM",
        "occupied": True,
        "course": "CSC 201"
    },
    "NH2": {
        "capacity": 150,
        "available_time": "5:15PM - 7:15PM",
        "occupied": True,
        "course": "CSC 101"
    },
    "NHA1": {
        "capacity": 160,
        "available_time": "",
        "occupied": False,
        "course": ""
    },
    "NHA2": {
        "capacity": 80,
        "available_time": "",
        "occupied": False,
        "course": ""
    },
    "NHA3": {
        "capacity": 50,
        "available_time": "",
        "occupied": False,
        "course": ""
    },
    "NHA4": {
        "capacity": 10,
        "available_time": "",
        "occupied": False,
        "course": ""
    },
    "NHA5": {
        "capacity": 80,
        "available_time": "",
        "occupied": False,
        "course": ""
    },
    "NGF1": {
        "capacity": 100,
        "available_time": "1:30PM - 2:30PM",
        "occupied": True,
        "course": "STS 203"
    },
    "NGF2": {
        "capacity": 30,
        "available_time": "",
        "occupied": False,
        "course": ""
    }

}
print()

print("\navailable halls".upper())
print("-" * 30)
for hall in halls:
    assigned_hall = halls[hall]
    if not assigned_hall["occupied"]:
        print(f"{hall} |", end=" ")
print("\n")

# print("available times".upper())
# print("-" * 30)
# for hall in halls.keys():
#     assigned_hall = halls[hall]
#     for times in available_time:
#         if assigned_hall["available_time"] != available_time.iter():
#             print(f"{times} |", end=" ")
#         else:
#             pass

print("\noccupied halls".upper())
print("-" * 30)
for hall in halls:
    assigned_hall = halls[hall]
    if assigned_hall["occupied"]:
        print(f"{hall} |", end=" ")

print()
print("\nAlready assigned courses and time".upper())
print("-" * 30)
print()
print("course  | time".upper())
print("-" * 20)
for hall in halls.keys():
    detail = halls[hall]
    if detail.get("course") != "":
        print(f"{detail['course']} |", end=" ")
        print(f"{detail['available_time']}")

print()

hall_name = input("\nEnter name of hall (example NH1): ").upper()

if hall_name in halls.keys():
    assign_hall = halls[hall_name]
    if not assign_hall.get("occupied"):
        print(f"{hall_name} is available")
        print(f"Capacity: {assign_hall['capacity']}")
        print("Space: Free")
        class_capacity = int(input("Enter class capacity: "))
        if assign_hall.get("capacity") >= class_capacity:
            print(f"{hall_name} can contain {class_capacity}.")
            course = input("Enter course code: ").upper()
            assign_hall["course"].replace("", course)
            assign_hall["occupied"] = True
            desired_time = input("Enter time for lecture: ")
            if desired_time.upper() in available_time and not assign_hall["available_time"]:
                assign_hall["available_time"].replace("", desired_time)
                print(f"{course} successfully assigned to {hall_name}")
                print()
                print("     H A L L     D E T A I L S")
                print("-" * 35)
                print("COURSE   |     TIME     | HALL | CAPACITY")
                print(f"{course}   |  {desired_time.upper()}  | {hall_name} | {assign_hall['capacity']}")
            elif assign_hall.get("available_time") == desired_time.upper():
                print(f"Error, {desired_time} already assigned.")

        elif assign_hall.get("capacity") < class_capacity:
            print(f"Error, {class_capacity} is more than hall capacity ({assign_hall['capacity']})")
            print(f"Please find different hall that can contain {class_capacity} students.")
        else:
            pass
    elif assign_hall["occupied"]:
        print(f"{hall_name} hall is already occupied.")
    else:
        pass
elif hall_name not in halls.keys():
    print("Sorry, No such hall found, please enter the right hall name (example NGF1)")
