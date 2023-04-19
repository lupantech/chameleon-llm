mkdir images
cd images

wget https://scienceqa.s3.us-west-1.amazonaws.com/images/train.zip
unzip -q train.zip
rm train.zip

wget https://scienceqa.s3.us-west-1.amazonaws.com/images/val.zip
unzip -q val.zip
rm val.zip

wget https://scienceqa.s3.us-west-1.amazonaws.com/images/test.zip
unzip -q test.zip
rm test.zip
