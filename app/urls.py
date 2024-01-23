from django.urls import path
from .views import scale, EditScaleView

urlpatterns = [
    path('', scale, name='scale'),
    path("scale/<pk>/update/", EditScaleView.as_view(), name="scale_update")
]
