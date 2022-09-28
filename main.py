import yeelight as ye
import json # Used to pretty print data
import time

# Theoritically we can just use the hostname to get the ip address, but it doesn't seem to resolve on my network
#import socket # Used to resolve hostname to ip address
# Resolve hostname
#ip_addr_1 = socket.gethostbyname("yeelink-light-color4_mibt7AAC")
#print(ip_addr_1)

#print(ye.discover_bulbs(timeout=2))

# discover_bulbs() didn't work so I just looked up the IP address of the bulb in my router's interface and also reserved the IP address for the bulb.
bulb = ye.Bulb(ip="192.168.1.24")

capabilities_dict = bulb.get_capabilities()
model_specs_dict = bulb.get_model_specs()
properties_dict = bulb.get_properties()

# Pretty-print light info
capabilities_pretty = json.dumps(capabilities_dict, indent=4)
model_specs_pretty = json.dumps(model_specs_dict, indent=4)
properties_pretty = json.dumps(properties_dict, indent=4)

print("capabilities:\n",capabilities_pretty)
print("model_specs: \n", model_specs_pretty)
print("properties: \n", properties_pretty)


sleep_interval= 3
bulb.turn_on()

while True: # Loop forever over RGB
    bulb.set_rgb(255, 0, 0) # Red
    time.sleep(sleep_interval)
    bulb.set_rgb(0, 255, 0) # Green
    time.sleep(sleep_interval)
    bulb.set_rgb(0, 0, 255) # Blue
    time.sleep(sleep_interval)
