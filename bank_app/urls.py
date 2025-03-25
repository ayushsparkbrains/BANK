# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.bank_list, name='bank_list'),  
#     path('bank/create/', views.bank_create, name='bank_create'),  
#     path('bank/edit/<int:bank_id>/', views.bank_edit, name='bank_edit'),  
#     path('bank/delete/<int:bank_id>/', views.bank_delete, name='bank_delete'),  
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.bank_list, name='bank_list'),
#     path('add/', views.bank_create, name='bank_create'),
#     path('edit/<int:bank_id>/', views.bank_edit, name='bank_edit'),
#     path('delete/<int:bank_id>/', views.bank_delete, name='bank_delete'),
#     path('navigate/<str:direction>/', views.navigate, name='navigate'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.bank_list, name="bank_list"),
    path("add/", views.bank_create, name="bank_create"),
    path("edit/<int:bank_id>/", views.bank_edit, name="bank_edit"),
    path("delete/<int:bank_id>/", views.bank_delete, name="bank_delete"),
    path("navigate/<str:direction>/", views.navigate, name="navigate"),
]

