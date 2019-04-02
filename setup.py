# coding: utf-8
"""Project setup script

See documentation and sample setup.py from the Python Packaging Authority(PyPA) for more information:

- https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-and-distributing-projects
- https://github.com/pypa/sampleproject/blob/master/setup.py
"""

import os
from setuptools import setup, find_packages
from setuptools.extension import Extension


def get_readme():
    """Returns the content of README.rst file
    
    :rtype: str
    """
    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, "README.rst")
    with open(filename, "r", encoding="utf-8") as fp:
        long_description = fp.read()
    return long_description


# Project classifiers from https://pypi.org/classifiers/
classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    ]


# https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args
setup(
    name='pypolynom',
    version='0.0.1',
    packages=find_packages(exclude=['doc']),
    # or packages=['pypolynom', 'pypolynom.test'],
    ext_modules=[Extension('pypolynom.cpolynom', ['pypolynom/cpolynom.pyx'])],

    # Every thing below is optional

    # Description of the project

    description='A simple polynom solver',
    long_description=get_readme(),
    url='https://gitlab.esrf.fr/silx/silx-trainings/pypolynom',
    classifiers=classifiers,
    # author='',
    # author_email='',
    # keywords='',
    # project_urls={},

    # Project requirements

    python_requires='>=3.4',
    setup_requires=['setuptools', 'wheel', 'cython'],
    install_requires=['numpy>=1.8', 'PyQt5'],
    extras_require={
        'doc': ['sphinx', 'nbsphinx']
        },

    # Additional resources
    # package_data={},
    # data_files=[],
    # entry_points={},
    )

