from setuptools import find_packages, setup

packages = find_packages()

setup(
    name='TicTacToe8460',
    version='1.0.0',
    description="My first python project.",
    packages=packages,
    install_requires=["PyQt5"]
)
