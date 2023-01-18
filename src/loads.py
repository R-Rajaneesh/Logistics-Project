# Imports

import json

import random

from tabulate import tabulate

from pick import pick

# File Imports

from src.stations import loading_station


def loads(profile_id, vehicle):

    database = {}

    with open("./storage.json", "r") as database_file:

        database = json.load(database_file)

        database_file.close()

    stations = ["Chennai", "Puducherry", "Vellore", "Tiruchirapalli", "Salem",
                "Madurai", "Thanjavur", "Coimbatore"]

    station_check_title = "Select your city"

    station, index = pick(stations, station_check_title, default_index=0, indicator="")

    profile = {}

    for prfp in database["profiles"]:

        if prfp["profile_id"] == profile_id:

            profile = prfp

    vehicles = []

    for v in profile["vehicles"]:

        vehicles.append([v["name"], v["id"], v["type"], v["load_size"]])

    print()

    print("Your vehicles")

    print()

    print(tabulate(vehicles, headers=["Name", "ID", "Type", "Max Load"]))

    print()

    vehicle_id = input("Enter your vehicle id: ")

    for order in profile["orders"]:

        if order["vehicle_id"] == vehicle_id:

            print()

            print("This vehicle has already taken an order")

            print()

            vehicle_id = input("Enter your vehicle id: ")

    current_station = loading_station(station)

    if (current_station.get("code") == 400):

        print()

        print("Error accessing your location")

        exit(1)

    print()

    print(f"Goods on station {current_station['goods']}")

    print()

    vehicle_type = vehicle["type"]

    load_size = vehicle["load_size"]

    nearest_stations = current_station["nearest_stations"]

    station_capacity = current_station["goods"]

    max_vehicle_load = load_size

    current_load = int(input("Enter the number of goods to load: "))

    while current_load > max_vehicle_load or current_load > station_capacity:

        print()

        print("Cannot load goods more than the current capacity or can load more goods from a station")

        print()

        current_load = int(input("Enter the number of goods to load: "))

    if current_load > station_capacity:

        print()

        print(
            f"Unable to load {current_load}, station only had {station_capacity}")

        print()

        current_load = station_capacity

        print(f"Loaded {current_load} into vehicle")

        station_goods_left = 0

    else:

        station_goods_left = station_capacity - current_load


    if max_vehicle_load != current_load or max_vehicle_load > current_load:

        print()

        load_more_goods = input("Would you like to pick up more goods from the next nearest location (y/N): ")

        print()

        if load_more_goods.lower() == "y":

            next_station = random.choices(nearest_stations)[0]

            stations.remove(next_station)


    stations.remove(station)

    destination_station = random.choices(stations)[0]

    print(f"Your destination station {destination_station}")

    print()

    order = {

        "vehicle_id": vehicle_id,

        "working_on_order": True,

        "last_pickup_station": station,

        "goods_loaded": current_load,

        "destination_station": destination_station
    }

    profile["orders"].append(order)

    print()

    # Update the latest data

    with open("./storage.json", "w") as db:

        database["stations"][station]["goods"] = station_goods_left

        db.write(json.dumps(database))

        db.close()

    return
