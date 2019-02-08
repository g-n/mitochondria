import setuptools

setuptools.setup(
    name="mitochondria",
    python_requires=">=3.7",
    install_requires=[
        "Django",
        "djangorestframework",
        "djangorestframework_simplejwt",
        "requests",
        "psycopg2",
        "gunicorn",
    ],
)
