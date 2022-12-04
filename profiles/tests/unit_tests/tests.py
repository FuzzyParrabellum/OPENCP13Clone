import pytest

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from profiles.models import Profile


class TestProfilesIndexUrl(TestCase):

    def test_profiles_index_exists_at_correct_location(self):
        response = self.client.get(reverse("profiles:index"))
        assert response.status_code == 200

    def test_profiles_index_template_name_correct(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profiles_index_correct_template_content(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertContains(response, "<h1>Profiles</h1>")


class TestProfilesUrl(TestCase):

    @pytest.mark.django_db
    def test_profiles_index_exists_at_correct_location(self):
        user1 = User.objects.create(username='toto', password=123,
                                    first_name='toto', last_name="tata",
                                    email="toto@example.com")
        profile1 = Profile.objects.create(user=user1,
                                          favorite_city="Rio")
        profile_name = profile1.user.username
        response = self.client.get(reverse("profiles:index")+f"{profile_name}/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_profiles_index_template_name_correct(self):
        user1 = User.objects.create(username='toto', password=123,
                                    first_name='toto', last_name="tata",
                                    email="toto@example.com")
        profile1 = Profile.objects.create(user=user1,
                                          favorite_city="Rio")
        profile_name = profile1.user.username
        response = self.client.get(reverse("profiles:index")+f"{profile_name}/")
        self.assertTemplateUsed(response, "profiles/profile.html")

    @pytest.mark.django_db
    def test_profiles_index_correct_template_content(self):
        user1 = User.objects.create(username='toto', password=123,
                                    first_name='toto', last_name="tata",
                                    email="toto@example.com")
        profile1 = Profile.objects.create(user=user1,
                                          favorite_city="Rio")
        profile1 = Profile.objects.get(id=1)
        profile_name = profile1.user.username
        response = self.client.get(reverse("profiles:index")+f"{profile_name}/")
        self.assertContains(response, f"<h1>{profile_name}</h1>")
