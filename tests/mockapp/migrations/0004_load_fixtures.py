from pathlib import Path

from django.core import serializers
from django.db import migrations


def load_data(apps, schema_editor):
    """
    Load fixtures for MockPerson, MockPet and MockLocation
    """

    fixtures = Path(__file__).parent.parent / "fixtures"

    with (fixtures / "mockperson.json").open() as fixture:
        objects = serializers.deserialize("json", fixture, ignorenonexistent=True)
        for obj in objects:
            obj.save()

    with (fixtures / "mocklocation.json").open() as fixture:
        objects = serializers.deserialize("json", fixture, ignorenonexistent=True)
        for obj in objects:
            obj.save()

    with (fixtures / "mockpet.json").open() as fixture:
        objects = serializers.deserialize("json", fixture, ignorenonexistent=True)
        for obj in objects:
            obj.save()


def unload_data(apps, schema_editor):
    """
    Unload fixtures for MockPerson, MockPet and MockLocation
    """

    MockPerson = apps.get_model("mockapp", "MockPerson")
    MockLocation = apps.get_model("mockapp", "MockLocation")
    MockPet = apps.get_model("mockapp", "MockPet")

    MockPerson.objects.all().delete()
    MockLocation.objects.all().delete()
    MockPet.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("mockapp", "0001_initial"),
        ("mockapp", "0002_mockperson"),
        ("mockapp", "0005_mockperson_birthdate"),
        ("mockapp", "0003_mockpet"),
    ]

    operations = [migrations.RunPython(load_data, reverse_code=unload_data)]
