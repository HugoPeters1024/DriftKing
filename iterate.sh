#!/bin/bash
alpha=0.0
for i in {0..10}
do
  echo "Execute with pivot $i and alpha $alpha."
  pipenv run python run.py $alpha $i
done
