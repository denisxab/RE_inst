from django.urls import path

from mainapp.views import RePage

urlpatterns = [
		path('', RePage.as_view(), name="main_url"),
]
