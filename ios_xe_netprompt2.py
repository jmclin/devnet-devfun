from netmiko import ConnectHandler
from pprint import pprint
import getpass

# Prompt user for hostname and interface
hostname = input("Enter the hostname or IP address: ")
interface = input("Enter the interface (e.g., Gi2): ")
password = getpass.getpass(prompt="Enter your password: ")
# Define device parameters
device = {
    "device_type": "cisco_ios",  # Use "cisco_ios" for Cisco IOX-SE devices
    "host": hostname,
    "username": "admin",
    "password": password
}

try:
    # Establish SSH connection
    connection = ConnectHandler(**device)
    print("Connection established!")

    # Execute first command: show running config for the given interface
    output_1 = connection.send_command(f"show run interface {interface} | begin ^interface")
    print(f"Output for 'show run int {interface}':")
    pprint(output_1)

    # Execute second command: show interface details
    output_2 = connection.send_command(f"show interface {interface} | include Description|CRC|RX|TX|error|discard|Last")
    print(f"Output for 'show interface {interface}':")
    pprint(output_2)

    # Close connection
    connection.disconnect()
    print("Connection closed.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
