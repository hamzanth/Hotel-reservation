from django.urls import path
from .views import HotelListView, DocumentationView

urlpatterns = [
	path("", HotelListView.as_view(), name="hotel-list"),
	path("api/documentation", DocumentationView.as_view(), name="documentation")
]