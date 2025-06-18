from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Count, Avg
import csv
import openpyxl
from .models import Enquete
from .forms import EnqueteForm
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from .serializers import EnqueteSerializer

# Vue pour la liste des enquêtes
def liste_enquetes(request):
    enquetes = Enquete.objects.all().order_by('-created_at')
    return render(request, 'liste.html', {'enquetes': enquetes})

# Vue pour ajouter une enquête
def ajouter_enquete(request):
    if request.method == 'POST':
        form = EnqueteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('enquete:liste_enquetes')
    else:
        form = EnqueteForm()
    return render(request, 'formulaire.html', {'form': form, 'titre': 'Ajouter'})

# Vue pour voir les détails d'une enquête
def detail_enquete(request, pk):
    enquete = get_object_or_404(Enquete, pk=pk)
    return render(request, 'detail.html', {'enquete': enquete})

# Vue pour modifier une enquête
def modifier_enquete(request, pk):
    enquete = get_object_or_404(Enquete, pk=pk)
    if request.method == 'POST':
        form = EnqueteForm(request.POST, request.FILES, instance=enquete)
        if form.is_valid():
            form.save()
            return redirect('enquete:detail_enquete', pk=pk)
    else:
        form = EnqueteForm(instance=enquete)
    return render(request, 'formulaire.html', {'form': form, 'titre': 'Modifier'})

# Vue pour supprimer une enquête
def supprimer_enquete(request, pk):
    enquete = get_object_or_404(Enquete, pk=pk)
    if request.method == 'POST':
        enquete.delete()
        return redirect('enquete:liste_enquetes')
    return render(request, 'supprimer.html', {'enquete': enquete})



from django.shortcuts import render
from .models import Enquete


#connection et déconnexion des utilisateurs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from .forms import LoginForm

class LoginView(View):
    template_name = 'enquete/login.html'
    form_class = LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('enquete:liste_enquetes')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', 'enquete:liste_enquetes')
                return redirect(next_url)
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        return render(request, self.template_name, {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('login')



# Export CSV
def export_enquetes_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="enquetes_artisans.csv"'
    
    writer = csv.writer(response)
    # Écrire l'en-tête
    writer.writerow([
        'Date enquête', 'Commune', 'Quartier', 'Nom chef atelier', 
        'Activité principale', 'Revenu mensuel', 'Statut activité'
    ])
    
    # Écrire les données
    for enquete in Enquete.objects.all():
        writer.writerow([
            enquete.date_enquete,
            enquete.commune,
            enquete.quartier,
            f"{enquete.nom_chef_atelier} {enquete.prenom_chef_atelier}",
            enquete.get_activite_principale_display(),
            enquete.get_revenu_mensuel_display(),
            enquete.get_statut_activite_display(),
        ])
    
    return response

# Export Excel
def export_enquetes_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="enquetes_artisans.xlsx"'
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Enquêtes Artisans"
    
    # En-tête
    columns = [
        'Date enquête', 'Commune', 'Quartier', 'Nom chef atelier', 
        'Téléphone', 'Activité', 'Revenu mensuel', 'Superficie (m²)'
    ]
    ws.append(columns)
    
    # Données
    for enquete in Enquete.objects.all():
        ws.append([
            enquete.date_enquete,
            enquete.commune,
            enquete.quartier,
            f"{enquete.nom_chef_atelier} {enquete.prenom_chef_atelier}",
            enquete.telephone_chef,
            enquete.get_activite_principale_display(),
            enquete.revenu_mensuel,
            enquete.superficie_atelier,
        ])
    
    wb.save(response)
    return response
