'''
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
'''
#import django

#from django.contrib.auth.models import AnonymousUser
#from django.core import serializers
from django.test import  (
    #Client,
    #RequestFactory,
    SimpleTestCase,
    #TestCase,
)
#from djmoney.money import Money
#from rest_framework.test import APITestCase, APIClient

#from ..chapter_3.models import Engine, Seller, Vehicle, VehicleModel
#from ..chapter_4.views import practice_year_view, VehicleView


class TestingCalibrator(SimpleTestCase):
    '''
    Calibrator, used to see if testing system works and is used as a boilerplate for creating
    new test classes.
    '''
    def setUp(self):
        '''
        Used to prepare the environment and/or database before executing any of the test methods.
        '''
        pass

    def tearDown(self):
        '''
        Clean-up task after firing unit test
        '''
        pass

    def test_pass(self):
        '''
        Checks if True == True
        Value set to True
        '''
        self.assertTrue(True)

    def test_fail(self):
        '''
        Checks if False == False
        Value set to True
        '''
        self.assertFalse(True)


#class ModelUnitTestCase(TestCase):
#    '''
#    Django Unit Test Case
#    Used to test smallest components of Django
#    These can be utility methods, template tags/filters and/or models to name a few.
#    '''
#    # Extra Practice
#    #fixtures = ['chapter_3']

#    def setUp(self):
#        '''
#        setUp() tests if we are able to create all model objects, by creating a seller, we create
#        all of the relate objects. If successful, the VehicleModel, Engine, Vehicle and Seller
#        objects all work as they should.
#        '''
#        model = VehicleModel.objects.create(
#            name = 'Grand Cherokee Laredo 4WD',
#            make = 8
#        )
#        engine = Engine.objects.create(
#            name = '3.6L FI FFV DO',
#            vehicle_model = model
#        )
#        vehicle = Vehicle.objects.create(
#            vin = 'aa890123456789012',
#            sold = False,
#            price = Money(39875, 'USD'),
#            make = 8,
#            vehicle_model = model,
#            engine = engine
#        )
#        seller = Seller.objects.create_user(
#            'test',
#            'testing@example.com',
#            'testpassword',
#            is_staff = True,
#            is_superuser = True,
#            is_active = True,
#            name = 'Chapter 9 Seller 1'
#        )

#        seller.vehicles.set([vehicle])

#    def test_full_vehicle_name(self):
#        '''
#        Checks if the full vehicle name of the vehicle created in the setUp() method is generated
#        as it should. Expected value = 'Jeep Grand Cherokee Laredo 4WD - 3.6L FI FFV DO'
#        '''
#        vehicle_1 = Vehicle.objects.get(
#            vin = 'aa890123456789012'
#        )
#        self.assertEqual(
#            vehicle_1.full_vehicle_name(),
#            'Jeep Grand Cherokee Laredo 4WD - 3.6L FI FFV DO' # Correct Value
#        )
#        #self.assertEqual(
#        #    vehicle_1.full_vehicle_name(),
#        #    'Jeep Grand Cherokee Laredo 4WD - 3.6L FI FFV DO asdfasdfas' # Incorrect Value
#        #)

#        # Extra Practice
#        #vehicle_2 = Vehicle.objects.get(id=1)
#        #self.assertEqual(
#        #    vehicle_2.full_vehicle_name(),
#        #    'Chevrolet Blazer LT - 3.9L DI DOHC 6cyl'
#        #)
#        #print('vehicle_1 = %s' % vehicle_1.full_vehicle_name())
#        #print('vehicle_2 = %s' % vehicle_2.full_vehicle_name())


#class YearRequestTestCase(TestCase):
#    '''
#    Django Request Test Case
#    Used to test Django method-based views
#    '''
#    def setUp(self):
#        '''
#        Testing views require a RequestFactory() object
#        '''
#        self.factory = RequestFactory()

#    def test_methodbased(self):
#        '''
#        Checks if the path http://localhost:8000/my_year_path/2022/ actually exists and returns
#        a 200 response code (Valid)
#        '''
#        request = self.factory.get('/my_year_path/2022/') # Correct Value
#        #request = self.factory.get('/my_year_path/12/') # Incorrect Value

#        request.user = AnonymousUser()

#        response = practice_year_view(request, 2022) # Correct Value
#        #response = practice_year_view(request, 12) # Incorrect Value

#        self.assertEqual(response.status_code, 200)


#class VehicleRequestTestCase(TestCase):
#    '''
#    Django Request Test Case
#    Used to test Django class-based views
#    '''
#    fixtures = ['chapter_3']

#    def setUp(self):
#        '''
#        Testing views require a RequestFactory() object
#        '''
#        self.factory = RequestFactory()

