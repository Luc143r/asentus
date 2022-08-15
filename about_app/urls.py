from django.urls import path, include
from rest_framework import routers
from . import views
from .views import ProductViewSet, SubViewSet, TeamViewSet, FeedbackViewSet


router = routers.DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"subscriptions", SubViewSet)
router.register(r"team", TeamViewSet)
router.register(r"feedback", FeedbackViewSet)


urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("about/", views.about_page, name="about_page"),
    path("about/team<int:pk>", views.team_detail, name="team_detail"),
    path("contact/", views.contact_page, name="contact_page"),
    path("faq/", views.faq_page, name="faq_page"),
    path("price/", views.price_page, name="price_page"),
    path("price/<int:pk>/", views.subscriptions_detail, name="sub_detail"),
    path("product/", views.product_page, name="product_page"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("feedback/", views.feedback_page, name="feedback_page"),
    # API urls
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
