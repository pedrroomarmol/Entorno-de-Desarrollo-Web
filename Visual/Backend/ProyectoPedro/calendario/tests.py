from django.test import TestCase
from django.urls import reverse


class CalendarioTests(TestCase):
    def test_inicio_displays_date_form(self):
        response = self.client.get(reverse('calendario:inicio'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendario/inicio.html')
        self.assertContains(response, 'DD-MM-AAAA')

    def test_date_form_redirects_to_named_date_url(self):
        response = self.client.get(
            reverse('calendario:inicio'),
            {'fecha': '07-03-2026'},
        )

        self.assertRedirects(
            response,
            reverse('calendario:fecha', kwargs={'fecha': '07-03-2026'}),
        )

    def test_valid_date_shows_date_details(self):
        response = self.client.get(
            reverse('calendario:fecha', kwargs={'fecha': '07-03-2026'})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendario/fecha.html')
        self.assertContains(response, '7 de marzo de 2026')

    def test_invalid_format_and_impossible_date_show_error_page(self):
        for fecha in ('2026-03-07', '31-02-2026'):
            with self.subTest(fecha=fecha):
                response = self.client.get(
                    reverse('calendario:fecha', kwargs={'fecha': fecha})
                )

                self.assertEqual(response.status_code, 400)
                self.assertTemplateUsed(response, 'calendario/error.html')
