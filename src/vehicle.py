# Imports

import random

import string

from pick import pick

import json

# File imports

from src.loads import loads

# Main Function


def vehicle(profile_id):

    database = {}

    with open("./storage.json", "r") as data:

        database = json.load(data)

        profiles = database["profiles"]

        profile = {}

        for Profile in profiles:

            if Profile["profile_id"] == profile_id:

                profile = Profile



    if len(profile["vehicles"]) == 0:

        title = "Please choose vehicle type "

        options = ["Mini", "Small", "Semi", "Large", "Big Mac", "Road Train", ]

        load_sizes = {

            "Mini": 40,

            "Small": 70,

            "Semi": 110,

            "Large": 160,

            "Big Mac": 250,

            "Road Train": 500

        }

        vehicle_type, index = pick(
            options, title, indicator="", default_index=0, multiselect=False)


        vehicle_name = input("Enter a name for your vehicle: ")

        # Generating a random string as vehicle id

        digits = random.choices(string.digits, k=2)

        letters = random.choices(string.ascii_uppercase, k=9)

        vehicle_id = random.sample(digits + letters, 11)

        vehicle_id_str = ""

        for id_char in vehicle_id:

            vehicle_id_str += id_char

        vehicle = {

            "name": vehicle_name,

            "type": vehicle_type,

            "id": vehicle_id_str,

            "load_size": load_sizes[vehicle_type]

        }

        profile["vehicles"].append(vehicle)

        for Profile in profiles:

            if Profile["profile_id"] == profile_id:

                Profile = profile

        data.close()

    else:

        more_vehicles = input("Do you want to register more vehicles (y/N): ")

        add_more_vehicles = False

        if (more_vehicles.lower() == "y"):

            add_more_vehicles = True

        else:

            add_more_vehicles = False

        while add_more_vehicles:

            title = "Please choose vehicle type "

            options = ["Mini", "Small", "Semi",
                       "Large", "Big Mac", "Road Train", ]

            load_sizes = {

                "Mini": 40,

                "Small": 70,

                "Semi": 110,

                "Large": 160,

                "Big Mac": 250,

                "Road Train": 500

            }

            vehicle_type, index = pick(
                options, title, indicator="", default_index=0, multiselect=False)

            database = {}

            with open("./storage.json", "r") as data:

                database = json.load(data)

                profiles = database["profiles"]

                profile = {}

                for Profile in profiles:

                    if Profile["profile_id"] == profile_id:

                        profile = Profile

                vehicle_name = input("Enter a name for your vehicle: ")

                # Generating a random string as vehicle id

                digits = random.choices(string.digits, k=2)

                letters = random.choices(string.ascii_uppercase, k=9)

                vehicle_id = random.sample(digits + letters, 11)

                vehicle_id_str = ""

                for id_char in vehicle_id:

                    vehicle_id_str += id_char

                vehicle = {

                    "name": vehicle_name,

                    "type": vehicle_type,

                    "id": vehicle_id_str,

                    "load_size": load_sizes[vehicle_type]

                }

                profile["vehicles"].append(vehicle)

                for Profile in profiles:

                    if Profile["profile_id"] == profile_id:

                        Profile = profile

                data.close()

                more_vehicles = input(
                    "Do you want to register more vehicles (y/N): ")

                if (more_vehicles.lower() == "y"):

                    add_more_vehicles = True

                else:

                    add_more_vehicles = False

    with open("./storage.json", "w") as db:

        db.write(json.dumps(database))

        db.close()

    return loads(profile_id, vehicle)
