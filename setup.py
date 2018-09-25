# Always prefer setuptools over distutils
from setuptools import setup

# Get the long description from the README file
with open('README.md', 'r', encoding='utf8') as file:
    long_description = file.read()

setup(
    name='tools',
    version='1.0',
    description=("some useful tools"),
    long_description=long_description,
    author='jinlong li',
    author_email='zxc76229@163.com',
    url='https://gitlab.com/killmymates/tools',
    packages=('tools', ),
    install_requires=(
        'fnvhash',
        'lxml',
        'peewee',
        'PyYAML',
        'redis',
        'requests',
        'fire',
        'html2text',
        'tomd',
        'requests',
        #'gevent',
        #'psycopg2',
        #'selenium>=3.7.0',
        #'parsel>=1.2.0',
        #'tldextract>=2.1.0'
    ),
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ])
