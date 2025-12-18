import json
import os

from django.conf import settings

with open(os.path.join(settings.BASE_DIR, "mockapp", "fixtures", "mocklocation.json")) as f:
    mocklocation_size = len(json.loads(f.read()))

MOCKLOCATION_DATA_SET_SIZE = mocklocation_size

with open(os.path.join(settings.BASE_DIR, "mockapp", "fixtures", "mockperson.json")) as f:
    mockperson_size = len(json.loads(f.read()))

MOCKPERSON_DATA_SET_SIZE = mockperson_size
