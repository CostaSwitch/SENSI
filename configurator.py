import socket
import netifaces
import ipaddress
import re

# Function to find the active network interface
def find_active_interface():
    interfaces = netifaces.interfaces()
    print(f"All interfaces: {interfaces}")
    for interface in interfaces:
        # Ignore the loopback interface
        if interface == 'lo':
            continue

        try:
            if netifaces.AF_INET in netifaces.ifaddresses(interface):
                for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                    if 'addr' in link and 'netmask' in link:
                        print(f"Selected interface: {interface}")
                        return interface
        except ValueError:
            continue

    return None

# Function to update HOME_NET in suricata.yaml
def update_home_net(network_ip):
    with open("/etc/suricata/suricata.yaml", "r") as file:
        lines = file.readlines()
        
    within_address_group = False
    for i, line in enumerate(lines):
        if 'address-groups' in line:
            within_address_group = True
        elif '##END SECTION FOR SCRIPT' in line:
            within_address_group = False
            
        if within_address_group:
            match = re.search(r'HOME_NET:.*', line)
            if match:
                print(f"Old line: {line}")  # Add this line
                lines[i] = re.sub(r'HOME_NET:.*', f'HOME_NET: "[{network_ip}]"', line)
                print(f"New line: {lines[i]}")  # And this line
    
    # Write the entire file out in one go
    with open("/etc/suricata/suricata.yaml", "w") as file:
        file.write("".join(lines))

# Get active interface
interface = find_active_interface()

if interface:
    # Get IP and subnet mask of the active interface
    ip_info = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
    print(f"IP info: {ip_info}")
    ip = ip_info['addr']
    netmask = ip_info['netmask']

    # Calculate network IP
    network_ip = ipaddress.IPv4Network(f'{ip}/{netmask}', strict=False)
    print(f"Network IP: {network_ip}")
    
    # Update HOME_NET in suricata.yaml
    update_home_net(str(network_ip))
else:
    print("No active network interface found.")
