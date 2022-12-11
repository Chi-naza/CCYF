from django.urls import path
from Dashboard.views import AdminHomeData


urlpatterns = [
    path('home-data/', AdminHomeData.as_view(), name="admin_homedata")
]
