if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

pip install -r deploy/requirements.txt
echo "Successfully installed requirements.txt"

echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Database migrations started"
python manage.py makemigrations
#python manage.py flush --no-input
python manage.py migrate
echo "Apply database migrations"
# Start server
echo "Starting server"
gunicorn -b 0.0.0.0:8000 --workers=49 --threads=2 conf.wsgi --reload