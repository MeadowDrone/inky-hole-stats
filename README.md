# Inky Hole Stats

Derived from [neauoire's Inky Hole](https://github.com/neauoire/inky-hole).

Display the **number of blocked requests, and filtered traffic** from [Pi-Hole](https://pi-hole.net) along with current system uptime, RAM, disk space and temperature, on [Pimoroni's Inky-Phat](https://github.com/pimoroni/inky-phat/issues).

<img src='https://raw.githubusercontent.com/MeadowDrone/inky-hole-stats/master/stats.jpg?v=1' width="600"/>

- Setup **Pi-Hole**, follow the [installation instructions](https://learn.adafruit.com/pi-hole-ad-blocker-with-pi-zero-w/install-pi-hole).
- Setup **InkyPhat**, follow the [installation instructions](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat).
- Clone this repo on your [Raspberry Pi Zero W](https://www.raspberrypi.org/products/).

## Reload automatically every 30 minutes

Edit `crontab`. 

```
crontab -e
```

Add the following line:

```
*/30 * * * * python /home/pi/inky-hole/main.py
```

Enjoy!