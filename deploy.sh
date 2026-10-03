#!/bin/bash
cd /home/profesor/mfis/

echo 'Running on date'
date

#echo 'Pulling master branch'
#git pull origin master

echo 'Building project'
bundle exec jekyll build

echo 'Running MFIS site on port 4000'
JEKYLL_ENV=production bundle exec jekyll serve --host mfis.dc.exa.unrc.edu.ar --port 4000 &

echo 'Done!'
echo ''
