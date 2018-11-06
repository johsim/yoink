from setuptools import setup

setup(
    name='yoink',
    version='0.1',
    py_modules=['yoink'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        yoink=yoink.cli:cli
    ''',
)
