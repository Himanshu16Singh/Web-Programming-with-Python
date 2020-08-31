from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # <str:name> is a placeholder
    path("<str:name>", views.greet, name="greet"),
    path("himanshu", views.himanshu, name="himanshu"),
    path("foo", views.foo, name="foo")
]
