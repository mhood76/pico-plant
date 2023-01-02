import network
from time import sleep
from pico_secrets import wifi_ssid, wifi_password


def connect_network():
    #Connect to WLAN
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(wifi_ssid, wifi_password)
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)
        ip = wlan.ifconfig()[0]
        print(f"Connected on {ip}")
    except KeyboardInterrupt:
        machine.reset()
    return ip

def disconnect_network():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        print(f"Network Connection Status: {wlan.isconnected()}")
        print(f"Disconnecting on: {wlan.ifconfig()[0]}")
        while wlan.isconnected() == True:
            wlan.disconnect()
        print(f"Network Connection Status: {wlan.isconnected()}")

    else:
        print("Wifi was not enabled")
        