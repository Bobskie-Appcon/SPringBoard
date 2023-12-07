from django.urls import path
from .controllers.StudentController import RegisterStudent, LoginStudent, LogoutStudent, StudentView
from .controllers.TeacherController import RegisterTeacher, LoginTeacher, LogoutTeacher, TeacherView, GetTeacherById
from .controllers.AdminController import RegisterAdmin, LoginAdmin, AdminView, LogoutAdmin

urlpatterns = [
    path('api/register-student', RegisterStudent.as_view()),
    path('api/login-student', LoginStudent.as_view()),
    path('api/active-student', StudentView.as_view()),
    path('api/logout-student', LogoutStudent.as_view()),

    path('api/register-teacher', RegisterTeacher.as_view()),
    path('api/login-teacher', LoginTeacher.as_view()),
    path('api/active-teacher', TeacherView.as_view()),
    path('api/logout-teacher', LogoutTeacher.as_view()),

    path('api/register-admin', RegisterAdmin.as_view()),
    path('api/login-admin', LoginAdmin.as_view()),
    path('api/active-admin', AdminView.as_view()),
    path('api/logout-admin', LogoutAdmin.as_view()),

]
