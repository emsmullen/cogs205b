#!/bin/sh

#pull latest changes from repo
git pull origin main

#get data from class repo
wget https://github.com/joachimvandekerckhove/cogs205b-s26/raw/refs/heads/main/modules/02-version-control/files/data.zip -O temp.zip
unzip temp.zip 
dt=$(date '+%Y-%m-%d')
mkdir -p ../data/$dt
mv *csv ../data/$dt

git add ./data/
git add ./scripts/fetch-csvs.sh
git commit -m "added data for $dt and fetch-csvs.sh script"
git push -u origin main

