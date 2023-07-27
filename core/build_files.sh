echo " BUILD START"
python3.7.9 -m pip install -r requirements.txt
python3.7.9 manage.py collectstatic --noinput --clear
echo " BUILD END"