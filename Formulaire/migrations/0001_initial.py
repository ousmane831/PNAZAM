# Generated by Django 5.2.3 on 2025-06-18 21:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Enquete",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_enquete", models.DateField(verbose_name="Date de l'enquête")),
                (
                    "latitude",
                    models.DecimalField(
                        decimal_places=7, max_digits=10, verbose_name="Latitude (x,y °)"
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        decimal_places=7,
                        max_digits=10,
                        verbose_name="Longitude (x,y °)",
                    ),
                ),
                ("altitude", models.IntegerField(verbose_name="Altitude (m)")),
                ("precision", models.IntegerField(verbose_name="Précision (m)")),
                (
                    "departement",
                    models.CharField(max_length=100, verbose_name="Département"),
                ),
                ("commune", models.CharField(max_length=100, verbose_name="Commune")),
                ("quartier", models.CharField(max_length=100, verbose_name="Quartier")),
                (
                    "prenom_enqueteur",
                    models.CharField(
                        max_length=100, verbose_name="Prénom(s) de l'enquêteur"
                    ),
                ),
                (
                    "nom_enqueteur",
                    models.CharField(max_length=100, verbose_name="Nom de l'enquêteur"),
                ),
                (
                    "prenom_proprietaire",
                    models.CharField(
                        max_length=100, verbose_name="Prénom(s) du propriétaire"
                    ),
                ),
                (
                    "nom_proprietaire",
                    models.CharField(
                        max_length=100, verbose_name="Nom du propriétaire"
                    ),
                ),
                (
                    "prenom_chef_atelier",
                    models.CharField(
                        max_length=100, verbose_name="Prénom(s) du chef d'atelier"
                    ),
                ),
                (
                    "nom_chef_atelier",
                    models.CharField(
                        max_length=100, verbose_name="Nom du chef d'atelier"
                    ),
                ),
                (
                    "telephone_chef",
                    models.CharField(
                        max_length=20,
                        verbose_name="Numéro de téléphone du chef d'atelier",
                    ),
                ),
                (
                    "sexe",
                    models.CharField(
                        choices=[("M", "Masculin"), ("F", "Féminin")],
                        max_length=1,
                        verbose_name="Sexe",
                    ),
                ),
                ("date_naissance", models.DateField(verbose_name="Date de naissance")),
                (
                    "cni",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        verbose_name="Numéro d'identification nationale (CNI)",
                    ),
                ),
                (
                    "niveau_etude",
                    models.CharField(
                        choices=[
                            ("aucun", "Aucun"),
                            ("coranique", "Ecole coranique"),
                            ("primaire", "Primaire"),
                            ("secondaire", "Secondaire"),
                            ("moyen", "Moyen"),
                            ("superieur", "Supérieur"),
                            ("autre", "Autre à préciser"),
                        ],
                        max_length=20,
                        verbose_name="Niveau d'étude",
                    ),
                ),
                (
                    "autre_niveau_etude",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Lequel autre ? (niveau étude)",
                    ),
                ),
                (
                    "profession",
                    models.CharField(
                        max_length=100, verbose_name="Quelle est votre profession?"
                    ),
                ),
                (
                    "type_activite",
                    models.CharField(
                        choices=[
                            ("mecanique", "mécanique"),
                            ("tolerie", "tôlerie"),
                            ("peinture", "peinture"),
                            ("menuiserie", "menuiserie"),
                            ("pieces_detachees", "vente de pièces détachées"),
                            ("electricite", "électricité"),
                            ("autre", "Autre à préciser"),
                        ],
                        max_length=20,
                        verbose_name="Type d'activité",
                    ),
                ),
                (
                    "autre_activite",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Lequel autre ? (activité)",
                    ),
                ),
                (
                    "revenu_journalier",
                    models.CharField(
                        choices=[
                            ("moins_5000", "Moins de 5 000"),
                            ("5000_10000", "5 000-10 000"),
                            ("10000_15000", "10 000-15 000"),
                            ("plus_15000", "Plus de 15 000"),
                        ],
                        max_length=20,
                        verbose_name="Revenu journalier",
                    ),
                ),
                (
                    "revenu_mensuel",
                    models.CharField(
                        choices=[
                            ("moins_50000", "Moins de 50 000"),
                            ("50000_100000", "50 000-100 000"),
                            ("100000_200000", "100 000-200 000"),
                            ("plus_200000", "Plus de 200 000"),
                        ],
                        max_length=20,
                        verbose_name="Revenu mensuel",
                    ),
                ),
                (
                    "statut_occupation",
                    models.CharField(
                        choices=[
                            ("proprietaire_exploitant", "Propriétaire Exploitant"),
                            (
                                "proprietaire_non_exploitant",
                                "Propriétaire non exploitant",
                            ),
                            ("coproprietaire", "Copropriétaire"),
                            (
                                "exploitant_non_proprietaire",
                                "Exploitant non propriétaire",
                            ),
                        ],
                        max_length=30,
                        verbose_name="Statut d'occupation",
                    ),
                ),
                (
                    "statut_non_proprietaire",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("locataire", "Locataire"),
                            ("occupation_gratuite", "Occupation gratuite"),
                            ("autre", "Autre à préciser"),
                        ],
                        max_length=20,
                        verbose_name="Statut si non propriétaire",
                    ),
                ),
                (
                    "autre_statut_non_proprietaire",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Lequel Autre ? (statut non propriétaire)",
                    ),
                ),
                (
                    "loyer_mensuel",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Loyer mensuel (si locataire)",
                    ),
                ),
                (
                    "annee_installation",
                    models.IntegerField(verbose_name="Année d'installation"),
                ),
                (
                    "acquisition_site",
                    models.CharField(
                        choices=[
                            ("occupation_spontanee", "Occupation spontanée"),
                            ("achat", "Achat"),
                            ("affectation_commune", "Affectation de la commune"),
                            ("heritage", "Héritage"),
                            ("don", "Don"),
                            ("autre", "autres à préciser"),
                        ],
                        max_length=20,
                        verbose_name="Mode d'acquisition du site",
                    ),
                ),
                (
                    "autre_acquisition",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Lequel Autre ? (acquisition)",
                    ),
                ),
                ("deja_deguerpi", models.BooleanField(verbose_name="Déjà déguerpi ?")),
                (
                    "lieu_provenance",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        verbose_name="Lieu de provenance (si déguerpi)",
                    ),
                ),
                (
                    "meilleur_site",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("nouveau", "le nouveau site"),
                            ("ancien", "l'ancien site"),
                        ],
                        max_length=10,
                        verbose_name="Meilleur site selon vous",
                    ),
                ),
                (
                    "menaces_expulsion",
                    models.BooleanField(verbose_name="Menaces d'expulsion ?"),
                ),
                (
                    "auteur_menaces",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="Auteur des menaces"
                    ),
                ),
                (
                    "nature_juridique",
                    models.CharField(
                        choices=[
                            ("titre_foncier", "Titre foncier"),
                            ("bail", "Bail"),
                            ("occupation_spontanee", "Occupation spontanée"),
                            (
                                "autorisation_temporaire",
                                "Autorisation d'occupation temporaire",
                            ),
                            ("autre", "Autre à préciser"),
                        ],
                        max_length=25,
                        verbose_name="Nature juridique du lieu",
                    ),
                ),
                (
                    "autre_nature_juridique",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Lequel Autre ? (nature juridique)",
                    ),
                ),
                (
                    "superficie_atelier",
                    models.IntegerField(verbose_name="Superficie de l'atelier (m²)"),
                ),
                (
                    "statut_activite",
                    models.CharField(
                        choices=[
                            (
                                "formelle",
                                "Formelle (NINEA, registre de commerce, etc.)",
                            ),
                            ("informelle", "Informelle"),
                        ],
                        max_length=10,
                        verbose_name="Statut de l'activité",
                    ),
                ),
                (
                    "activite_principale",
                    models.CharField(
                        choices=[
                            ("mecanique_generale", "Mécanique générale"),
                            ("froid_climatisation", "Froid & climatisation"),
                            ("electricite_automobile", "Électricité automobile"),
                            ("tolerie_peinture", "Tôlerie-peinture"),
                            ("diagnostic_electronique", "Diagnostic électronique"),
                            ("autre", "Autre à préciser"),
                        ],
                        max_length=25,
                        verbose_name="Activité principale",
                    ),
                ),
                (
                    "autre_activite_principale",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Lequel Autre ? (activité principale)",
                    ),
                ),
                (
                    "nombre_total_personnes",
                    models.IntegerField(
                        verbose_name="Nombre total de personnes dans l'atelier"
                    ),
                ),
                (
                    "nombre_proprietaires",
                    models.IntegerField(verbose_name="Nombre de propriétaires"),
                ),
                (
                    "nombre_ouvriers",
                    models.IntegerField(verbose_name="Nombre d'ouvriers"),
                ),
                (
                    "nombre_apprentis",
                    models.IntegerField(verbose_name="Nombre d'apprentis"),
                ),
                (
                    "nombre_stagiaires",
                    models.IntegerField(verbose_name="Nombre de stagiaires"),
                ),
                (
                    "formation_professionnelle",
                    models.BooleanField(verbose_name="Formation professionnelle ?"),
                ),
                (
                    "ecole_formation",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        verbose_name="École/établissement de formation",
                    ),
                ),
                (
                    "formation_ouvriers",
                    models.CharField(
                        choices=[
                            ("aucune", "Aucune"),
                            ("sur_le_tas", "Formation sur le tas"),
                            ("technique_courte", "Formation technique courte"),
                            ("diplome_technique", "Diplôme technique/professionnel"),
                        ],
                        max_length=20,
                        verbose_name="Formation des ouvriers/apprentis",
                    ),
                ),
                (
                    "nombre_personnes_formees",
                    models.IntegerField(verbose_name="Nombre de personnes formées"),
                ),
                (
                    "duree_apprentissage",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Durée moyenne de l'apprentissage",
                    ),
                ),
                (
                    "electricite",
                    models.BooleanField(default=False, verbose_name="Électricité"),
                ),
                (
                    "eau_courante",
                    models.BooleanField(default=False, verbose_name="Eau courante"),
                ),
                (
                    "espace_stockage",
                    models.BooleanField(
                        default=False, verbose_name="Espace de stockage"
                    ),
                ),
                (
                    "materiel_levage",
                    models.BooleanField(
                        default=False, verbose_name="Matériel de levage"
                    ),
                ),
                (
                    "banc_diagnostic",
                    models.BooleanField(
                        default=False, verbose_name="Banc de diagnostic électronique"
                    ),
                ),
                (
                    "outillage_specialise",
                    models.BooleanField(
                        default=False, verbose_name="Outillage spécialisé"
                    ),
                ),
                (
                    "type_outillage",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        verbose_name="Type d'outillage spécialisé",
                    ),
                ),
                (
                    "acces_internet",
                    models.BooleanField(verbose_name="Accès à internet/smartphone"),
                ),
                (
                    "besoin_diagnostic",
                    models.BooleanField(
                        default=False, verbose_name="Diagnostic électronique"
                    ),
                ),
                (
                    "besoin_vehicules_hybrides",
                    models.BooleanField(
                        default=False, verbose_name="Véhicules hybrides/électriques"
                    ),
                ),
                (
                    "besoin_gestion_atelier",
                    models.BooleanField(
                        default=False, verbose_name="Gestion d'atelier"
                    ),
                ),
                (
                    "besoin_relation_client",
                    models.BooleanField(default=False, verbose_name="Relation client"),
                ),
                (
                    "besoin_froid_climatisation",
                    models.BooleanField(
                        default=False, verbose_name="Froid/Climatisation"
                    ),
                ),
                (
                    "autres_besoins_formation",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        verbose_name="Autres besoins (préciser)",
                    ),
                ),
                (
                    "dispose_formaliser",
                    models.BooleanField(
                        verbose_name="Disposé à formaliser l'activité ?"
                    ),
                ),
                (
                    "type_accompagnement",
                    models.TextField(
                        blank=True, verbose_name="Type d'accompagnement nécessaire"
                    ),
                ),
                (
                    "affilie_opa",
                    models.BooleanField(verbose_name="Affilié à une OPA ?"),
                ),
                (
                    "nom_opa",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="Nom de l'OPA"
                    ),
                ),
                (
                    "horaires_occupation",
                    models.CharField(
                        max_length=200, verbose_name="Horaires d'occupation"
                    ),
                ),
                (
                    "impact_environnement",
                    models.CharField(
                        choices=[("positifs", "Positifs"), ("negatifs", "Négatifs")],
                        max_length=10,
                        verbose_name="Impacts sur l'environnement",
                    ),
                ),
                (
                    "avantages_positifs",
                    models.TextField(
                        blank=True,
                        verbose_name="Avantages/Bénéfices (si impacts positifs)",
                    ),
                ),
                (
                    "inconvenients_negatifs",
                    models.TextField(
                        blank=True,
                        verbose_name="Inconvénients/Problèmes (si impacts négatifs)",
                    ),
                ),
                (
                    "genere_dechets",
                    models.BooleanField(verbose_name="Génère des déchets ?"),
                ),
                (
                    "gestion_dechets",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("incineration", "incinération"),
                            ("recyclage", "recyclage"),
                            ("autre", "Autre à préciser"),
                        ],
                        max_length=15,
                        verbose_name="Gestion des déchets",
                    ),
                ),
                (
                    "autre_gestion_dechets",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Lequel autre ? (gestion déchets)",
                    ),
                ),
                (
                    "relations_occupants",
                    models.BooleanField(
                        verbose_name="Relations avec autres occupants ?"
                    ),
                ),
                (
                    "problemes_autorites",
                    models.BooleanField(verbose_name="Problèmes avec les autorités ?"),
                ),
                (
                    "autorite_probleme",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("gouverneur", "Gouverneur"),
                            ("prefet", "Préfet"),
                            ("maire", "Maire"),
                            ("delegue_quartier", "Délégué de quartier"),
                            ("autre", "Autre à préciser"),
                        ],
                        max_length=20,
                        verbose_name="Quelle autorité ?",
                    ),
                ),
                (
                    "autre_autorite",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Lequel autre ? (autorité)",
                    ),
                ),
                (
                    "avantages_commune",
                    models.TextField(
                        blank=True, verbose_name="Avantages pour la commune"
                    ),
                ),
                (
                    "inconvenients_commune",
                    models.TextField(
                        blank=True, verbose_name="Inconvénients pour la commune"
                    ),
                ),
                (
                    "opinion_reglementation",
                    models.TextField(
                        blank=True, verbose_name="Opinion sur la réglementation"
                    ),
                ),
                (
                    "suggestions",
                    models.TextField(blank=True, verbose_name="Suggestions"),
                ),
                (
                    "pret_demenager",
                    models.BooleanField(verbose_name="Prêt à déménager ?"),
                ),
                (
                    "pret_exercer_hors_dakar",
                    models.BooleanField(verbose_name="Prêt à exercer hors Dakar ?"),
                ),
                (
                    "raison_refus_dakar",
                    models.TextField(
                        blank=True, verbose_name="Raison du refus (si non)"
                    ),
                ),
                (
                    "equipements_souhaites",
                    models.TextField(blank=True, verbose_name="Équipements souhaités"),
                ),
                (
                    "difficultes_acces",
                    models.BooleanField(verbose_name="Difficultés d'accès ?"),
                ),
                (
                    "lieu_origine",
                    models.CharField(max_length=200, verbose_name="Lieu d'origine"),
                ),
                (
                    "temps_acces",
                    models.CharField(
                        choices=[
                            ("moins_30min", "moins de 30 minutes"),
                            ("1h", "01 heure de temps"),
                            ("2h", "02 heures de temps"),
                            ("3h", "03 heures de temps"),
                            ("6h", "06 heures de temps"),
                        ],
                        max_length=15,
                        verbose_name="Temps d'accès",
                    ),
                ),
                (
                    "lieu_residence_clientele",
                    models.CharField(
                        max_length=200, verbose_name="Lieu de résidence de la clientèle"
                    ),
                ),
                (
                    "commentaires_supplementaires",
                    models.TextField(
                        blank=True, verbose_name="Commentaires supplémentaires"
                    ),
                ),
                (
                    "commentaire_enqueteur",
                    models.TextField(
                        blank=True, verbose_name="Commentaire de l'enquêteur"
                    ),
                ),
                (
                    "photo_atelier",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="ateliers/",
                        verbose_name="Photo de l'atelier",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "enqueteur",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Enquêteur (système)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Enquête Artisan",
                "verbose_name_plural": "Enquêtes Artisans",
                "ordering": ["-created_at"],
            },
        ),
    ]
