from django.urls import path, re_path

from . import views

app_name = "instructors"

urlpatterns = [
    # example: /pt
    re_path(r"(?P<language>[a-zA-Z]{0,2})", views.list, name="list"),
]
