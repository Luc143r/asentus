from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('about/', views.about_page, name='about_page'),
    path('about/team<int:pk>', views.team_detail, name='team_detail'),
    path('contact/', views.contact_page, name='contact_page'),
    path('faq/', views.faq_page, name='faq_page'),
    path('price/', views.price_page, name='price_page'),
    path('price/<int:pk>/', views.subscriptions_detail, name='sub_detail'),
    path('product/', views.product_page, name='product_page'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('feedback/', views.feedback_page, name='feedback_page'),
]