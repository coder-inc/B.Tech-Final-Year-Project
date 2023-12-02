thicknessBase, thicknessSubBase, thicknessBinder, thicknessWearing = map(float, input("Input the value of thickness of Base Layer, Binder Layer, Sub-Base Layer, Wearing Layer in m: ").split())

volBase = thicknessBase * 3500
volSubBase = thicknessSubBase * 3500
volBinder = thicknessBinder * 3500
volWearing = thicknessWearing * 3500

# Unit of Plant Coefficient is Hour per m3
plantCoBaseWheelLoader, plantCoSubBaseWheelLoader, plantCoBinderWheelLoader, plantCoWearingWheelLoader = 0.061, 0.061, 0.048, 0.002
plantCoBaseDumpTruck, plantCoSubBaseDumpTruck, plantCoBinderDumpTruck, plantCoWearingDumpTruck = 0.292, 0.292, 1.392, 0.105
plantCoBinderTandem, plantCoWearingTandem = 0.028, 0.002
plantCoBinderAMP, plantCoWearingAMP = 0.054, 0.002
plantCoBinderAsphaltFinisher, plantCoWearingAsphaltFinisher = 0.068, 0.003
plantCoBinderRoller, plantCoWearingRoller = 0.021, 0.002
plantCoBaseMotorGrader, plantCoSubBaseMotorGrader = 0.011, 0.011
plantCoBaseVibro, plantCoSubBaseVibro = 0.017, 0.017
plantCoBaseWaterTanker, plantCoSubBaseWaterTanker = 0.021, 0.021

# Wheel Loader
operationalHrWLB = volBase * plantCoBaseWheelLoader
operationalHrWLSB = volSubBase * plantCoSubBaseWheelLoader
operationalHrWLBind = volBinder * plantCoBinderWheelLoader
operationalHrWLW = volWearing * plantCoWearingWheelLoader
totalWL = operationalHrWLB + operationalHrWLBind + operationalHrWLSB + operationalHrWLW

# Fuel Consumption
fuelConsumptionWheelLoader = 2.08 * 3.79 * totalWL  # in Liters

# CO2 Emission due to Wheel Loader in tonnes
CO2eWL = fuelConsumptionWheelLoader * 2.66 / 1000
print("CO2 Emission due to Wheel Loader in tonnes:", CO2eWL)

# Dump Truck
operationalHrDTB = volBase * plantCoBaseDumpTruck
operationalHrDTSB = volSubBase * plantCoSubBaseDumpTruck
operationalHrDTBind = volBinder * plantCoBinderDumpTruck
operationalHrDTW = volWearing * plantCoWearingDumpTruck
totalDT = operationalHrDTB + operationalHrDTBind + operationalHrDTSB + operationalHrDTW

# Fuel Consumption
fuelConsumptionDumpTruck = 5.5 * 3.79 * totalDT

# CO2 Emission due to Dump Truck in tonnes
CO2eDT = fuelConsumptionDumpTruck * 2.66 / 1000
print("CO2 Emission due to Dump Truck in tonnes:", CO2eDT)

# Tandem
operationalHrTBind = volBinder * plantCoBinderTandem
operationalHrTW = volWearing * plantCoWearingTandem
totalT = operationalHrTBind + operationalHrTW

# Fuel Consumption
fuelConsumptionTandem = 4 * 3.79 * totalT

# CO2 Emission due to Tandem in tonnes
CO2eT = fuelConsumptionTandem * 2.66 / 1000
print("CO2 Emission due to Tandem in tonnes:", CO2eT)

# AMP
operationalHrAMPBind = volBinder * plantCoBinderAMP
operationalHrAMPW = volWearing * plantCoWearingAMP
totalAMP = operationalHrAMPBind + operationalHrAMPW

# Fuel Consumption
fuelConsumptionAMP = 4 * 3.79 * totalAMP

# CO2 Emission due to AMP in tonnes
CO2eAMP = fuelConsumptionAMP * 2.66 / 1000
print("CO2 Emission due to AMP in tonnes:", CO2eAMP)

# AsphaltFinisher
operationalHrAFBind = volBinder * plantCoBinderAsphaltFinisher
operationalHrAFW = volWearing * plantCoWearingAsphaltFinisher
totalAF = operationalHrAFBind + operationalHrAFW

# Fuel Consumption
fuelConsumptionAsphaltFinisher = 8.52 * 3.79 * totalAF

# CO2 Emission due to Asphalt Finisher in tonnes
CO2eAF = fuelConsumptionAsphaltFinisher * 2.66 / 1000
print("CO2 Emission due to Asphalt Finisher in tonnes:", CO2eAF)

# Roller
operationalHrRBind = volBinder * plantCoBinderRoller
operationalHrRW = volWearing * plantCoWearingRoller
totalR = operationalHrRBind + operationalHrRW

# Fuel Consumption
fuelConsumptionRoller = 4 * 3.79 * totalR

# CO2 Emission due to Roller in tonnes
CO2eR = fuelConsumptionRoller * 2.66 / 1000
print("CO2 Emission due to Roller in tonnes:", CO2eR)

# MotorGrader
operationalHrMGB = volBase * plantCoBaseMotorGrader
operationalHrMGSB = volSubBase * plantCoSubBaseMotorGrader
totalMG = operationalHrMGB + operationalHrMGSB

# Fuel Consumption
fuelConsumptionMotorGrader = 6 * 3.79 * totalMG

# CO2 Emission due to Motor Grader in tonnes
CO2eMG = fuelConsumptionMotorGrader * 2.66 / 1000
print("CO2 Emission due to Motor Grader in tonnes:", CO2eMG)

# Vibro
operationalHrVB = volBase * plantCoBaseVibro
operationalHrVSB = volSubBase * plantCoSubBaseVibro
totalV = operationalHrVB + operationalHrVSB

# Fuel Consumption
fuelConsumptionVibro = 10.5 * 3.79 * totalV

# CO2 Emission due to Vibro in tonnes
CO2eV = fuelConsumptionVibro * 2.66 / 1000
print("CO2 Emission due to Vibro in tonnes:", CO2eV)

# Water Tanker
operationalHrWTB = volBase * plantCoBaseWaterTanker
operationalHrWTSB = volSubBase * plantCoSubBaseWaterTanker
totalWT = operationalHrWTB + operationalHrWTSB

# Fuel Consumption
fuelConsumptionWaterTanker = 5 * 3.79 * totalWT

# CO2 Emission due to Water Tanker in tonnes
CO2eWT = fuelConsumptionWaterTanker * 2.66 / 1000
print("CO2 Emission due to Water Tanker in tonnes:", CO2eWT)
