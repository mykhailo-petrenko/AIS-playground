# AIS receive & decode playground

## Prerequisites
- Compile / Install `AIS-catcher`
- Python 3

## Reception
- Resonant Antenna 162 mhz (http://dl2kq.de/ant/3-78.htm)
- rtl-sdr or another sdr receiver.
- run `AIS-catcher  -gm lna AUTO vga 12 mixer 12 -u 127.0.0.1 5005`

## Decode
- `pip install pyais`
- `python3 udp.py`

## Links
- https://github.com/jvde-github/AIS-catcher
- https://gpsd.gitlab.io/gpsd/AIVDM.html
- https://github.com/M0r13n/pyais
- http://dl2kq.de/ant/3-78.htm