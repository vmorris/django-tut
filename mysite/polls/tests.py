from django.test import TestCase

# Create your tests here.

class Homepage_Test(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/polls/')
        self.assertContains(response, "Hello, world. You're at the polls index.")
