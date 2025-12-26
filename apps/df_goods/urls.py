from django.urls import re_path

from . import views

app_name = 'df_goods'

urlpatterns = [
    re_path('^$', views.index, name="index"),
    re_path('^list(\d+)_(\d+)_(\d+)/$', views.good_list, name="good_list"),
    re_path('^(\d+)/$', views.detail, name="detail"),
    re_path(r'^search/', views.ordinary_search, name="ordinary_search"),  # 全文检索
]
