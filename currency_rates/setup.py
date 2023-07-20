from setuptools import setup, find_packages

setup(
    name='currency_rates',
    version='0.1.0',
    packages=find_packages(),
    py_modules=['currency_rates'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'currency_rates = currency.main:cli',
        ],
    },
)