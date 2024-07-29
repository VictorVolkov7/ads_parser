import os

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """
    Loads data from JSON files.
    """
    help = 'Loads data from fixtures dir'
    fixtures_dir = 'fixtures'
    loaddata_command = 'loaddata'
    filename = 'ad'

    def handle(self, *args, **options):
        call_command(
            self.loaddata_command, os.path.join(self.fixtures_dir, f'{self.filename}.json')
        )
