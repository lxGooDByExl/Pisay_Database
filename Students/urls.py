from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from Students.views import StudentView

urlpatterns = [
    url(r'^list/$', StudentView.as_view(), name='students'),
]