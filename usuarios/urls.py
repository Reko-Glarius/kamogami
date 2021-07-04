from django.urls import include, path
from django.contrib.auth import views as auth_views
from usuarios import views

urlpatterns = [
    path("registro/", views.registro, name="register"),
    path("perfil/", views.perfil, name="perfil"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="usuarios/inicioseccion.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="index"),
        name="logout",
    ),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="usuarios/recuperarcontrasena.html"),
        name="reset_password",
    ),
    path(
        "reset_password/sent",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="usuarios/cambiocontrasena.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    )
]