#!/bin/sh
picom --config ~/.config/picom/picom.conf &
dunst -conf /home/rusito/.config/dunst/dunstrc &
nm-applet &
cbatticon -i standard BAT0 &
volumeicon &
