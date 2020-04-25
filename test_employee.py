import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):    
    
    
    @classmethod
    def setUpClass(cls):
        print('setupclass')
        
    @classmethod
    def tearDownClass(cls):
        print('teardownclass')
    
    def setUp(self):
        print('\nsetup')
        self.emp_1 = Employee('Kshitiz','Bhattarai',50000)
        self.emp_2 = Employee('sanju','kiran',60000)
    
    def tearDown(self):
        print('teardown')
        pass
    
    
    
    def test_email(self):
        # self.emp_1 = Employee('Kshitiz','Bhattarai',50000)
        # self.emp_2 = Employee('sanju','kiran',60000)
        
        print('test_email')
        
        self.assertEqual(self.emp_1.email,'Kshitiz.Bhattarai@email.com')
        self.assertEqual(self.emp_2.email,'sanju.kiran@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.email,'John.Bhattarai@email.com')
        self.assertEqual(self.emp_2.email,'Jane.kiran@email.com')
        
    def test_fullname(self):     
        # self.emp_1 = Employee('Kshitiz','Bhattarai',50000)
        # self.emp_2 = Employee('sanju','kiran',60000)   
        
        print('test_fullname')
        
        self.assertEqual(self.emp_1.fullname,'Kshitiz Bhattarai')
        self.assertEqual(self.emp_2.fullname,'sanju kiran')
        
        self.emp_1.first='John'
        self.emp_2.first='Jane'
        
        self.assertEqual(self.emp_1.fullname, 'John Bhattarai')
        self.assertEqual(self.emp_2.fullname,'Jane kiran')
        
    def test_apply_raise(self):        
        # self.emp_1 = Employee('Kshitiz','Bhattarai',50000)
        # self.emp_2 = Employee('sanju','kiran',60000)
        
        
        print('test_apply_raise')
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay,52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('April')
            mocked_get.assert_called_with('http://company.com/Bhattarai/April')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/kiran/June')
            self.assertEqual(schedule, 'Bad Response!')
        
        
if __name__=='__main__':
    unittest.main()