from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    # ...

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Script(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    writed_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'script'
        verbose_name = 'Script'
        verbose_name_plural = 'Scripts'

    def __str__(self):
        return self.name