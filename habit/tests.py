from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User


class HabitTestCase(APITestCase):
    test_email = 'abc@mail.ru'
    test_password = 'abc123'

    def setUp(self) -> None:
        self.user = User(
            email=self.test_email,
        )

        self.user.set_password(self.test_password)
        self.user.save()

        response = self.client.post(
            '/user/api/token/',
            {'email': self.test_email, 'password': self.test_password}
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_habit_create(self):
        response = self.client.post(
            '/habit/',
            {
                "action": "Делать зарядку",
                "location_action": "Дома",
                "time_action": "08:30",
                "time_to_complete": "00:10",
                "award": "Шоколадка"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_id_habit(self):
        self.test_habit_create()
        response = self.client.get(
            '/habit/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "location_action": "Дома",
                "time_action": "08:30:00",
                "action": "Делать зарядку",
                "is_pleasant": False,
                "period": "one_day",
                "award": "Шоколадка",
                "time_to_complete": "00:10:00",
                "is_public": False,
                "owner": 1,
                "pleasant_habit": None
            }
        )

    def test_get_habit(self):
        self.test_habit_create()
        response = self.client.get(
            '/habit/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "location_action": "Дома",
                    "time_action": "08:30:00",
                    "action": "Делать зарядку",
                    "is_pleasant": False,
                    "period": "one_day",
                    "award": "Шоколадка",
                    "time_to_complete": "00:10:00",
                    "is_public": False,
                    "owner": 1,
                    "pleasant_habit": None
                }
            ]
        )
    def test_put_or_patch_habit(self):
        self.test_habit_create()
        response = self.client.put(
            '/habit/1/',
            {
                "action": "Пить воду",
                "location_action": "Дома",
                "time_action": "10:30",
                "time_to_complete": "00:10",
                "award": "Шоколадка"
            }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "location_action": "Дома",
                "time_action": "10:30:00",
                "action": "Пить воду",
                "is_pleasant": False,
                "period": "one_day",
                "award": "Шоколадка",
                "time_to_complete": "00:10:00",
                "is_public": False,
                "owner": 1,
                "pleasant_habit": None
            }
        )
        self.test_habit_create()
        response = self.client.patch(
            '/habit/1/',
            {
                "action": "Пить воду",
                "location_action": "Дома",
                "time_action": "10:30",
                "time_to_complete": "00:10",
                "award": "Шоколадка"
            }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "location_action": "Дома",
                "time_action": "10:30:00",
                "action": "Пить воду",
                "is_pleasant": False,
                "period": "one_day",
                "award": "Шоколадка",
                "time_to_complete": "00:10:00",
                "is_public": False,
                "owner": 1,
                "pleasant_habit": None
            }
        )
    def test_delete_habit(self):
        self.test_habit_create()
        response = self.client.delete(
            '/habit/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )