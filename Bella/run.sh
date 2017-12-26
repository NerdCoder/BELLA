#!/bin/sh
python3 manage.py migrate
echo "\nMigration Done!"

python3 manage.py train
echo "\nTraining Done!"

python3 manage.py runserver
echo "\nOpen Chrome!"
