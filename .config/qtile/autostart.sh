#!/bin/sh
picom --config ~/.config/picom/picom.conf &
dunst -conf /home/rusito/.config/dunst/dunstrc &
nm-applet &
cbatticon -i standard BAT0 &
volumeicon &
nitrogen --restore &
setxkbmap -layout "us,ru" 
setxkbmap -option "grp:alt_shift_toggle,grp_led:scroll" 
