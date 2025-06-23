from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'enquete'

urlpatterns = [
    # URLs pour la gestion des enquêtes
    path('', views.Accueil, name='accueil'),
    path('listes/', views.liste_enquetes, name='liste_enquetes'),
    path('ajouter/', views.ajouter_enquete, name='ajouter_enquete'),
    path('<int:pk>/', views.detail_enquete, name='detail_enquete'),
    path('<int:pk>/modifier/', views.modifier_enquete, name='modifier_enquete'),
    path('<int:pk>/supprimer/', views.supprimer_enquete, name='supprimer_enquete'),
   
    
     # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
   
    
    # URLs pour les exports et rapports
    path('export/csv/', views.export_enquetes_csv, name='export_csv'),
    path('export/excel/', views.export_enquetes_excel, name='export_excel'),
  
    
   
]

# Configuration pour servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)