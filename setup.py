# Always prefer setuptools over distutils
from setuptools import setup

# Get the long description from the README file
with open('README.md') as file:
    long_description = file.read()

setup(
    name='tools',
    version='0.1',
    description=("some useful tools"),
    long_description=long_description,
    author='jinlong li',
    author_email='zxc76229@163.com',
    url='https://gitlab.com/killmymates/tools',
    packages=('tools', ),
    install_requires=(
        'certifi==2017.7.27.1',
        'chardet==3.0.4',
        'fnvhash==0.1.0',
        'idna==2.6',
        'gevent',
        'lxml==4.0.0',
        'peewee==2.10.1',
        'psycopg2==2.7.3.1',
        'PyYAML==3.12',
        'redis==2.10.6',
        'requests==2.18.4',
        'urllib3==1.22',
        'fire',
        'tenacity',
        'html2text',
        'tomd',
        'pytube',
        #'requests>=2.18.1',
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
