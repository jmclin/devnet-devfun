from netmiko import ConnectHandler
from pprint import pprint

# Define device parameters
device = {
    "device_type": "cisco_ios",  # Use "cisco_ios" for Cisco IOX-SE devices
    "host": "devnetsandboxiosxe.cisco.com",
    "username": "admin",
    "password": "C1sco12345"
}

try:
    # Establish SSH connection
    connection = ConnectHandler(**device)
    print("Connection established!")

    # Execute first command: show interface status
    output_1 = connection.send_command("show run interface Gi2 | begin ^interface")  # Adjusted for IOX-SE
    print("\nOutput for 'show run int':")
    pprint(output_1)

    # Execute second command: show ip protocols
    output_2 = connection.send_command("show interface Gi2")  # Another IOX-SE command example
    print("\nOutput for 'show interface':")
    pprint(output_2)

    # Close connection
    connection.disconnect()
    print("\nConnection closed.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
