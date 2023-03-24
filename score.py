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

    # displaying the contents of the CSV file
    for lines in csv_file:
        print(Fore.GREEN + "TimeStamp: " + lines[0])
        print(Fore.GREEN + "Duration: " + lines[3] + " seconds")
        print(Fore.GREEN + "Energy Consumption: " + lines[12] + " W")
        print(Fore.GREEN + "Emissions: " + lines[4] + " kg")
        print(Fore.GREEN + "Emission Rate" + lines[5] + " per second")

        # Estimated energy consumption of the computer running the script in watts
        energy_consumption = float(lines[12]) * 1000

        # Estimated time the script runs in hours
        script_runtime = (float(lines[3]) * 1000)//3600

        # Proportion of renewable energy in the power grid
        renewable_proportion = 0.3

        # Carbon dioxide emission factor of the region (kg CO2/kWh)
        co2_factor = 0.5

        # Calculate the energy consumption in kWh
        energy_consumed = energy_consumption * script_runtime / 1000

        # Calculate the greenhouse gas emissions of the energy consumption
        emissions = energy_consumed * co2_factor

        # Calculate the proportion of renewable energy used
        renewable_energy = energy_consumed * renewable_proportion

        # Calculate the green energy score
        green_score = renewable_energy / script_runtime

        # Print the results
        print(Fore.RED + f"Carbon footprint: {emissions} kg CO2")
        print(Fore.GREEN + f"Green energy score: {green_score} kW")
