from django.test import TestCase
from application.models import Section

class SectionExistenceTest(TestCase):

    def setUp(self):
        Section.objects.create(section_name="Section 1", description="abc")
        Section.objects.create(section_name="Section 2", description="abc")

    def test_at_least_two_sections_exist(self):
        count = Section.objects.count()
        self.assertGreaterEqual(count, 2, f"Expected at least 2 sections in the DB, found {count}")
