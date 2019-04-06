#!/bin/bash
alpha=0.025
for i in {29..30}
do
  pipenv run python run.py $alpha $i
done
