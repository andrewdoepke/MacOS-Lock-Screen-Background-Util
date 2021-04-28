#!/bin/bash
path=$(ls -d /Library/Caches/'Desktop Pictures'/*)
rm "${path}"/lockscreen.png
cp $1 lockscreen.png
cp lockscreen.png "${path}"
rm lockscreen.png
echo "Set Successfully"