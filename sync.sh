git add game-list.json images pack
git commit -m 'add files'
git push -u origin gh-pages

# 同步s3
aws s3 sync pack s3://games-h5-zip/pack
