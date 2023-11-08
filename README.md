# Howsmypi

Howsmypi is an open-source Python project that provides information about your Raspberry Pi, including temperature, weather, CPU usage, memory usage, and system information. It's designed to be easy to use and customizable to fit your needs.

## Features

- Display Raspberry Pi's temperature.
- Get weather information for a specified city. `Prague and Pislen by default`
- Monitor CPU usage and memory usage.
- Display system information.
- Interactive command-line options using Typer.

## Requirements
- Raspberry pi  `3A/3B/3A+/3B+/4B/5  `or`  Raspberry pi Zero W/Zero 2 W`
- Any linux distro compatiable with Raspberry Pi `(Debian or Ubuntu based ones are recommented)` 
- Python 3
- `termcolor` library (can be installed using `pip3`)
- `yaspin` library (can be installed using `pip3`)
- `pyfiglet` library (can be installed using `pip3`)
- `requests` library (can be installed using `pip3`)
- `datetime` library (can be installed using `pip3`)
- `psutil` library (can be installed using `pip3`)
- `subprocess` library (can be installed using `pip3`)
- `typer` library (can be installed using `pip3`)
- API
- `RapidAPI key for weather data (update 'RAPIDAPI_KEY'in the script or use the default one...)`

## Installation

1. Clone the repository to your Raspberry Pi:

   ```bash
   git clone https://github.com/JarrahDev/Howsmypi.git
