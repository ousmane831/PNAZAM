from django.db import models
from django.contrib.auth.models import User

class Enquete(models.Model):
    ### 1. Informations de l'enquête ###
    date_enquete = models.DateField(verbose_name="Date de l'enquête")
    enqueteur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Enquêteur (système)")

    ### 2. Localisation ###
    latitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name="Latitude (x,y °)")
    longitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name="Longitude (x,y °)")
    altitude = models.IntegerField(verbose_name="Altitude (m)")
    precision = models.IntegerField(verbose_name="Précision (m)")
    departement = models.CharField(max_length=100, verbose_name="Département")
    commune = models.CharField(max_length=100, verbose_name="Commune")
    quartier = models.CharField(max_length=100, verbose_name="Quartier")

    ### 6-9. Personnes concernées ###
    prenom_enqueteur = models.CharField(max_length=100, verbose_name="Prénom(s) de l'enquêteur")
    nom_enqueteur = models.CharField(max_length=100, verbose_name="Nom de l'enquêteur")
    prenom_proprietaire = models.CharField(max_length=100, verbose_name="Prénom(s) du propriétaire")
    nom_proprietaire = models.CharField(max_length=100, verbose_name="Nom du propriétaire")
    prenom_chef_atelier = models.CharField(max_length=100, verbose_name="Prénom(s) du chef d'atelier")
    nom_chef_atelier = models.CharField(max_length=100, verbose_name="Nom du chef d'atelier")
    telephone_chef = models.CharField(max_length=20, verbose_name="Numéro de téléphone du chef d'atelier")

    ### 10-13. Démographie ###
    SEXE_CHOICES = [('M', 'Masculin'), ('F', 'Féminin')]
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, verbose_name="Sexe")
    date_naissance = models.DateField(verbose_name="Date de naissance")
    cni = models.CharField(max_length=20, blank=True, verbose_name="Numéro d'identification nationale (CNI)")

    NIVEAU_ETUDE_CHOICES = [
        ('aucun', 'Aucun'),
        ('coranique', 'Ecole coranique'),
        ('primaire', 'Primaire'),
        ('secondaire', 'Secondaire'),
        ('moyen', 'Moyen'),
        ('superieur', 'Supérieur'),
        ('autre', 'Autre à préciser'),
    ]
    niveau_etude = models.CharField(max_length=20, choices=NIVEAU_ETUDE_CHOICES, verbose_name="Niveau d'étude")
    autre_niveau_etude = models.CharField(max_length=100, blank=True, verbose_name="Lequel autre ? (niveau étude)")

    ### 14-18. Activité professionnelle ###
    profession = models.CharField(max_length=100, verbose_name="Quelle est votre profession?")

    TYPE_ACTIVITE_CHOICES = [
        ('mecanique', 'mécanique'),
        ('tolerie', 'tôlerie'),
        ('peinture', 'peinture'),
        ('menuiserie', 'menuiserie'),
        ('pieces_detachees', 'vente de pièces détachées'),
        ('electricite', 'électricité'),
        ('autre', 'Autre à préciser'),
    ]
    type_activite = models.CharField(max_length=20, choices=TYPE_ACTIVITE_CHOICES, verbose_name="Type d'activité")
    autre_activite = models.CharField(max_length=100, blank=True, verbose_name="Lequel autre ? (activité)")

    REVENU_JOURNALIER_CHOICES = [
        ('moins_5000', 'Moins de 5 000'),
        ('5000_10000', '5 000-10 000'),
        ('10000_15000', '10 000-15 000'),
        ('plus_15000', 'Plus de 15 000'),
    ]
    revenu_journalier = models.CharField(max_length=20, choices=REVENU_JOURNALIER_CHOICES, verbose_name="Revenu journalier")

    REVENU_MENSUEL_CHOICES = [
        ('moins_50000', 'Moins de 50 000'),
        ('50000_100000', '50 000-100 000'),
        ('100000_200000', '100 000-200 000'),
        ('plus_200000', 'Plus de 200 000'),
    ]
    revenu_mensuel = models.CharField(max_length=20, choices=REVENU_MENSUEL_CHOICES, verbose_name="Revenu mensuel")

    ### 19-28. Statut d'occupation ###
    STATUT_OCCUPATION_CHOICES = [
        ('proprietaire_exploitant', 'Propriétaire Exploitant'),
        ('proprietaire_non_exploitant', 'Propriétaire non exploitant'),
        ('coproprietaire', 'Copropriétaire'),
        ('exploitant_non_proprietaire', 'Exploitant non propriétaire'),
    ]
    statut_occupation = models.CharField(max_length=30, choices=STATUT_OCCUPATION_CHOICES, verbose_name="Statut d'occupation")

    STATUT_NON_PROPRIETAIRE_CHOICES = [
        ('locataire', 'Locataire'),
        ('occupation_gratuite', 'Occupation gratuite'),
        ('autre', 'Autre à préciser'),
    ]
    statut_non_proprietaire = models.CharField(max_length=20, choices=STATUT_NON_PROPRIETAIRE_CHOICES, blank=True, verbose_name="Statut si non propriétaire")
    autre_statut_non_proprietaire = models.CharField(max_length=100, blank=True, verbose_name="Lequel Autre ? (statut non propriétaire)")

    loyer_mensuel = models.IntegerField(null=True, blank=True, verbose_name="Loyer mensuel (si locataire)")
    annee_installation = models.IntegerField(verbose_name="Année d'installation")

    ACQUISITION_SITE_CHOICES = [
        ('occupation_spontanee', 'Occupation spontanée'),
        ('achat', 'Achat'),
        ('affectation_commune', 'Affectation de la commune'),
        ('heritage', 'Héritage'),
        ('don', 'Don'),
        ('autre', 'autres à préciser'),
    ]
    acquisition_site = models.CharField(max_length=20, choices=ACQUISITION_SITE_CHOICES, verbose_name="Mode d'acquisition du site")
    autre_acquisition = models.CharField(max_length=100, blank=True, verbose_name="Lequel Autre ? (acquisition)")

    deja_deguerpi = models.BooleanField(verbose_name="Déjà déguerpi ?")
    lieu_provenance = models.CharField(max_length=200, blank=True, verbose_name="Lieu de provenance (si déguerpi)")

    MEILLEUR_SITE_CHOICES = [
        ('nouveau', 'le nouveau site'),
        ('ancien', 'l\'ancien site'),
    ]
    meilleur_site = models.CharField(max_length=10, choices=MEILLEUR_SITE_CHOICES, blank=True, verbose_name="Meilleur site selon vous")

    ### 29-36. Situation juridique et activité ###
    menaces_expulsion = models.BooleanField(verbose_name="Menaces d'expulsion ?")
    auteur_menaces = models.CharField(max_length=200, blank=True, verbose_name="Auteur des menaces")

    NATURE_JURIDIQUE_CHOICES = [
        ('titre_foncier', 'Titre foncier'),
        ('bail', 'Bail'),
        ('occupation_spontanee', 'Occupation spontanée'),
        ('autorisation_temporaire', 'Autorisation d\'occupation temporaire'),
        ('autre', 'Autre à préciser'),
    ]
    nature_juridique = models.CharField(max_length=25, choices=NATURE_JURIDIQUE_CHOICES, verbose_name="Nature juridique du lieu")
    autre_nature_juridique = models.CharField(max_length=100, blank=True, verbose_name="Lequel Autre ? (nature juridique)")

    superficie_atelier = models.IntegerField(verbose_name="Superficie de l'atelier (m²)")

    STATUT_ACTIVITE_CHOICES = [
        ('formelle', 'Formelle (NINEA, registre de commerce, etc.)'),
        ('informelle', 'Informelle'),
    ]
    statut_activite = models.CharField(max_length=10, choices=STATUT_ACTIVITE_CHOICES, verbose_name="Statut de l'activité")

    ACTIVITE_PRINCIPALE_CHOICES = [
        ('mecanique_generale', 'Mécanique générale'),
        ('froid_climatisation', 'Froid & climatisation'),
        ('electricite_automobile', 'Électricité automobile'),
        ('tolerie_peinture', 'Tôlerie-peinture'),
        ('diagnostic_electronique', 'Diagnostic électronique'),
        ('autre', 'Autre à préciser'),
    ]
    activite_principale = models.CharField(max_length=25, choices=ACTIVITE_PRINCIPALE_CHOICES, verbose_name="Activité principale")
    autre_activite_principale = models.CharField(max_length=100, blank=True, verbose_name="Lequel Autre ? (activité principale)")

    ### 37-50. Ressources humaines et équipements ###
    nombre_total_personnes = models.IntegerField(verbose_name="Nombre total de personnes dans l'atelier")
    nombre_proprietaires = models.IntegerField(verbose_name="Nombre de propriétaires")
    nombre_ouvriers = models.IntegerField(verbose_name="Nombre d'ouvriers")
    nombre_apprentis = models.IntegerField(verbose_name="Nombre d'apprentis")
    nombre_stagiaires = models.IntegerField(verbose_name="Nombre de stagiaires")

    formation_professionnelle = models.BooleanField(verbose_name="Formation professionnelle ?")
    ecole_formation = models.CharField(max_length=200, blank=True, verbose_name="École/établissement de formation")

    FORMATION_OUVRIERS_CHOICES = [
        ('aucune', 'Aucune'),
        ('sur_le_tas', 'Formation sur le tas'),
        ('technique_courte', 'Formation technique courte'),
        ('diplome_technique', 'Diplôme technique/professionnel'),
    ]
    formation_ouvriers = models.CharField(max_length=20, choices=FORMATION_OUVRIERS_CHOICES, verbose_name="Formation des ouvriers/apprentis")
    nombre_personnes_formees = models.IntegerField(verbose_name="Nombre de personnes formées")
    duree_apprentissage = models.CharField(max_length=100, blank=True, verbose_name="Durée moyenne de l'apprentissage")

    # Équipements (question 48)
    electricite = models.BooleanField(default=False, verbose_name="Électricité")
    eau_courante = models.BooleanField(default=False, verbose_name="Eau courante")
    espace_stockage = models.BooleanField(default=False, verbose_name="Espace de stockage")
    materiel_levage = models.BooleanField(default=False, verbose_name="Matériel de levage")
    banc_diagnostic = models.BooleanField(default=False, verbose_name="Banc de diagnostic électronique")
    outillage_specialise = models.BooleanField(default=False, verbose_name="Outillage spécialisé")
    type_outillage = models.CharField(max_length=200, blank=True, verbose_name="Type d'outillage spécialisé")

    acces_internet = models.BooleanField(verbose_name="Accès à internet/smartphone")

    ### 51-60. Besoins et impacts ###
    besoin_diagnostic = models.BooleanField(default=False, verbose_name="Diagnostic électronique")
    besoin_vehicules_hybrides = models.BooleanField(default=False, verbose_name="Véhicules hybrides/électriques")
    besoin_gestion_atelier = models.BooleanField(default=False, verbose_name="Gestion d'atelier")
    besoin_relation_client = models.BooleanField(default=False, verbose_name="Relation client")
    besoin_froid_climatisation = models.BooleanField(default=False, verbose_name="Froid/Climatisation")
    autres_besoins_formation = models.CharField(max_length=200, blank=True, verbose_name="Autres besoins (préciser)")

    dispose_formaliser = models.BooleanField(verbose_name="Disposé à formaliser l'activité ?")
    type_accompagnement = models.TextField(blank=True, verbose_name="Type d'accompagnement nécessaire")

    affilie_opa = models.BooleanField(verbose_name="Affilié à une OPA ?")
    nom_opa = models.CharField(max_length=200, blank=True, verbose_name="Nom de l'OPA")

    horaires_occupation = models.CharField(max_length=200, verbose_name="Horaires d'occupation")

    IMPACT_ENVIRONNEMENT_CHOICES = [
        ('positifs', 'Positifs'),
        ('negatifs', 'Négatifs'),
    ]
    impact_environnement = models.CharField(max_length=10, choices=IMPACT_ENVIRONNEMENT_CHOICES, verbose_name="Impacts sur l'environnement")
    avantages_positifs = models.TextField(blank=True, verbose_name="Avantages/Bénéfices (si impacts positifs)")
    inconvenients_negatifs = models.TextField(blank=True, verbose_name="Inconvénients/Problèmes (si impacts négatifs)")

    ### 61-72. Gestion des déchets et relations ###
    genere_dechets = models.BooleanField(verbose_name="Génère des déchets ?")

    GESTION_DECHETS_CHOICES = [
        ('incineration', 'incinération'),
        ('recyclage', 'recyclage'),
        ('autre', 'Autre à préciser'),
    ]
    gestion_dechets = models.CharField(max_length=15, choices=GESTION_DECHETS_CHOICES, blank=True, verbose_name="Gestion des déchets")
    autre_gestion_dechets = models.CharField(max_length=100, blank=True, verbose_name="Lequel autre ? (gestion déchets)")

    relations_occupants = models.BooleanField(verbose_name="Relations avec autres occupants ?")
    problemes_autorites = models.BooleanField(verbose_name="Problèmes avec les autorités ?")

    AUTORITE_PROBLEME_CHOICES = [
        ('gouverneur', 'Gouverneur'),
        ('prefet', 'Préfet'),
        ('maire', 'Maire'),
        ('delegue_quartier', 'Délégué de quartier'),
        ('autre', 'Autre à préciser'),
    ]
    autorite_probleme = models.CharField(max_length=20, choices=AUTORITE_PROBLEME_CHOICES, blank=True, verbose_name="Quelle autorité ?")
    autre_autorite = models.CharField(max_length=100, blank=True, verbose_name="Lequel autre ? (autorité)")

    avantages_commune = models.TextField(blank=True, verbose_name="Avantages pour la commune")
    inconvenients_commune = models.TextField(blank=True, verbose_name="Inconvénients pour la commune")
    opinion_reglementation = models.TextField(blank=True, verbose_name="Opinion sur la réglementation")
    suggestions = models.TextField(blank=True, verbose_name="Suggestions")

    pret_demenager = models.BooleanField(verbose_name="Prêt à déménager ?")
    pret_exercer_hors_dakar = models.BooleanField(verbose_name="Prêt à exercer hors Dakar ?")
    raison_refus_dakar = models.TextField(blank=True, verbose_name="Raison du refus (si non)")
    equipements_souhaites = models.TextField(blank=True, verbose_name="Équipements souhaités")

    ### 76-82. Accessibilité et commentaires ###
    difficultes_acces = models.BooleanField(verbose_name="Difficultés d'accès ?")
    lieu_origine = models.CharField(max_length=200, verbose_name="Lieu d'origine")

    TEMPS_ACCES_CHOICES = [
        ('moins_30min', 'moins de 30 minutes'),
        ('1h', '01 heure de temps'),
        ('2h', '02 heures de temps'),
        ('3h', '03 heures de temps'),
        ('6h', '06 heures de temps'),
    ]
    temps_acces = models.CharField(max_length=15, choices=TEMPS_ACCES_CHOICES, verbose_name="Temps d'accès")
    lieu_residence_clientele = models.CharField(max_length=200, verbose_name="Lieu de résidence de la clientèle")

    commentaires_supplementaires = models.TextField(blank=True, verbose_name="Commentaires supplémentaires")
    commentaire_enqueteur = models.TextField(blank=True, verbose_name="Commentaire de l'enquêteur")

    photo_atelier = models.ImageField(upload_to='ateliers/', blank=True, null=True, verbose_name="Photo de l'atelier")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Enquête Artisan"
        verbose_name_plural = "Enquêtes Artisans"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nom_chef_atelier} {self.prenom_chef_atelier} - {self.commune}"