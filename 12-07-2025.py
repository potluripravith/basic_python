#Test Driven Development 

### 1) Basic Function 
import unittest
from maths import multiply

class TestMathOperations(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3,4),12) # Fails -funtion does not exist
        
    def test_multiply_different_values(self):
        self.assertEqual(multiply(5, 6), 30)
    def test_multiply_by_zero(self):
        self.assertEqual(multiply(7, 0), 0)    
    
if __name__=='__main__':
    unittest.main()
    
#### First we have build the test case but it fails because we didnot created the function which is RED and now we improve the code which is hardcoded which cheating but we did then we test with some more test cases now we do correct code Green phase which is good then again add edge cases for refactoring

## assertEqual exact matching almost equal (a,b,places = n) floats we will use
### 2)Stack Class
import unittest
from stack import Stack ## Will cause ImportError intially
class TestStack(unittest.TestCase):
    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(),2)
        self.assertEqual(s.pop(),1)
        
    def test_empty_stack(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()
            
if __name__ == '__main__':
    unittest.main()
    
#Flask API  
import unittest
from app import app
class TestHelloAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_hello_endpoint(self):
        response= self.client.get("/hello")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,{"message":"Hello,TDD!"})
    def _hello_person(self):
        response = self.client.get('/greet/Sunny')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, Sunny!"})
   
if __name__ == '__main__':
    
    unittest.main()
    
    
    
#Mocking External Services 
import unittest
from unittest.mock import patch, Mock
from weather_service import get_weather

class TestWeatherService(unittest.TestCase):
    @patch('weather_service.requests.get')
    def test_get_weather_success(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 22.5},
            'weather': [{'description': 'clear sky'}]
        }
        mock_get.return_value = mock_response
        
        # Call function
        result = get_weather('London')
        
        # Assertions
        self.assertEqual(result['temperature'], 22.5)
        self.assertEqual(result['description'], 'clear sky')
    
    @patch('weather_service.requests.get')
    def test_get_weather_failure(self, mock_get):
        # Setup failed response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        # Call function
        result = get_weather('InvalidCity')
        
        # Assertion
        self.assertIsNone(result)
    @patch('weather_service.requests.get')
    def test_get_weather_invalid_response(self, mock_get):
        # Setup invalid JSON response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response
    
        result = get_weather('BrokenCity')
    
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
