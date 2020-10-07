from django.test import TestCase
from accounts.models import User
from todos.models import Todo

# Create your tests here.
class TodoTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='password')

    def test_todo_index(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/todos/')

        # User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        response = self.client.get('/todos/')
        self.assertTemplateUsed(response, 'todos/index.html')

    
    def test_todo_create_get(self):
        self.client.login(username='testuser', password='password')
        # todos 경로로 요청한다.
        response = self.client.get('/todos/create/')
        # todos/form.html이 랜더링 되었는지 확인한다.
        print(response)
        self.assertTemplateUsed(response, 'todos/form.html')
        self.assertEqual(response.status_code, 200)

    def test_todo_create_post(self):
        self.client.login(username='testuser', password='password')
        
        # 데이터가 유효하지 않은경우
        invalid_data = {
            # 'content': None
        }
        response = self.client.post('/todos/create/', invalid_data)
        self.assertEqual(response.status_code, 200)
        todos = Todo.objects.all()
        self.assertEqual(len(todos), 0)

        # 데이터가 유효한 경우
        valid_data = {
            'content': 'test-content'
        }
        response = self.client.post('/todos/create/', valid_data)
        todos = Todo.objects.all()
        self.assertEqual(len(todos), 1)


