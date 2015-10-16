
from setuptools import setup, find_packages

setup(
    name='struct_bench',
    version='0.1',
    author='androm3da',
    author_email='foo@example.com',
    packages=find_packages(),
    url='http://example.com/',
    license='MIT',
    description='TBD',
    long_description='''TBD''',
    install_requires=[
        'cffi >= 1.1',
    ],
#    extras_require={
#        'test': [
#            'tox',
#        ]
#    }
)
