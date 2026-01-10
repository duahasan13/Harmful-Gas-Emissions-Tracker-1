def calculate_house_emissions(HouseE, PersonalE, HouseG, G_in_kwh, HouseA, Area_in_m2):
    HouseE_adjusted = HouseE - PersonalE

    if not G_in_kwh:
        HouseG = HouseG * 11  # m³ to kWh
    # else: assume already in kWh

    # Total household energy
    HouseT = HouseE_adjusted + HouseG

    HouseA_m2 = HouseA if Area_in_m2 else HouseA * 0.0929

    return HouseT, HouseA_m2

def calculate_vehicle_emissions(VehicleDistance, VehicleDistance_in_km):
    # VehicleDistance = list of distances
    # VehicleDistance_in_km = list of booleans: True if in km, False if in miles
    emissions = []
    for i, dist in enumerate(VehicleDistance):
        km = dist if VehicleDistance_in_km[i] else dist * 1.609
        emissions.append(km)  # placeholder
    return emissions


def calculate_recycling_score(Recyclescale):
    return sum(Recyclescale)
