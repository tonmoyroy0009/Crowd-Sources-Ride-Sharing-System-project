from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

User._meta.get_field('email')._unique = True

def upload_pic_to(instance, filename):
    return 'user_data/{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False)
    profile_picture = models.ImageField(
        default='default.jpg', upload_to=upload_pic_to)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=255, verbose_name="Present Address")
    is_email_verified = models.BooleanField(default=False)    
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

class Verify(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nid = models.CharField(max_length=23, verbose_name="NID")
    nid_front = models.ImageField(
        verbose_name="NID Front Picture", upload_to=upload_pic_to)
    nid_back = models.ImageField(
        verbose_name="NID Back Picture", upload_to=upload_pic_to)
    nid_selfie = models.ImageField(
        verbose_name="Selfie With Holding Your NID", upload_to=upload_pic_to)
    utility = models.ImageField(
        verbose_name="Utility Picture", upload_to=upload_pic_to)

    is_verified = models.BooleanField(default=False)
    is_verify_submit = models.BooleanField(default=False)
