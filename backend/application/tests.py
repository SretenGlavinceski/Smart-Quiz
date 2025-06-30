from django.test import TestCase
from .models import Section

class SectionExistenceTest(TestCase):
    def test_at_least_two_sections_exist(self):
        count = Section.objects.count()
        self.assertGreaterEqual(count, 2, f"Expected at least 2 sections in the DB, found {count}")
