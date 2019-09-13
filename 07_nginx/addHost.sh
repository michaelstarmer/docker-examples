#!/bin/bash

for i in "$@"; do
  args="$args $i"
done

python3 .scripts/addHost.py $args


