# the fixed steps required to enter the virtual environment
source ~/.profile
workon cv
cd /home/pi/Downloads/Smart-Security-Camera-master

# executing the required python scripts
python camclick.py
python livefeed.py
