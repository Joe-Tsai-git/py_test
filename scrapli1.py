from scrapli.driver.core import IOSXEDriver

device = {
    "host": "10.0.2.27",
    "auth_username": "python",
    "auth_password": "123",
    "port": 22,
    "auth_strict_key": False,
}

conn = IOSXEDriver(**device)
conn.open()
responses = conn.send_commands(["show clock", "show ip int bri"])

for response in responses:
    print(response.result)
output = conn.send_configs(["interface GigabitEthernet0/1", "description Configured by Scrapli"])
print(output.result)
output = conn.send_command("show interface Gi0/1 description")
print(output.result)
conn.close()