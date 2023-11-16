from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login_student',views.login_student, name="login"),
    path('login_college',views.login_college, name="login_college"),
    path('login_manager',views.login_manager, name="login_manager"),
    path('handleLogin',views.handleLogin,name="handleLogin"),
    path('handleLogout',views.handleLogout,name="handleLogout"),
    path('register',views.register,name="register"),
    path('register_college',views.register_college,name="register_college"),
    path('register_manager',views.register_manager,name="register_manager"),
    path('handleSignup',views.handleSignup,name="handleSignup"),
    path('student_dashboard', views.student_dashboard, name='student_dashboad'),
    path('profile', views.profile, name='profile'),
    path('set_route', views.set_route, name='set_route'),
    path('handleRoute',views.handleRoute,name="handleRoute"),
    path('view_route', views.view_route, name='view_route'),
    path('apply_pass', views.apply_pass, name='apply_pass'),
    path('verification',views.verification, name='verification'),
    path('college_verify',views.college_verify, name='college_verify'),
    path('college_verify_reject',views.college_verify_reject, name='college_verify_reject'),
    path('manager_verify',views.manager_verify, name='manager_verify'),
    path('manager_verify_reject',views.manager_verify_reject, name='manager_verify_reject'),
    path('generate_pass',views.generate_pass, name='generate_pass'),
    path('college_dashboard',views.college_dashboard, name='college_dashboard'),
    path('student_verification',views.student_verification, name='student_verification'),
    path('verified_student',views.verified_student, name='verified_student'),
    path('manager_dashboard',views.manager_dashboard, name='manager_dashboard'),
    path('approval',views.approval, name='approval'),
    path('payment',views.payment, name='payment'),
    path('generate',views.generate, name='generate'),
    path('report',views.report, name='report')

]