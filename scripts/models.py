from django.db import models
from core.models import CustomUser
from ckeditor.fields import RichTextField


# Create your models here.
class Script(models.Model):
    name = models.CharField(max_length=50)
    content = RichTextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    writed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'script'
        verbose_name = 'Script'
        verbose_name_plural = 'Scripts'

    def __str__(self):
        return self.name