from django.test import TestCase, Client


class PostsTestCase(TestCase):
    fixtures = ['posts.json','users']
    
    def setUp(self):
        # Test definitions as before
        self.client = Client()
    
    def test_get_posts(self):
        """TODO"""
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)   
        print(response.json()) 
    
    def test_post_posts(self):
        data = {
            'author': 1, 
            "title": "automatic tests", 
            "text": "Questi dati vengono dall'automatic test e alla fine non ci saranno piu a DB"
        }
        response = self.client.post('/api/posts/',data=data)
        self.assertEqual(response.status_code, 403)   
    def test_post_posts_authenticated(self):
        self.client.login(username="admin",password="admin")
        data = {
            'author': 1, 
            "title": "automatic tests", 
            "text": "Questi dati vengono dall'automatic test e alla fine non ci saranno piu a DB"
        }
        response = self.client.post('/api/posts/',data=data)
        self.assertEqual(response.status_code, 201)   