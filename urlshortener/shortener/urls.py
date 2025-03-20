from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.ShortenURLView.as_view(), name='shorten'),
    path('<str:short_code>/', views.URLDetailView.as_view(), name='url_detail'),
    path('r/<str:short_code>/', views.URLRedirectView.as_view(), name='redirect'),
    path('stats/<str:short_code>/', views.URLStatsView.as_view(), name='stats'),
]