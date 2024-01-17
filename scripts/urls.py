from django.urls import path
from scripts.views import *


urlpatterns = [
    path('write/', write, name='writescript'),
    path('delete/<int:script_id>', delete_script, name='delete_script')
]