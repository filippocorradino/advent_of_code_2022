#!/usr/bin/bash

set -eu

for f in ./day*.py
do
  echo -n "$f "
  python -m cProfile $f | grep primitive | awk '{print $8,$9}'
done