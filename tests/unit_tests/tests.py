from django.test import TestCase
from django.urls import reverse


# original test from forked project
def test_dummy():
    assert 1

class TestOcLettingsIndexUrl(TestCase):

    def test_oc_lettings_index_exists_at_correct_location(self):
        response = self.client.get(reverse("oc_lettings_app:index"))
        assert response.status_code == 200

    def test_oc_lettings_index_template_name_correct(self):  
        response = self.client.get(reverse("oc_lettings_app:index"))
        self.assertTemplateUsed(response, "index.html")

    def test_oc_lettings_index_correct_template_content(self):
        response = self.client.get(reverse("oc_lettings_app:index"))
        self.assertContains(response, "<h1>Welcome to Holiday Homes</h1>")