from django.test import TestCase, SimpleTestCase, Client

class ViewTest(SimpleTestCase):
    '''
    testing class for my views, using Simple Test Case because i dont need a database
    right now
    '''
    
    def test_home(self):
        client = Client()
        response = client.get('/home/')
        self.assertEqual(response.status_code, 200)
