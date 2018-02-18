from setuptools import setup, find_packages

setup(
    name='tic-tac-toe',
    version='0.0.1',
    description='Learning by creating a tic-tac-toe game',
    url='https://github.com/alysivji/tic-tac-toe',
    author='Aly Sivji',
    author_email='alysivji@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests', ]),
    install_requires=[''],
    download_url='https://github.com/alysivji/tic-tac-toe',
)
