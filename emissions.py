# --- Helper Functions for Input Validation ---
def get_float_input(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val < 0:
                print("Please enter a positive number.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val < 0:
                print("Please enter a positive integer.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        print("Please answer Yes or No.")
# ---------------------------------------------

def calculate_vehicle_distances_km(VehicleDistance, VehicleDistance_in_km):
    # VehicleDistance = list of distances
    # VehicleDistance_in_km = list of booleans: True if in km, False if in miles
    emissions = []
    for i, dist in enumerate(VehicleDistance):
        km = dist if VehicleDistance_in_km[i] else dist * 1.609
        emissions.append(km)  # placeholder, you can multiply by emission factor later
    return emissions


def calculate_recycling_score(Recyclescale):
    # Example: higher score = more recycling, reduce methane
    # Just sum the scores
    return sum(Recyclescale)


