pipreqs --encoding=utf-8 --force
python manage.py makemigrations
python manage.py migrate

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

python manage.py createsuperuser


python manage.py seed shop --number=150