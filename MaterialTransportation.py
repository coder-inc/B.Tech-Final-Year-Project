hauling_dist = float(input("Input the value of the hauling Distance in Km: "))
vol_CA = 731.19  # m3
vol_FA = 413.75  # m3
vol_bitumen = 41970  # Litres
vol_filler = 49.4  # m3
capacity_of_plant_agg = 4.56  # m3
capacity_of_plant_bitumen = 10000  # Litres

total_dist_CA = (vol_CA / capacity_of_plant_agg) * 2 * hauling_dist  # CA in km
print(total_dist_CA)

total_dist_FA = (vol_FA / capacity_of_plant_agg) * 2 * hauling_dist  # FA in km

total_dist_filler = (vol_filler / capacity_of_plant_agg) * 2 * hauling_dist  # Filler in km

total_dist_bitumen = (vol_bitumen / capacity_of_plant_bitumen) * 2 * hauling_dist  # Bitumen in km

final_distance = total_dist_bitumen + total_dist_CA + total_dist_FA + total_dist_filler

print(f"The Final Distance in Km is: {final_distance} km")

total_fuel_consumption = 0.286 * final_distance  # Litres

total_emission_CO2 = (2.66 * total_fuel_consumption) / 1000  # Tonnes

print(f"The total Emission of CO2 in Material Transportation in tonnes is: {total_emission_CO2} tonnes")
