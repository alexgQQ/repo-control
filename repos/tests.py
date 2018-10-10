from django.test import TestCase
from django.urls import reverse

from .models import GitRepo

class GitRepoModelTest(TestCase):

    def setUp(self):
        GitRepo.objects.create(name='test-repo')

    def test_text_content(self):
        repo = GitRepo.objects.get(id=1)
        expected_object_name = f'{repo.name}'
        self.assertEqual(expected_object_name, 'test-repo')

class HomePageViewTest(TestCase):

    def setUp(self):
        GitRepo.objects.create(name='test-repo')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
