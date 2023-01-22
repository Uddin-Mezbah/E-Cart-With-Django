from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="Productview"),
    path("checkout/", views.checkout, name="Checkout"),

    path("login/", views.login, name="Login"),
    path("logup/", views.logup, name="Logup"),
    path("logout/", views.logout, name="Logout"),

]
