from django.urls import path
from scripts.views import *


urlpatterns = [
    path('write/', write, name='writescript'),
    path('delete/<int:script_id>', delete_script, name='delete_script'),
    path('<slug:script_slug>/', script_detail, name='script_detail'),
]