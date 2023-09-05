from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    path('student_create/', views.StudentCreate.as_view()),
    path('student_retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    path('student_update/<int:pk>/', views.StudentUpdate.as_view()),
    path('student_destroy/<int:pk>/', views.StudentDestroy.as_view()),

    path('student_list_create/', views.StudentListCreate.as_view()),
    path('student_retrieve_update/<int:pk>/', 
         views.StudentRetrieveUpdate.as_view()),
    path('student_retrieve_destroy/<int:pk>/', 
         views.StudentRetrieDestroy.as_view()),
    path('student_retrieve_update_destroy/<int:pk>/', 
         views.StudentRetrieUpdateDestroy.as_view()),
]

