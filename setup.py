from setuptools import setup, find_packages
setup(
    name="Speed Engine",
    version="1.0.0",
    packages=find_packages(),
    install_requires=['click'],
    extra_require={
        "sqlite":[],
        "mysql":["mysql-connector-python"],
        "postgresql":["psycopg2"],
        "mssql":["pyodbc"],
        "mongodb":["pymongo"]
    },
    description="A cutting edge python database engine with an ORM optimized for speed and flexibility",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Verkyav Peter",
    author_email="verkyavpeter@gmail.com",
    url="https://github.com/cleancodelover/speed-engine.git",
    entry_points={
        "console_scripts":[
            "speed-engine=speed_engine.cli:cli"
        ]
    }
)