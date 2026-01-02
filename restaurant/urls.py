#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('message/', views.message),
    path('api-token-auth/', obtain_auth_token),

]
