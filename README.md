# System Monitoring Automation Script

## Features
This script monitors the system's CPU usage, memory usage, and disk usage, and logs the monitoring data to a log file `system_monitor.log`.

## Usage
1. Download the script to your local machine.
2. Run the script:
    ```sh
    python system_monitor.py
    ```
3. Monitoring data will be recorded in the `system_monitor.log` file, updated every 60 seconds.

## Stopping the Script
To manually stop the script while it is running in the terminal or command line, press `Ctrl + C`. The script will gracefully stop and log the stop information to the log file.

## Notes
- Ensure the `psutil` library is installed. You can install it using the following command:
    ```sh
    pip install psutil
    ```
- The log file will be saved in the same directory as the script. Make sure there is enough disk space.
# system_monitor_python
system_monitor_python
