from django.test import TestCase
from django.urls import reverse


class TiendaPagesTests(TestCase):
    def test_homepage_uses_shared_base_template(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tienda_bolis/home.html')
        self.assertTemplateUsed(response, 'tienda_bolis/base.html')

    def test_store_page_uses_shared_base_template(self):
        response = self.client.get(reverse('tienda_bolis:home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tienda_bolis/home.html')
        self.assertTemplateUsed(response, 'tienda_bolis/base.html')

    def test_contact_page_contains_simple_form(self):
        response = self.client.get(reverse('tienda_bolis:contact'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tienda_bolis/base.html')
        self.assertContains(response, '<form class="contact-form" method="get">')
        self.assertContains(response, 'type="email"')
