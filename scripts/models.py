from django.db import models
from core.models import CustomUser
from rooms.models import Room
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


# Create your models here.
class Script(models.Model):
    name = models.CharField(max_length=50)
    content = RichTextField()
    slug = AutoSlugField(populate_from='name', unique=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=False)
    writed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'script'
        verbose_name = 'Script'
        verbose_name_plural = 'Scripts'

    def __str__(self):
        return self.name