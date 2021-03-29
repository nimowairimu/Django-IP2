from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to="static/") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 50)

    def __str__(self):
        return str(self.profile_photo)
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to="user_directory_path",verbose_name ='Picture', null=False)
    image_name = models.CharField(max_length = 30)
    image_caption = models.TextField(max_length = 30)
    profile  = models.ForeignKey('Profile', on_delete= models.DO_NOTHING,)
    likes =models.IntegerField( blank=True,null=True )
    comments =models.TextField(max_length = 50) 

    def get_absolute_url(self):
        return reverse('postdetails', args=[str(self.id)])

    def __str__(self):
         return str(self.image)

    def save_image(self):
        self.save()

class Follow(models.Model):
	follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='follower')
	following = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='following')
    
def __str__(self):
    return f'{self.follower} Follow' 