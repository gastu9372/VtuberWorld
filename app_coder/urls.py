from app_coder import views
from django.urls import path


urlpatterns = [
    # Inicio
    path('', views.index, name="Inicio"),
    path('about-me', views.about_me, name="about-me"),
    
    # Relacionados a usuarios
    path('users/', views.users, name="Users"),
    
    # Vtuber
    path('vtubers/', views.vtubers, name ="Vtubers"),
    path('formulario/', views.formulario_vtuber_api, name="Formulario"),
    path('del_vtuber/<int:id>', views.eliminar_vtuber, name="Eliminar-vtuber"),
    path('edit_vtuber/<int:pk>', views.editar_vtuber, name="Editar-vtuber"),
    
    # Sesiones
    path("login/", views.login_view, name = "Login" ),
    path("logout/", views.user_logout, name = "Logout" ),
    path("register/", views.register_view, name = "Register" ),
    
    # Perfil
    path("perfil/", views.show_profile, name="Perfil"),
    path("editar-perfil/", views.edit_profile, name="edit-perfil"),
    path("change-password/", views.change_password, name="change-password"),
    
]
