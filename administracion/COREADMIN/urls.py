from django.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from coreadmin import views

urlpatterns = [
    path('', views.home_view, name=''),
    path('home/', views.home_view, name='index.html'),

    # Account
    path('login/', views.login_view, name='login.html'),
    path('logout/', auth_views.LogoutView.as_view(template_name='appointments/account/logout.html'), name='logout'),
    # Reset password
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name='appointments/account/reset_password.html'),
        name='reset_password.html'),
    path('reset_password_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='appointments/account/reset_password_confirm.html'),
        name='password_reset_confirm'),


    # Admin
    path('register/admin/', views.register_adm_view, name='register_adm.html'),  # Admin registration
    path('login/admin/', views.login_adm_view, name='login_adm.html'),  # Admin login
    path('dashboard/admin/', views.dashboard_adm_view, name='dashboard_adm.html'),  # Admin dashboard
    path('profile/admin/', views.profile_adm_view, name='profile_adm.html'),  # Admin profile
    # Admin - Appointments
    path('view/appointments/', views.appointment_adm_view, name='appointment_adm.html'),  # Admin profile
    path('book-appointment-adm/', views.book_app_adm_view, name='book_app_adm.html'),  # Book an appointment
    path('approve-appointment/<int:pk>', views.approve_app_adm_action, name='approve_app_adm_action'),  # Approve an appointment
    path('appointment-admin/complete=<int:pk>', views.complete_app_adm_action, name='complete_app_adm_action'),  # Complete appointment action
    path('appointments/all/', views.all_app_adm_view, name='view_all_app_adm.html'),  # View approved appointments
    path('appointment/details/<int:pk>', views.app_details_adm_view, name='view_app_details_adm.html'),  # View approved appointment's details
    # path('summary-report/', views.summary_report_adm_view, name="summary_report.html"),
    path('download-report/', views.dl_report_adm_action, name="dl_report_adm_action"),
    # Admin - Patients
    path('view/pacientes/', views.paciente_adm_view, name='paciente_adm.html'),  # pacientes section
    path('approve/pacientes/', views.approve_pac_adm_view, name='approve_pac.html'),  # Approve pacientes accounts
    path('approve/pacientes=<int:pk>', views.approve_pac_adm_action, name='approve_pac_action'), # Approve pacientes action
    path('view/all-pacientes/', views.all_pac_adm_view, name='view_all_pac.html'),  # View all pacientes accounts
    # Admin - Profesionales
    path('view/profesionales/', views.profesional_adm_view, name='profesional_adm.html'),  # profesionales section
    path('approve/profesionales/', views.approve_prof_adm_view, name='approve_prof.html'),  # Approve profesionales accounts
    path('approve/profesionales=<int:pk>', views.approve_prof_adm_action, name='approve_prof_action'), # Approve profesionales action
    path('view/all-profesionales/', views.all_prof_adm_view, name='view_all_prof.html'),  # View all profesionales accounts
    # Admin - Admin
    path('view/admins/', views.admin_adm_view, name='admin_adm.html'),  # Admins section
    path('approve/admins/', views.approve_adm_adm_view, name='approve_adm.html'),  # Approve profesionales accounts
    path('approve/admin=<int:pk>', views.approve_adm_adm_action, name='approve_adm_action'),  # Approve admin action
    path('view/all-admins/', views.all_adm_adm_view, name='view_all_adm.html'),  # View all profesionales accounts
    # Statistics
    path('view/statistics/', views.statistics_adm_view, name='view_statistics_adm.html'),  # View appointments statistics
    path('data', views.pivot_data, name='pivot_data'),

    # Patients
    path('register/pacientes/', views.register_pac_view, name='register_pac.html'),  # pacientes registration
    path('login/pacientes/', views.login_pac_view, name='login_pac.html'),  # pacientes login
    path('profile/pacientes/', views.profile_pac_view, name='profile_pac.html'),  # pacientes profile
    path('book-appointment-pac/', views.book_app_pac_view, name='book_app_pac.html'),  # Book an appointment
    path('pacientes/appointments', views.app_pac_view, name='view_app_pac.html'),  # View pending appointments
    path('pacientes/appointments/all', views.all_app_pac_view, name='view_all_app_pac.html'),  # View pending appointments
    path('pac-appointment/details/<int:pk>', views.app_details_pac_view, name='view_app_details_pac.html'),  # View appointment details
    path('pacientes/join-meeting/', views.join_meeting_pac_view, name='join_meeting_pac.html'),  # Join meeting
    path('appointment/report/<int:pk>', views.app_report_pac_view, name='app_report_pac.html'),  # View appointment reports
    path('pacientes/feedback/', views.feedback_pac_view, name='feedback_pac.html'),

    # Profesionales
    path('register/profesionales/', views.register_prof_view, name='register_prof.html'),  # Register profesionales
    path('login/profesionales/', views.login_prof_view, name='login_prof.html'),  # Login profesionales
    path('profile/profesionales/', views.profile_prof_view, name='profile_prof.html'),  # profesionales profile
    path('dashboard/profesionales/', views.dashboard_prof_view, name='dashboard_prof.html'),  # profesionales dashboard
    path('profesionales/your-appointments/', views.all_app_prof_view, name='view_app_prof.html'),  # View profesionales's appointments
    path('profesionales/appointment-details/<int:pk>', views.app_details_prof_view, name='view_app_details_prof.html'),  # profesionales appointment's details
    path('appointment/<int:pk>/<str:link>', views.add_link_prof_action, name='add_link_prof_action'),  # Add link to appointment
    path('profesionales/appointment/get=<int:pk>', views.get_link_prof_action, name='get_link_prof_action'),  # profesionales get appointment link action
    path('profesionales/appointment/complete=<int:pk>', views.complete_app_prof_action, name='complete_app_prof_action'),  # Complete appointment action
    path('profesionales/approved-appointments/', views.approved_app_prof_view, name='view_approved_app_prof.html'),
    path('profesionales/approved-appointment-details/<int:pk>', views.approved_app_details_prof_view, name='view_approved_app_details_prof.html'),
    path('profesionales/feedback/', views.feedback_prof_view, name='feedback_prof.html'),

    # Report (global)
    path('download/report/id=<int:pk>', views.dl_app_report_action, name="dl_app_report_action"),
    # Download report action
]