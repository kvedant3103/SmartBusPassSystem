from django.urls import path

# from Buss_pass import Buss_pass_app
from . import views

urlpatterns = [
  # -------------------------------user------------------------------------------
    path('', views.index, name='index'),
    path('register/', views.regform_view, name='register'),
    path('login/', views.userlogin, name='login'),
    path('busdetails/', views.Bus_details, name='busdetails'),
    path('createpass/<int:id>/',views.createbuspass, name='createpass'),
    path('renewpass/<int:id>/', views.renewpass, name='renewpass'),
    path('updatepass/<int:id>/', views.updatepass, name='updatepass'),
    path('created_pass/', views.created_pass, name='created_pass'),
    path('logoutuser/', views.logout_request_user, name="logoutuser"),

  # ---------------------------------admin------------------------------------------
    path('adminlogin/', views.admin_login, name='adminlogin'),
    path('addbus/', views.addbus, name='addbus'),
    path('userdetails/', views.user_details, name='userdetails'),
    path('editbus/', views.edit_bus, name='editbus'),
    path('delete/<int:id>',views.delete_bus, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete_bus/<int:id>/', views.delete_bus, name='delete_bus'),
    path('logoutadmin/', views.logout_request_admin, name="logoutadmin"),

 # ------------------------------------ Pdf ---------------------------------------------
    path('<int:pk>', views.PdfDetail.as_view(), name='pdfdetail'),


]