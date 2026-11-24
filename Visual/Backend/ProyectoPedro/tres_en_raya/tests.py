from django.test import TestCase
from django.urls import reverse


class TresEnRayaTests(TestCase):
    def test_initial_board_is_empty(self):
        response = self.client.get(reverse('tres_en_raya:juego'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tres_en_raya/tres_en_raya.html')
        self.assertContains(response, 'Turno de X')
        self.assertContains(response, 'value="---------"', count=1)

    def test_move_changes_turn(self):
        response = self.client.post(
            reverse('tres_en_raya:juego'),
            {'tablero': '---------', 'turno': 'X', 'posicion': '0'},
        )

        self.assertContains(response, 'Turno de O')
        self.assertContains(response, 'value="X--------"', count=1)

    def test_x_can_win(self):
        response = self.client.post(
            reverse('tres_en_raya:juego'),
            {'tablero': 'XX-OO----', 'turno': 'X', 'posicion': '2'},
        )

        self.assertContains(response, '¡Ha ganado X!')
