from netmiko import ConnectHandler

username = "<username>"
password = "<login password>"
enable_password = "<secret password>"

with open("devices.txt") as f:
    devices = [line.strip() for line in f]

with open("template.cfg") as f:
    config_commands = f.read().splitlines()

for ip in devices:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
        "secret" : enable_password,
    }

    try:
        print(f"Connecting to {ip}")

        connection = ConnectHandler(**device)
        connection.enable()

        output = connection.send_config_set(config_commands)

        print(output)

        connection.save_config()

        connection.disconnect()

        print(f"{ip} configured successfully\n")

    except Exception as e:
        print(f"{ip} failed: {e}")
