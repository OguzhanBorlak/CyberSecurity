import subprocess
import optparse
import re

def get_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()

def changemac(user_interface,user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac Changer started. ")

(user_input,arguments) = get_input()
changemac(user_input.interface,user_input.mac_address)
final_mac = control(str(user_input.interface))


if final_mac == user_input.mac_address:
    print("Success")
    print("New mac address: "+user_input.mac_address)
else: print("Error")