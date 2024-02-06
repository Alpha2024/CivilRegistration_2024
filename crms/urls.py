from django.urls import path
from .import views
from django.contrib.auth import views as auth_views



urlpatterns = [
  path('',views.home,name='home'),
  path('login',views.index, name='index'),
  path('register',views.register, name ='register'),
  path('adminhome',views.admin_page, name='admin_page'),
  path('adminstaff',views.adminstaff_page, name='adminstaff_page'),
  path('employee',views.employee_page, name='employee_page'),
  path('employeeusers_page',views.employeeusers_page, name='employeeusers_page'),
  path('aduser',views.admin_users, name='admin_users'),
  path('view_users/<int:pk>/',views.view_users,name='view_users'),
  path('delete/<int:id>/',views.delete_staff, name='emp_del'),
  path('del/<int:id>/',views.delete_emp, name='emp_delt'),
  path('dl/<int:id>/',views.del_client, name='emp_de'),
  path('export-to-csv',views.export_to_csv,name='export_to_csv'),
  path('export-to-pdf',views.export_to_pdf,name='export_to_pdf'),
  # view customer
  path('c_view_users/<int:pk>/',views.customer_users,name='c_view_users'),
  # update customer
  path('update_customer/<int:pk>/', views.update_customer, name='update_customer'),

  # staff update customer
  path('emp_update_customer/<int:pk>/', views.emp_update_customer, name='emp_update_customer'),

# admin registered death path
  path('reg_death',views.reg_death, name='reg_death'),
  path('emp_reg_death',views.emp_reg_death, name='emp_reg_death'),

  # print pdf
  path('generate-pdf/<int:id>/', views.generate_pdf, name='generate_pdf'),

  # page 404
  path('page_404', views.page_404, name='page_404'),

  # email passowrd reset
  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

# qrcode
 
]

