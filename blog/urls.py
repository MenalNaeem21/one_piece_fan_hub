from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import discussionListView, discussionDetailView, discussionCreateView, add_comment, login_view,logout_view,register
urlpatterns=[
    path('',views.home,name='home'),
    path('discussions/',discussionListView.as_view(),name='discussion-list'),
    path('discussion/<int:pk>/',discussionDetailView.as_view(),name='discussion-detail'),
    path('discussion/new',discussionCreateView.as_view(),name='discussion-create'),
    path('discussion/<int:discussion_id>/comment/',add_comment,name='add-comment'),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout")



]