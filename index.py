# Package imports

import sys

import atexit

import string

import random

import json

# File Imports

from src.vehicle import vehicle

# Main Code

has_reset_index_val = sys.argv.index("--reset")

if sys.argv[has_reset_index_val]:

    stations = {

        "Chennai": {

            "nearest_stations": ["Vellore", "Puducherry"],

            # In tons

            "goods": 15000

        },

        "Puducherry": {

            "nearest_stations": ["Tiruchirapalli", "Thanjavur", "Chennai", "Salem"],

            # In tons

            "goods": 10000

        },

        "Vellore": {

            "nearest_stations": ["Chennai", "Puducherry", "Salem", ],

            # In tons

            "goods": 6000

        },

        "Tiruchirapalli": {

            "nearest_stations": ["Thanjavur", "Salem", "Puducherry", "Madurai", "Coimbatore"],

            # In tons

            "goods": 4000

        },

        "Salem": {

            "nearest_stations": ["Vellore", "Chennai", "Puducherry", "Madurai", "Tiruchirapalli"],

            # In tons

            "goods": 8000

        },

        "Madurai": {

            "nearest_stations": ["Coimbatore", "Thanjavur", "Tiruchirapalli", "Salem"],

            # In tons

            "goods": 12500

        },

        "Thanjavur": {

            "nearest_stations": ["Tiruchirapalli", "Puducherry", "Madurai", "Salem"],

            # In tons

            "goods": 11000

        },

        "Coimbatore": {

            "nearest_stations": ["Salem", "Madurai", "Tiruchirapalli"],

            # In tons

            "goods": 9000

        }

    }

    with open("./storage.json", "w") as db:

        data = {}

        data["stations"] = stations

        data["profiles"] = []

        db.write(json.dumps(data))

        db.close()

        exit(1)

# File imports

# Reading the file

# Loading the file as dict

database: dict[str, list] = {}

with open("./storage.json", "r") as database_file:

    if (database_file == ""):

        database = {}

    else:

        database = json.load(database_file)

    try:

        if database == {}:

            database = {

                "stations": [],

                "profiles": []

            }

    except:

        exit(0)

    database_file.close()


# Generating a random string as profile id

digits = random.choices(string.digits, k=2)

letters = random.choices(string.ascii_uppercase, k=9)

id = random.sample(digits + letters, 11)

id_str = ""

for id_char in id:

    id_str += id_char

# Get or create profile id

has_profile_id = input("Do you have a profile registered (Y/n): ")

if (has_profile_id.lower() == "n"):

    # Set newly created vehicle id

    profile_id = id_str

    print(f"Here is your newly created profile id: {profile_id}")

    database["profiles"].append({

        "profile_id": profile_id,

        "vehicles": [],

        "orders": []

    })

else:

    profile_id = input("Enter your profile id: ")

    has_profile = False

    profiles = database["profiles"]

    for profile in profiles:

        if profile["profile_id"] and profile["profile_id"] == profile_id:

            has_profile = True

        else:

            has_profile = False

    if not has_profile:

        print("Profile not found!")

        exit(1)

updated_database = json.dumps(database)

with open("./storage.json", "w") as database_file:

    database_file.write(updated_database)

    database_file.close()

# Ask for a job application

get_new_job = input("Accept a new job offer? (y/N): ")

new_job = False

if get_new_job.lower() == "y":

    new_job = True

else:

    new_job = False

if not new_job:

    exit(1)

order = vehicle(profile_id)

# Checking if the script is exiting

@atexit.register

def exit_handler():

    print()

    print("End of code")
