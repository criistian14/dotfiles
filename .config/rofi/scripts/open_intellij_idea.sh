#!/bin/sh
ls ~/Documents/Projects/ | rofi -show -dmenu | xargs -I_ intellij-idea-ultimate ~/Documents/Projects/_
