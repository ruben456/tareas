from django.test import TestCase
from api.models import Task
from django.contrib.auth.models import User
from django.urls import reverse
import json

class ListTaskTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        """Preparación de usuario y objetos para la realización de pruebas"""
        number_of_task = 10
        User.objects.create_user('test_user', 'test@django.com', '1234')
        user = User.objects.get(pk=1)
        for datos_task in range(number_of_task):
            Task.objects.create(
                user=user, description= 'Prueba %s' % datos_task, complete=False
            )
    
    def test_view_url_exists_at_desired_location(self):
        """Prueba que valida que la url exista y sea accesible"""
        self.client.login(username='test_user', password='1234')
        resp = self.client.get('/api/tasks/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        """Prueba que valida que la url sea accesible por el name"""
        self.client.login(username='test_user', password='1234')
        resp = self.client.get(reverse('tasks'))
        self.assertEqual(resp.status_code, 200)
    
    def test_unauthorized_user(self):
        """Prueba que valida que los usuarios no autenticados no puedan acceder a la url"""
        resp = self.client.get(reverse('tasks'))
        self.assertEqual(resp.status_code, 403)
    
    def test_lists_all_task(self):
        """Prueba para validar el listado de tareas"""
        self.client.login(username='test_user', password='1234')
        resp = self.client.get(reverse('tasks'))
        self.assertEqual(resp.status_code, 200)
    
    def test_lists_page_task(self):
        """Prueba para validar la paginación en el listado de tareas"""
        self.client.login(username='test_user', password='1234')
        resp = self.client.get('/api/tasks/?page=1')
        self.assertEqual(resp.status_code, 200)
    
    def test_lists_search_task(self):
        """Prueba para validar la busqueda en la descripción del listado de tareas"""
        self.client.login(username='test_user', password='1234')
        resp = self.client.get('/api/tasks/?search=prueba')
        self.assertEqual(resp.status_code, 200)
    
    def test_create_task(self):
        """Prueba para validar la creación de tareas"""
        self.client.login(username='test_user', password='1234')
        payload = {'description': 'prueba', 'complete': 'true'}
        resp = self.client.post(reverse('tasks'), payload)
        self.assertEqual(resp.status_code, 201)
    
    def test_update_task(self):
        """Prueba para validar la actualización de tareas"""
        self.client.login(username='test_user', password='1234')
        payload = {'id': 1, 'description': 'prueba_update', 'complete': False}
        resp = self.client.put('/api/tasks/1/', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
    
    def test_delete_task(self):
        """Prueba para validar la eliminación de tareas"""
        self.client.login(username='test_user', password='1234')
        payload = {'id': 1, 'description': 'prueba_update', 'complete': False}
        resp = self.client.delete('/api/tasks/1/', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 204)