from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),  # 클래스형 뷰를 url과 매핑하려면 {class_type_view}.as_view() 를 붙여서 사용해야 함.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]