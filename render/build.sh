set -o errexit

pip install -r install.txt

python manage.py collectstatic --no-input

python manage.py migrate