update: makemigrations migrate

run:
	python3 manage.py runserver --settings=config.settings.local

makemigrations:
	python3 manage.py makemigrations --settings=config.settings.local

migrate:
	python3 manage.py migrate --settings=config.settings.local

test:
	python3 manage.py test --settings=config.settings.local
