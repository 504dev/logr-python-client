from setuptools import setup, find_packages

setup(
    name='logrpy',
    version='1.0.4',
    packages=find_packages(),
    install_requires=[
        'pycryptodome',
        'colorama',
        'psutil',
    ],
    url='https://github.com/504dev/logr-python-client',
    py_modules=['logrpy'],
    package_dir={'': 'src'},
    include_package_data=True,
    author='Kozhurkin Dima',
    author_email='kozhurkin.dima@gmail.com'
)
