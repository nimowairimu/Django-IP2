from django.test import TestCase
from .models import Image,Profile
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
       self.nimo = Profile(1,'default.jpg','babygirl')
    
    def test_save_profile(self):
        self.nimo.save_profile()
        nimo_profile = Profile.objects.all()
        self.assertTrue(len(nimo_profile) > 0)
    
    def test_delete_profile(self):
        self.nimo.delete_profile()
        nimo_profile = Profile.objects.all()
        self.assertTrue(len(nimo_profile) < 1)

                                    

    
# class ImageTestClass(TestCase):
#     def setUp(self):
#         self.post = Image( 1,'static/logo.png','karura','slim thick',1,23,'Wueeh')
#     def test_save_image(self):
#         self.post.save_image()
#         image = Image.objects.all()
#         self.assertTrue(len(image) > 0)