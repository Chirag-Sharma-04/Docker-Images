import socket
import subprocess
from time import sleep
from smbus2 import SMBus
from RPLCD.i2c import CharLCD

# Initialize I2C LCD (Adjust address if needed)
I2C_ADDRESS = 0x3f  # Default address for most 16x2 I2C LCDs
lcd = CharLCD('PCF8574', I2C_ADDRESS, cols=16, rows=2)

# Function to get IP address
def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return "No IP"

# Function to get Wi-Fi SSID
def get_ssid():
    try:
        result = subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE, text=True)
        ssid = result.stdout.strip()
        return ssid if ssid else "No SSID"
    except Exception as e:
        return "No SSID"

# Main loop to display IP and SSID
def main():
    last_ssid = ""
    last_ip = ""

    while True:
        ssid = get_ssid()
        ip_address = get_ip_address()

        if ssid != last_ssid or ip_address != last_ip:
            lcd.clear()  # Only clear if there's a change
            lcd.cursor_pos = (0, 0)  # Top row
            lcd.write_string(f" SCORPION ROBOT ")

            lcd.cursor_pos = (1, 0)  # Bottom row
            lcd.write_string(f"IP:{ip_address[:16]}")

            last_ssid = ssid
            last_ip = ip_address

        sleep(1)  # Delay to prevent rapid updates

if __name__ == "__main__":
    main()
