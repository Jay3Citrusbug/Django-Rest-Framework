from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from .import views



urlpatterns = [
    
    # path('stu_info/',views.student_detail),
    path('stu_data/',views.StudentApi.as_view()),
    path('stu_data/<int:pk>',views.StudentApi.as_view()),
    # path('stu_list/',views.StudentList.as_view()),
    # path('gettoken/',obtain_auth_token)
    path('reg_data/',views.regiuser.as_view()),
    path('log_data/',views.loginuser.as_view())
  
   
    ]
