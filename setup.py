import setuptools

setuptools.setup(
    name="mitochondria",
    python_requires=">=3.7",
    install_requires=[
        "django",
        "drf_yasg",
        "openapi",
        "djangorestframework",
        "psycopg2",
        "gunicorn",
        "pandas",
        "django-heroku",
        "pytest",
    ],
)
