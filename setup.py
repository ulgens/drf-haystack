import os
import re

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name="drf-haystack",
    version=get_version("drf_haystack"),
    description="Makes Haystack play nice with Django REST Framework",
    long_description="Implements a ViewSet, FiltersBackends and Serializers in order to play nice with Haystack.",
    author="Rolf Håvard Blindheim",
    author_email="rhblind@gmail.com",
    url="https://github.com/rhblind/drf-haystack",
    download_url="https://github.com/rhblind/drf-haystack.git",
    license="MIT License",
    packages=[
        "drf_haystack",
    ],
    include_package_data=True,
    install_requires=[
        "Django>=5.2,<6.1",
        "djangorestframework>=3.16",
        "django-haystack>=3.3.0,<4",
        "python-dateutil",
    ],
    tests_require=["coverage", "geopy", "requests"],
    zip_safe=False,
    test_suite="tests.run_tests.start",
    classifiers=[
        "Operating System :: OS Independent",
        # The package is being transferred between organizations and has no working tests / CI.
        # Use at your own risk.
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11, <3.15",
)
