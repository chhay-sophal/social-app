from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        default='default.jpg'
    )

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        force_insert = kwargs.pop('force_insert', False)
        super().save()

        pic = Image.open(self.profile_picture.path)

        if pic.mode != 'RGB':
            pic = pic.convert('RGB')

        if pic.height > 300 or pic.width > 300:
            output_size = (300, 300)
            pic.thumbnail(output_size)
            pic.save(self.profile_picture.path)