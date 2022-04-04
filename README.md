How to install
===============

1. Activate virtualenv with python3
2. Execute:

	
`sudo apt-get install python3-dev default-libmysqlclient-dev`

`sudo apt-get install build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev`

`pip install -r requirements.txt`

3. Migrate database:


`python manage.py migrate`

TEST
====

1. Create fixtures:

`python manage.py dumpdata --format yaml > blog/fixtures/posts.yml`

`python manage.py dumpdata --format xml --indent 3 > blog/fixtures/posts.xml`

`python manage.py dumpdata --indent 3 > blog/fixtures/posts.json`

