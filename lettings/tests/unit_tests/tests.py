from django.test import TestCase
from django.urls import reverse

import pytest, pdb

from lettings.models import Letting, Address

# pytestmark = pytest.mark.django_db

class TestLettingsIndexUrl(TestCase):

    def test_lettings_index_exists_at_correct_location(self):
        response = self.client.get(reverse("lettings:index"))
        assert response.status_code == 200

    def test_lettings_index_template_name_correct(self):  
        response = self.client.get(reverse("lettings:index"))
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_lettings_index_correct_template_content(self):
        response = self.client.get(reverse("lettings:index"))
        self.assertContains(response, "<h1>Lettings</h1>")

# <h1>Welcome to Holiday Homes</h1>
# <h1>Lettings</h1>
# <h1>{}</h1>
# <h1>Profiles</h1>
# <h1>Welcome to Holiday Homes</h1>
# Tests 2e view

class TestLettingsUrl(TestCase):

    def setup_method(self, method):
        address1 = Address.objects.create(number=1, street="Sesame Street",
        city="LA", state="California", zip_code=5, country_iso_code=455)
        letting1 = Letting.objects.create(title="SupaFlat", address=address1)

    def test_lettings_index_exists_at_correct_location(self):
        response = self.client.get(reverse("lettings:index")+"1/")
        assert response.status_code == 200

    def test_lettings_index_template_name_correct(self):  
        response = self.client.get(reverse("lettings:index")+"1/")
        self.assertTemplateUsed(response, "lettings/letting.html")

    def test_lettings_index_correct_template_content(self):
        letting1 = Letting.objects.get(id=1)
        response = self.client.get(reverse("lettings:index")+"1/")
        self.assertContains(response, f"<h1>{letting1.title}</h1>")
