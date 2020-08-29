from setuptools import setup, find_packages

setup(
    name='logrpy',
    version='1.0.8',
    author='Kozhurkin Dima',
    author_email='kozhurkin.dima@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pycryptodome',
        'colorama',
        'psutil',
    ],
    url='https://github.com/504dev/logr-python-client',
    include_package_data=True
)
