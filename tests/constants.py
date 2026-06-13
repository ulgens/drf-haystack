import json

from django.conf import settings

with (settings.BASE_DIR / "mockapp" / "fixtures" / "mocklocation.json").open() as f:
    mocklocation_size = len(json.loads(f.read()))

MOCKLOCATION_DATA_SET_SIZE = mocklocation_size

with (settings.BASE_DIR / "mockapp" / "fixtures" / "mockperson.json").open() as f:
    mockperson_size = len(json.loads(f.read()))

MOCKPERSON_DATA_SET_SIZE = mockperson_size
