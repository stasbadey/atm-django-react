from django.urls import path

from banking import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('refill/', views.refill, name='refill'),
    path('check-amount/', views.check_money, name='check-amount'),
    path('transfer/', views.transfer, name='transfer'),
    path('withdraw/', views.withdraw, name='withdraw')
]
