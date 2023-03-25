import datetime
import colorama
from colorama import Fore, Back, Style

#Initialize colorama
colorama.init(autoreset=True)
import csv

# opening the CSV file
with open('emissions.csv', mode='r') as file:
    # reading the CSV file
    csv_file = csv.reader(file)
    next(csv_file, None)

    # Proportion of renewable energy in the power grid
    renewable_proportion = 0.3

    # Carbon dioxide emission factor of the region (kg CO2/kWh)
    co2_factor = 0.5
    duration = 0
    energy = 0
    emissions = 0
    emission_rate = 0

    # displaying the contents of the CSV file
    for lines in csv_file:
        timestamp = lines[0]
        duration += float(lines[3])
        energy += float(lines[12])
        emissions += float(lines[4])
        emission_rate += float(lines[5])

    print(f"{Fore.GREEN}TimeStamp: {timestamp}")
    print(f"{Fore.GREEN}Duration: {round(duration,5)} seconds")
    print(f"{Fore.GREEN}Energy Consumption: {round(energy,5)} W")
    print(f"{Fore.GREEN}Emissions: {round(emissions,5)} kg")
    print(f"{Fore.GREEN}Emission Rate: {round(emission_rate,5)} per second")

    # Estimated energy consumption of the computer running the script in watts
    energy_consumption = energy * 1000

    # Estimated time the script runs in hours
    script_runtime = (duration * 1000)//3600

    # Calculate the energy consumption in kWh
    energy_consumed = energy_consumption * script_runtime / 1000

    # Calculate the greenhouse gas emissions of the energy consumption
    emissions = energy_consumed * co2_factor

    # Calculate the proportion of renewable energy used
    renewable_energy = energy_consumed * renewable_proportion

    # Calculate the green energy score
    green_score = renewable_energy / script_runtime

    # Print the results
    print(f"{Fore.RED}Carbon footprint: {round(emissions,5)} kg CO2")
    print(f"{Fore.GREEN}Green energy score: {round(green_score,5)} kW")
