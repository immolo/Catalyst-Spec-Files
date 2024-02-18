#!/bin/sh

for cmd in $(getcmdline); do
	if [ $cmd = "dokeymap" ]; then
		dokeymap=1
	fi
done
