# For Sub-base Course
thickness_sub_base = float(input("Input the value of thickness of Sub-base in metres: "))
vol_sub_base = 1 * 3.5 * thickness_sub_base
density_sub_base_mix = float(input("Input the value of density of Sub-base Mix in kg per cu.m: "))
wt_sub_base = vol_sub_base * density_sub_base_mix
aggregate_sub_base = float(input("Input the value of aggregate in percent: "))
part_filler_sub_base = (100 - aggregate_sub_base) * wt_sub_base / 100

EF_agg = 1.067
CO2e_sub_base = EF_agg * wt_sub_base

# For Wearing Course
thickness_wearing = float(input("Input the value of thickness of Wearing in metres: "))
vol_wearing = 1 * 3.5 * thickness_wearing
density_wearing_mix = float(input("Input the value of density of wearing mix in kg per cu.m: "))
wt_wearing_mix = vol_wearing * density_wearing_mix
part_bitumen_wearing = float(input("Input the value of Bitumen in percent: "))
aggregate_wearing = (100 - part_bitumen_wearing) * wt_wearing_mix / 100

EF_bit = 11.91
CO2e_wearing = EF_bit * (part_bitumen_wearing * wt_wearing_mix / 100) + EF_agg * (aggregate_wearing)

# For Base Course
thickness_base = float(input("Input the value of thickness of Base Course in metres: "))
vol_base = 1 * 3.5 * thickness_base
density_base_mix = float(input("Input the value of density of Base Mix in kg per cu.m: "))
wt_base_mix = vol_base * density_base_mix
aggregate_base = float(input("Input the value of aggregate in percent: "))
part_filler_base = (100 - aggregate_base) * wt_base_mix / 100

CO2e_base = EF_agg * wt_base_mix

# For Binder Course
thickness_binder = float(input("Input the value of thickness of Binder Mix in metres: "))
vol_binder = 1 * 3.5 * thickness_binder
density_binder_mix = float(input("Input the value of density of Binder Mix in kg per cu.m: "))
wt_binder_mix = vol_binder * density_binder_mix
part_bitumen_binder = float(input("Input the value of Bitumen in percent: "))
aggregate_binder = wt_binder_mix * (100 - part_bitumen_binder) / 100

CO2e_binder = EF_bit * (part_bitumen_binder * wt_binder_mix / 100) + EF_agg * (aggregate_binder)

prime_coat = 3.33  # in tonne
tack_coat = 10.36  # in tonne

total_CO2e = CO2e_base + CO2e_binder + CO2e_sub_base + CO2e_wearing + prime_coat + tack_coat
print(f"The total CO2 emission in tonne is: {total_CO2e}")
