import setuptools

setuptools.setup(
    name='mitochondria',
    python_requires='>=3.7',
    install_requires=[
        'Django',
        'djangorestframework',
        'requests',
        'psycopg2',
        'gunicorn',
        'django-heroku',
        'dj-database-url'
        
    ],
)