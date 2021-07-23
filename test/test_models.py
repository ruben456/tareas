from django.test import TestCase
from api.models import Task
from django.contrib.auth.models import User

class TaskTest(TestCase):
    """ Módulo de pruebas para el modelo Task """

    def setUp(self):
        """ Preparación de objetos para pruebas """
        User.objects.create_user('prueba', 'prueba@django.com', '1234')
        user = User.objects.get(pk=1)
        Task.objects.create(
            user=user, description='prueba 1', complete=False
        )
        Task.objects.create(
            user=user, description='prueba 2', complete=False
        )
    
    def test_task_str(self):
        """ Prueba para validar que los objetos existen """
        task_1 = Task.objects.get(description='prueba 1')
        task_2 = Task.objects.get(description='prueba 2')
        self.assertEqual(
            task_1.__str__(), "prueba 1"            
        )
        self.assertEqual(
            task_2.__str__(), "prueba 2"            
        )