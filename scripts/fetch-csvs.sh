#!/bin/sh

#pull latest changes from repo 
git pull origin main

#make temp dir to extract zip file into
mkdir temp_for_zip_extract

#get data from class repo
wget https://github.com/joachimvandekerckhove/cogs205b-s26/raw/refs/heads/main/modules/02-version-control/files/data.zip -O temp.zip

#unzip the file into the temp dir
unzip temp.zip -d temp_for_zip_extract

#get the date and make a new directory in data with that date, then move the csv files into that directory and remove the temporary directory and zip file
dt=$(date '+%Y-%m-%d')
mkdir -p data/$dt
mv temp_for_zip_extract/*csv ../data/$dt
rm -r temp_for_zip_extract temp.zip

git add ./data/ ./scripts/fetch-csvs.sh
git commit -m "added data for $dt and fetch-csvs.sh script"
git push -u origin main