#    def test_classbased(self):
#        '''
#        Checks if the path http://localhost:8000/vehicle/1/ actually exists and returns a 200
#        response code (Valid)
#        '''
#        request = self.factory.get('/vehicle/1/') # Correct Value
#        #request = self.factory.get('/vehicle/99/') # Incorrect Value

#        request.user = AnonymousUser()

#        response = VehicleView.as_view()(request, 1) # Correct Value
#        #response = VehicleView.as_view()(request, 99) # Incorrect Value

#        self.assertEqual(response.status_code, 200)


#class SellerClientTestCase(TestCase):
#    '''
#    Django Client/Request Test Case
#    Used to test custom REST-API Endpoints
#    '''
#    fixtures = ['chapter_3']

#    def setUp(self):
#        self.user = Seller.objects.get(id=1)
#        self.client = Client()

#        # Note - It would be wise to keep this password in your .env file as a TESTUSER_PASSWORD,
#        # then bring it in as a global variable in your settings.py file and then import your
#        # settings into this file to use your variable that way.
#        self.client.login(
#            username = self.user.username,
#            password = 'mynewpassword' # Correct Value
#        )
#        #self.client.login(
#        #    username = self.user.username,
#        #    password = 'mynewpassword1' # Incorrect Value
#        #)

#    def test_get(self):
#        '''
#        Tests a custom-built REST-API Endpoint using the GET Method at the path
#        http://localhost:8000/chapter-8/seller/1/, while using the Django Client() class to
#        login for authentication. Checks if it actually exists and returns a
#        200 response code (Valid)
#        '''
#        response = self.client.get('/chapter-8/seller/1/')

#        self.assertEqual(response.status_code, 200)

#        # Check that the returned context object has a seller name equal to what
#        # is expected (Test Biz Name)
#        seller = response.context['seller']
#        self.assertEqual(seller.name, 'Test Biz Name') # Correct Value
#        #self.assertEqual(seller.name, 'Test Biz Name1') # Incorrect Value


#class EngineAPITestCase(APITestCase):
#    '''
#    Django Client/Request Test Case
#    Used to test custom REST-API Endpoints
#    '''
#    fixtures = ['chapter_3']

#    def setUp(self):
#        self.user = Seller.objects.get(id=1)
#        self.client = APIClient()

#        # Note - It would be wise to keep this password in your .env file as a TESTUSER_PASSWORD,
#        # then bring it in as a global variable in your settings.py file and then import your
#        # settings into this file to use your variable that way.
#        self.client.login(
#            username = self.user.username,
#            password = 'mynewpassword' # Correct Value
#        )
#        #self.client.login(
#        #    username = self.user.username,
#        #    password = 'mynewpassword1' # Incorrect Value
#        #)

#    def test_post(self):
#        '''
#        Tests creating an Engine at a Django REST Framework REST-API Endpoint using the POST method
#        at http://localhost:8000/chapter-8/engines/, while using the Django REST-Framework
#        APIClient() class to login for authentication. Checks if it returns
#        a 201 response code (Created).
#        '''
#        response = self.client.post(
#            '/chapter-8/engines/',
#            {'name': 'New Engine'},
#            format='json'
#        )

#        self.assertEqual(response.status_code, 201) # Correct Value
#        #self.assertEqual(response.status_code, 500) # Incorrect Value
#        self.assertEqual(response.data['name'], 'New Engine') # Correct Value
#        #self.assertEqual(response.data['name'], 'New Engine1') # Incorrect Value

#    def test_put(self):
#        '''
#        Tests updating an Engine at a Django REST Framework REST-API Endpoint using the PUT method
#        at http://localhost:8000/chapter-8/engines/1/, while using the Django REST-Framework
#        APIClient() class to login for authentication. Checks if it returns
#        a 200 response code (Success).
#        '''
#        response = self.client.put(
#            '/chapter-8/engines/1/', # Correct Value
#            #'/chapter-8/engines/3/', # Incorrect Value
#            {'name': 'My Changed Engine Name'},
#            format='json'
#        )

#        self.assertEqual(response.status_code, 200) # Correct Value
#        #self.assertEqual(response.status_code, 500) # Incorrect Value
#        self.assertEqual(response.data['name'], 'My Changed Engine Name') # Correct Value
#        #self.assertEqual(response.data['name'], 'My Changed Engine Name1') # Incorrect Value


# This class was auto generated when you created a new Django app, either with Visual Studio or
# through the command-line.
#class SimpleTest(TestCase):
#    '''Tests for the application views.'''

#    # Django requires an explicit setup() when running tests in PTVS
#    @classmethod
#    def setUpClass(cls):
#        super(SimpleTest, cls).setUpClass()
#        django.setup()

#    def test_basic_addition(self):
#        '''
#        Tests that 1 + 1 always equals 2.
#        '''
#        self.assertEqual(1 + 1, 2)
