# Imports

def loading_station(station):

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

    if (station not in stations):

        return {"code": 400, "error": "Location not found"}

    location = stations[station]

    return location
