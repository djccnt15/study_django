from django.urls import path
from . import views

app_name = 'board_qna'

urlpatterns = [
    path('', views.index, name='index'),  # name parameter is to set name of url variable for template
    path('<int:question_id>/', views.detail, name='detail'),  # url for board_qna
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]