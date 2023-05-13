python3.7 -m pip install virtualenv
python3.7 -m venv venv

source venv/bin/activate
pip install --upgrade pip
pip install --upgrade Pillow
pip install -r requirements.txt


python app/main.py
echo 'Paste The link in a new edge tab'
