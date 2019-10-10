from django.conf.urls import url,include
from . import views
from rest_framework.authtoken import views as v
app_name='app_heisen'
urlpatterns=[url(r'^signup/$',views.SignupAPIView.as_view(),name='signup_api'),
            url(r'^user_list/$',views.UserListAPIView.as_view(),name='user_list_api'),
            url(r'^user_detail/(?P<username>\w+)/$',views.UserDetailAPIView.as_view(),name='user_detail_api'),
            url(r'^question_list/$',views.QuestionListAPIView.as_view(),name='question_list_api'),
            url(r'^question_detail/(?P<id>\w+)/$',views.QuestionDetailAPIView.as_view(),name='question_detail_api',),
            url(r'login/',v.obtain_auth_token),
            url(r'^contest_list/$',views.ContestListAPIView.as_view(),name='contest_list_api'),
            url(r'^contest_detail/(?P<id>\w+)/$',views.ContestDetailAPIView.as_view(),name='contest_detail_api',),
            url(r'^contest/(?P<contest_id>\w+)/participants/$',views.ContestStandingsAPIView.as_view(),name='standings_api',),
            url(r'^(?P<username>\w+)/contests/$',views.UserContestsAPIView.as_view(),name='user_contests_api',),
            ]
