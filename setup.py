from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

VERSION = "0.10"

setup(
    name='yahooweather',
    version=VERSION,
    license='BSD License',
    author='Pascal Vizeli',
    author_email='pvizeli@syshack.ch',
    url='https://github.com/pvizeli/yahooweather',
    download_url='https://github.com/pvizeli/yahooweather/tarball/'+VERSION,
    description=('a Python module that provides an interface to the Yahoo! '
                 'Weather RSS feed.'),
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    keywords=['weather', 'yahoo', 'interface', 'wrapper', 'api'],
    zip_safe=False,
    platforms='any',
    py_modules=['yahooweather'],
)
