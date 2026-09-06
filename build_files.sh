
# build_files.sh
echo "BUILD START"
pip install -r requirements.txt
python3.14.2 manage.py collectstatic --no-input --clear