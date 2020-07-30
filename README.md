# Feed My Cats with a Raspberry Pi

## Parts I Use

* Raspberry PI 3
* [RPi Motor Driver Board](https://www.waveshare.com/rpi-motor-driver-board.htm)
* [Trixie Futterautomat TX7 5l](https://www.trixie.de/heimtierbedarf/de/shop/Hund/ErnaehrungBelohnung/FutterWasserautomaten/Futterautomat+TX7/?card=181439)
* Apple TV (optional)

Just gut the logic board and the display of the feeder, its not good at anything.
Connect the motors cables with the board and use the existing power cables
of the feeder to power the Motor board. The Pi 3 itself does not have enough
power for the motor.

I did drill a hole into the back of the feeder to route in the USB power cable.

There is enough space in the feeder to fit the whole Rasperry.

## Feed [via IOS / Apple Watch](cli)

This is what I use. 

Using [Homebride](https://homebridge.io) and the [cmdtriggerswitch](https://github.com/hans-1/homebridge-cmdtriggerswitch) plugin.

Simply install homebridge.io on your Raspberry Pi and install the cmdtriggerswitch plugin.
Configure the plugin like so:

![Plugin Config](/images/plugin.png)

## Feed [via a Browser](flask)

This was done using the CentOS 7 Raspberry image, but since its based on Python
it should work with any version.

Requires Flask and Gunicorn and ideally also a webserver like nginx to front it.

