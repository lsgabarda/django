from django.urls import path
from .views import HomePageView, UserList, PermissionList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('user_list/', UserList.as_view(), name='user_list'),
    path('permission/', PermissionList.as_view(), name='permission'),
]