# Weather Data Project

Projet de traitement de données météorologiques avec pipeline ETL (Extract, Transform, Load).

##  Description

Ce projet récupère des données météorologiques depuis l'API Open-Meteo, les nettoie et les transforme en format CSV pour analyse.

##  Structure du projet

```
weatherDataProject/
├── src/
│   ├── extract.py      # Extraction des données depuis l'API
│   ├── transform.py    # Transformation et nettoyage des données
│   └── main.py         # Orchestration du pipeline
├── data/
│   ├── raw/            # Données brutes (JSON)
│   └── processed/      # Données nettoyées (CSV)
├── README.md
├── requirements.txt
└── .gitignore
```

##  Installation

1. Cloner le projet (ou naviguer vers le dossier)

2. Créer un environnement virtuel (optionnel mais recommandé) :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

##  Utilisation

### Exécution complète du pipeline

```bash
python src/main.py
```

Cette commande exécute automatiquement :
1. **Extraction** : Récupération des données depuis l'API Open-Meteo
2. **Transformation** : Nettoyage et conversion en CSV
3. **Vérification** : Confirmation de la création du fichier CSV

### Exécution étape par étape

**Extraction uniquement :**
```bash
python src/extract.py
```

**Transformation uniquement :**
```bash
python src/transform.py
```

##  Données

### Données extraites

- **Source** : API Open-Meteo (https://api.open-meteo.com)
- **Localisation** : Paris, France (latitude: 48.85, longitude: 2.35)
- **Paramètres** :
  - Température à 2m (`temperature_2m`)
  - Humidité relative à 2m (`relative_humidity_2m`)
  - Vitesse du vent à 10m (`wind_speed_10m`)

### Format des données

- **Raw** : JSON (`data/raw/weather_raw.json`)
- **Processed** : CSV (`data/processed/weather_clean.csv`)

### Colonnes du CSV final

- `time` : Date et heure (datetime)
- `temperature_2m` : Température en °C
- `relative_humidity_2m` : Humidité relative en %
- `wind_speed_10m` : Vitesse du vent en km/h



