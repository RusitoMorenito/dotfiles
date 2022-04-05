#!/usr/bin/env python3
import json
import urllib.request

def myround (val, r=2):
  """
  Converts a string of float to rounded string
  @param {String} val, "42.551"
  @param {int} r, the decimal to round
  @return {string} "42.55" if r is 2
  """
  return "{:.{}f}".format(float(val), r)

with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=XXBTZEUR,XLMEUR,XTZEUR,XETHZEUR") as url:
    data = json.loads(url.read().decode())
    str = "₿ " + myround(data['result']['XXBTZEUR']['a'][0]) + "€ "
    str += "ﲹ " + myround(data['result']['XETHZEUR']['c'][0], 4) + "€"
    print(str, end='')

