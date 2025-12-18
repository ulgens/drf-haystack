import os
from importlib.util import find_spec
import django

test_runner = None
old_config = None

os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"


if hasattr(django, "setup"):
    django.setup()


def _geospatial_support():
    return find_spec("geopy") and find_spec("haystack.utils.geo.Point")


geospatial_support = _geospatial_support()


def _restframework_version():
    import rest_framework

    return tuple(map(int, rest_framework.VERSION.split(".")))


restframework_version = _restframework_version()


def _elasticsearch_version():
    import elasticsearch

    return elasticsearch.VERSION


elasticsearch_version = _elasticsearch_version()


def setup():
    from django.test.runner import DiscoverRunner

    global test_runner
    global old_config

    test_runner = DiscoverRunner()
    test_runner.setup_test_environment()
    old_config = test_runner.setup_databases()


def teardown():
    test_runner.teardown_databases(old_config)
    test_runner.teardown_test_environment()
