""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SERVER = 'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'wifi_ssid'
WIFI_PASS = 'wifi_pass'

# for EU868
LORA_FREQUENCY = 868300000
#LORA_FREQUENCY = 868500000
#LORA_FREQUENCY = 868700000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5
