import os
import json
import psutil
import urllib.request
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne


# SYSTEM INFO
# Uptime
uptime = os.popen('uptime -p').read()[3:-1]
uptime_stripped = uptime[:uptime.index(',')]

# Free RAM in MB
ram_mb = int(psutil.virtual_memory().available) / 1024 / 1024
ram_mb_str = str(round(ram_mb, 2)) + "MB"

# Temperature in C
temp = round(psutil.sensors_temperatures().get('cpu_thermal')[0].current, 1)
temp_str = str(temp) + "C"

# Disk space in GB
disk = psutil.disk_usage('/').free
disk_gb = round(disk / 1024 / 1024 / 1024, 2)
disk_str = str(disk_gb) + "GB"

# Pi-hole API data
try:
    with urllib.request.urlopen('http://192.168.1.220/admin/api.php') as f:
        parsed_json = json.loads(f.read())
        ads_blocked = parsed_json['ads_blocked_today']
        ratio_blocked = parsed_json['ads_percentage_today']
        status = parsed_json['status']
except Exception:
    status = 'disabled'

# Initialise Inky pHAT display
small_font = ImageFont.truetype(FredokaOne, 16)
large_font = ImageFont.truetype(FredokaOne, 40)
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

if status != 'enabled':
    draw.text((20, 5), "Pi-hole", inky_display.RED, large_font)
    draw.text((20, 45), "is down :(", inky_display.RED, large_font)
else:
    # Draw ads blocked
    ads_text = str(ads_blocked) + " (" + str(
            "%.1f" % round(ratio_blocked, 2) + "%)"
            )
    draw.text((5, 2), "Ads blocked:", inky_display.BLACK, small_font)
    draw.text((110, 2), ads_text, inky_display.RED, small_font)

    # Draw uptime
    draw.text((5, 22), "Uptime:", inky_display.BLACK, small_font)
    draw.text((110, 22), uptime_stripped, inky_display.RED, small_font)

    # Draw RAM
    draw.text((5, 42), "RAM (free):", inky_display.BLACK, small_font)
    draw.text((110, 42), ram_mb_str, inky_display.RED, small_font)

    # Draw disk space
    draw.text((5, 62), "Disk Space:", inky_display.BLACK, small_font)
    draw.text((110, 62), disk_str, inky_display.RED, small_font)

    # Draw temperature
    draw.text((5, 82), "Temp:", inky_display.BLACK, small_font)
    draw.text((110, 82), temp_str, inky_display.RED, small_font)

inky_display.set_image(img)
inky_display.show()
