from django import forms
from .models import Enquete
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect

class EnqueteForm(forms.ModelForm):
    class Meta:
        model = Enquete
        fields = '__all__'
        widgets = {
            # Section 1-2: Informations de base et localisation
            'date_enquete': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'step': '0.000001', 'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'step': '0.000001', 'class': 'form-control'}),
            'altitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'precision': forms.NumberInput(attrs={'class': 'form-control'}),
            'departement': forms.TextInput(attrs={'class': 'form-control'}),
            'commune': forms.TextInput(attrs={'class': 'form-control'}),
            'quartier': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Section 6-9: Personnes concernées
            'prenom_enqueteur': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_enqueteur': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_proprietaire': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_proprietaire': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_chef_atelier': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_chef_atelier': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone_chef': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Section 10-13: Démographie
            'sexe': forms.RadioSelect(choices=Enquete.SEXE_CHOICES),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cni': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau_etude': forms.Select(attrs={'class': 'form-control'}),
            'autre_niveau_etude': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Section 14-18: Activité professionnelle
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'type_activite': forms.Select(attrs={'class': 'form-control'}),
            'autre_activite': forms.TextInput(attrs={'class': 'form-control'}),
            'revenu_journalier': forms.Select(attrs={'class': 'form-control'}),
            'revenu_mensuel': forms.Select(attrs={'class': 'form-control'}),
            
            # Section 19-28: Statut d'occupation
            'statut_occupation': forms.Select(attrs={'class': 'form-control'}),
            'statut_non_proprietaire': forms.Select(attrs={'class': 'form-control'}),
            'autre_statut_non_proprietaire': forms.TextInput(attrs={'class': 'form-control'}),
            'loyer_mensuel': forms.NumberInput(attrs={'class': 'form-control'}),
            'annee_installation': forms.NumberInput(attrs={'class': 'form-control'}),
            'acquisition_site': forms.Select(attrs={'class': 'form-control'}),
            'autre_acquisition': forms.TextInput(attrs={'class': 'form-control'}),
            'lieu_provenance': forms.TextInput(attrs={'class': 'form-control'}),
            'meilleur_site': forms.RadioSelect(choices=Enquete.MEILLEUR_SITE_CHOICES),
            
            # Section 29-36: Situation juridique
            'auteur_menaces': forms.TextInput(attrs={'class': 'form-control'}),
            'nature_juridique': forms.Select(attrs={'class': 'form-control'}),
            'autre_nature_juridique': forms.TextInput(attrs={'class': 'form-control'}),
            'superficie_atelier': forms.NumberInput(attrs={'class': 'form-control'}),
            'statut_activite': forms.RadioSelect(choices=Enquete.STATUT_ACTIVITE_CHOICES),
            'activite_principale': forms.Select(attrs={'class': 'form-control'}),
            'autre_activite_principale': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Section 37-50: Ressources humaines
            'nombre_total_personnes': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_proprietaires': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_ouvriers': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_apprentis': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_stagiaires': forms.NumberInput(attrs={'class': 'form-control'}),
            'ecole_formation': forms.TextInput(attrs={'class': 'form-control'}),
            'formation_ouvriers': forms.Select(attrs={'class': 'form-control'}),
            'nombre_personnes_formees': forms.NumberInput(attrs={'class': 'form-control'}),
            'duree_apprentissage': forms.TextInput(attrs={'class': 'form-control'}),
            'type_outillage': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Section 51-60: Besoins et impacts
            'autres_besoins_formation': forms.TextInput(attrs={'class': 'form-control'}),
            'type_accompagnement': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nom_opa': forms.TextInput(attrs={'class': 'form-control'}),
            'horaires_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'avantages_positifs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'inconvenients_negatifs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            # Section 61-72: Gestion des déchets
            'autre_gestion_dechets': forms.TextInput(attrs={'class': 'form-control'}),
            'autre_autorite': forms.TextInput(attrs={'class': 'form-control'}),
            'avantages_commune': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'inconvenients_commune': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'opinion_reglementation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'suggestions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'raison_refus_dakar': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'equipements_souhaites': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            # Section 76-82: Accessibilité
            'lieu_origine': forms.TextInput(attrs={'class': 'form-control'}),
            'lieu_residence_clientele': forms.TextInput(attrs={'class': 'form-control'}),
            'commentaires_supplementaires': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'commentaire_enqueteur': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo_atelier': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configuration des champs booléens pour utiliser des cases à cocher
        for field_name in ['deja_deguerpi', 'menaces_expulsion', 'formation_professionnelle',
                         'electricite', 'eau_courante', 'espace_stockage', 'materiel_levage',
                         'banc_diagnostic', 'outillage_specialise', 'acces_internet',
                         'besoin_diagnostic', 'besoin_vehicules_hybrides', 'besoin_gestion_atelier',
                         'besoin_relation_client', 'besoin_froid_climatisation', 'dispose_formaliser',
                         'affilie_opa', 'genere_dechets', 'relations_occupants', 'problemes_autorites',
                         'pret_demenager', 'pret_exercer_hors_dakar', 'difficultes_acces']:
            self.fields[field_name].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
            
        # Configuration spéciale pour les choix multiples (équipements)
        self.fields['impact_environnement'].widget = forms.RadioSelect(choices=Enquete.IMPACT_ENVIRONNEMENT_CHOICES)
        self.fields['gestion_dechets'].widget = forms.RadioSelect(choices=Enquete.GESTION_DECHETS_CHOICES)
        self.fields['autorite_probleme'].widget = forms.RadioSelect(choices=Enquete.AUTORITE_PROBLEME_CHOICES)
        self.fields['temps_acces'].widget = forms.RadioSelect(choices=Enquete.TEMPS_ACCES_CHOICES)

    # Validation personnalisée si nécessaire
    def clean(self):
        cleaned_data = super().clean()
        
        # Exemple de validation : Vérifier que si "Autre" est sélectionné, le champ correspondant est rempli
        if cleaned_data.get('niveau_etude') == 'autre' and not cleaned_data.get('autre_niveau_etude'):
            self.add_error('autre_niveau_etude', "Veuillez préciser le niveau d'étude")
            
        if cleaned_data.get('statut_non_proprietaire') == 'autre' and not cleaned_data.get('autre_statut_non_proprietaire'):
            self.add_error('autre_statut_non_proprietaire', "Veuillez préciser le statut")
            
        return cleaned_data
    
    
    
    
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Entrez votre nom d'utilisateur",
            'autofocus': True
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Entrez votre mot de passe"
        })
    )