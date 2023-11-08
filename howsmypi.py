from termcolor import colored
from yaspin import yaspin
from pyfiglet import Figlet
import requests
import datetime
import psutil
import subprocess
import typer

app = typer.Typer(name="Howsmypi")

# Replace with your RapidAPI key
RAPIDAPI_KEY = "82a65c301fmsh534b79a669546b4p121fe1jsn2584ad7653e7"

# Function to get weather data using the RapidAPI URL
def get_weather(city):
    headers = {
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
    }
    url = f"https://weatherapi-com.p.rapidapi.com/current.json?q={city}"
    response = requests.get(url, headers=headers)
    data = response.json()
    if "current" in data:
        weather_data = data["current"]
        weather_description = weather_data["condition"]["text"]
        temperature = weather_data["temp_c"]
        return f"Weather in {city}: {weather_description}, Temperature: {temperature}°C"
    else:
        return f"Could not fetch weather data for {city}"

def determine_condition(temperature, cpu_usage, memory_usage):
    if "temp=" in temperature:
        temperature = float(temperature.split("=")[1].split("'")[0])
        if temperature < 60:
            temperature_condition = "Cool"
        elif 60 <= temperature < 80:
            temperature_condition = "Moderate"
        else:
            temperature_condition = "Warm"
    else:
        temperature_condition = "Unable to determine condition"

    if cpu_usage < 30:
        cpu_condition = "Low"
    elif 30 <= cpu_usage < 70:
        cpu_condition = "Moderate"
    else:
        cpu_condition = "High"

    if memory_usage < 30:
        memory_condition = "Low"
    elif 30 <= memory_usage < 70:
        memory_condition = "Moderate"
    else:
        memory_condition = "High"


    return f"Temperature: {temperature_condition}, CPU Usage: {cpu_condition}, Memory Usage: {memory_condition}"

# Function to check Raspberry Pi temperature using a Bash command
def get_temperature():
    temperature_command = "vcgencmd measure_temp"
    temperature = subprocess.check_output(temperature_command, shell=True, text=True)
    return temperature.strip()

def get_system_info():
    uname_info = subprocess.check_output("uname -a", shell=True, text=True)
    hostname_info = subprocess.check_output("hostname", shell=True, text=True)
    uptime_info = subprocess.check_output("uptime -p", shell=True, text=True)

    system_info = []
    system_info.append("uname -a:")
    system_info.append(uname_info)
    system_info.append("Hostname:")
    system_info.append(hostname_info)
    system_info.append("Uptime:")
    system_info.append(uptime_info)

    return "\n".join(system_info)

# Function to display the Raspberry Pi logo as ASCII art
def display_pi_logo():
    pi_logo_top = """
       .~.   .~.
      '. \ ' ' / .'"""
    pi_logo_bottom = """
       .~ .~..~.
      : ..''.~. :
     ~ (   ) (   ) ~
    ( : ''..'~' : )
     ~ .~ (   ) ~. ~
      (  : '~' :  ) Raspberry Pi
       '~ .~. ~'
           '~'
          """
    colored_pi_logo_top = colored(pi_logo_top, "green")
    colored_pi_logo_bottom = colored(pi_logo_bottom, "red")
    typer.echo(colored_pi_logo_top)
    typer.echo(colored_pi_logo_bottom)

@app.command()
def main():
    with yaspin(text="Loading...", color="yellow") as sp:
        f = Figlet(font="slant")
        banner = f.renderText("Howsmypi")
        sp.write(banner)

        # Display the Raspberry Pi logo as ASCII art
        display_pi_logo()

        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = get_temperature()
        prague_weather = get_weather("Prague")
        pilsen_weather = get_weather("Pilsen")

        # Get CPU usage and memory usage
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        memory_usage = memory.percent

        # Determine the overall condition based on temperature, CPU, and memory
        condition = determine_condition(temperature, cpu_usage, memory_usage)

        # Get and display system information
        system_info = get_system_info()
        typer.echo(f"Current Date & Time: {current_date_time}")
        typer.echo(f"Raspberry Pi Temperature: {temperature}")
        typer.echo(f"Overall Condition: {condition}")
        typer.echo(f"CPU Usage: {cpu_usage}%")
        typer.echo(f"Memory Usage: {memory_usage}%")
        typer.echo("System Information:")
        typer.echo(system_info)
        typer.echo(prague_weather)
        typer.echo(pilsen_weather)

if __name__ == "_main_":
    app()
