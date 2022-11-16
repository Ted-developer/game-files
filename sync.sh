git add game-list.json images pack
git commit -m 'add files'
git push -u origin gh-pages

# 同步s3
aws s3 sync pack s3://games-h5-zip/pack

# 同步cos
coscli sync pack cos://global/pack -r
coscli sync images cos://global/images -r
