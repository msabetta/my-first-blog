from django.test import TestCase, Client
import logging

logger = logging.getLogger(__name__)


class BaseTestCase(TestCase):
    fixtures = ['posts.json','users.json']
    
    def setUp(self):
        # Test definitions as before
        self.client = Client()
        self.username = "user"
        self.password = "pass"
        #this is a django login (not django rest)
        logged = self.client.login()
        logger.debug("L\'utente è loggato: {}".format(logged))
    
    def test_hello_world_ok(self):
        """TODO"""
        response = self.client.get('/blog/base/')
        self.assertEqual(response.status_code, 200)
   
    def test_hello_world_post(self):
        """TODO"""
        data = {}
        response = self.client.post('/blog/base/',data)
        self.assertEqual(response.status_code, 405)
    
    def test_get_posts(self):
        """TODO"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)    
    