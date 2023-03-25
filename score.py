import colorama
import openai
import os
import sys
from colorama import Fore

#Initialize colorama
colorama.init(autoreset=True)
openai.api_key = os.getenv("OPENAI_API_KEY","")

import csv

def get_green_score():
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


def get_optimized_code(file_data):
    print(Fore.BLUE + ".......Generating Memory Efficient Code Snippet......")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Provide a memory efficient alternative for following code snippet without removing any library: \n\n {}".format(file_data),
        temperature=0.9,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    print(Fore.GREEN + response["choices"][0]["text"])
    with open('src/algo_optimized.py', 'w') as f:
        f.write(response["choices"][0]["text"])

if __name__ == "__main__":
    get_green_score()
    if len(sys.argv) > 1:
        if sys.argv[1] == "--optimize":
            file = open("src/algo.py", "r")
            get_optimized_code(file.read())
