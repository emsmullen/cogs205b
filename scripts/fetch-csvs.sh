#!/bin/sh
wget https://github.com/joachimvandekerckhove/cogs205b-s26/raw/refs/heads/main/modules/02-version-control/files/data.zip -O temp.zip
unzip temp.zip 
dt=$(date '+%Y-%m-%d')
mkdir -p ../data/$dt
mv *csv ../data/$dt
git clone ssh://git@github.com:emsmullen/cogs205b.git
git commit -m "added data for $dt and fetch-csvs.sh script"

#git remote add origin 
#git branch -M main
git push -u origin main

