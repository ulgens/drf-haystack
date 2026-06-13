#!/usr/bin/env python


import os
import sys
from pathlib import Path

import django
from django.core.management import call_command


def start(argv=None):
    sys.path.insert(0, str(Path(__file__).parent.parent))
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
    django.setup()

    call_command("test", sys.argv[1:])


if __name__ == "__main__":
    start(sys.argv)
