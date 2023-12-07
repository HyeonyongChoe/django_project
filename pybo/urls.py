from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # question_id = 2 이런식으로 됨
    path('answer/create/<int:question_id>',views.answer_create, name = 'answer_create'),
    path('question/create/',views.question_create,name='question_create')
]
