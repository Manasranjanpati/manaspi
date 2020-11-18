from django.urls import path
from . import views


urlpatterns = [
    path('', views.applicant_form_view, name='applicant_form_view'),
    path('<int:id>/', views.applicant_form_view, name='applicant_form_view'),
    path('delete/<int:id>/', views.applicant_delete_view,
         name='applicant_delete_view'),
    path('list/', views.applicant_list_view, name='applicant_list_view')
]
