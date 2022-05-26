from django.urls  import path
from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:contato_id>", views.index_contato, name="ver_contato"),
]