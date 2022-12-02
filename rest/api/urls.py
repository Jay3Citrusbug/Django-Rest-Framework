from django.urls import path
from .import views



urlpatterns = [
    
    # path('stu_info/',views.student_detail),
    path('stu_data/',views.StudentApi.as_view()),
    path('stu_data/<int:pk>',views.StudentApi.as_view()),
    path('stu_list/',views.StudentList.as_view()),
   
    ]
