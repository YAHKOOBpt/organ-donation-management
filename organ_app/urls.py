from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('main1',views.index,name='index'),
    path('',views.home,name='home'),


#################donor panel##############
    path('donor_home',views.donor_home,name='donor_home'),
    ###### donor login ########
    path('donor_register',views.donor_register,name='donor_register'),
    path('donor_login',views.donor_login,name='donor_login'),
    path('donor_logout', views.donor_logout, name='donor_logout'),

    ###### create donor ########
    path('add_donor_details',views.add_donor_details,name='add_donor_details'),
    path('view_donor_details/<int:donor_id>', views.view_donor_details, name='view_donor_details'),
    path('Update_donor_details/<int:donor_id>', views.Update_donor_details, name='Update_donor_details'),
    path('delete_donor_details/<int:donor_id>/', views.delete_donor_details, name='delete_donor_details'),

    path('home_donor/<int:donor_id>/', views.home_donor, name='home_donor'),

    path('view_organ_request', views.view_organ_request, name='view_organ_request'),

    path('Update_organ_request/<int:pk>/', views.Update_organ_request, name='Update_organ_request'),

    

################################## patient panel #################################################

    ###### patient login ########
    path('intex_1',views.intex_1,name='intex_1'),
    path('Patient_register',views.Patient_register,name='Patient_register'),
    path('Patient_login',views.Patient_login,name='Patient_login'),
    path('patient_logout', views.patient_logout, name='patient_logout'),

    ###### create patient ########
    path('add_patient_details',views.add_patient_details,name='add_patient_details'),
    path('view_patient_details/<int:patient_id>', views.view_patient_details, name='view_patient_details'),
    path('Update_patient_details/<int:patient_id>', views.Update_patient_details, name='Update_patient_details'),
    path('delete_patient_details/<int:patient_id>/', views.delete_patient_details, name='delete_patient_details'),
    path('view_organ_details', views.view_organ_details, name='view_organ_details'),

    path('give_request/<int:pk>/', views.give_request, name='give_request'),

    path('view_send_request', views.view_send_request, name='view_send_request'),




]