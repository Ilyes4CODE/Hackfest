from django.urls import path
from . import views
urlpatterns = [
    path('create_event/', views.Create_Event, name='create_event'),
    path('enroll_event/<str:pk>/', views.Enroll_Event, name='enroll_event'),
    path('create_newsletter/', views.Create_newsletter, name='create_newsletter'),
    path('get_student_tickets/', views.Get_Student_Tickets, name='get_student_tickets'),
    path('get_events/',views.get_events),
    path('get_own_newsletters/',views.Get_Prof_NewsLetters),
    path('Get_all_newslettres/',views.get_all_newslettres)
]