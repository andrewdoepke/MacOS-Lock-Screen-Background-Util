#!/bin/bash
rm /Library/Caches/'Desktop Pictures'/DFB3ED3E-AAE7-4C3E-A7D6-CA825E2A9F09/lockscreen.png
cp $1 lockscreen.png
cp lockscreen.png /Library/Caches/'Desktop Pictures'/DFB3ED3E-AAE7-4C3E-A7D6-CA825E2A9F09
rm lockscreen.png
echo "Set Successfully"