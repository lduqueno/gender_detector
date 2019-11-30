echo 'Downloading requirements..'
pip install -r resources/requirements.txt > /dev/null
echo 'Requirements successfully downloaded!'
echo 'Now create an account on https://www.faceplusplus.com and retrieve your API access. Then, write it in srcs/config.py.'
open srcs/config.py
echo '\nTo launch script, use: python3 srcs/main.py <Image PATH>'
