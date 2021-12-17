import re
from pathlib import Path

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    version = Path(package, "__version__.py").read_text()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", version).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [str(path.parent) for path in Path(package).glob("**/__init__.py")]


setup(
    name='fastlab',
    version=get_version('fastlab'),
    author='Anoyi',
    author_email='545544032@qq.com',
    url='https://github.com/tezignlab/fastlab',
    description='An extension library for FastAPI framework',
    long_description=(
        open('README.md', 'r', encoding='utf8').read()
    ),
    license='MIT License',
    install_requires=[
        'fastapi>=0.70.0',
    ],
    keywords="fastapi logs utils models",
    packages=get_packages('fastlab'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)