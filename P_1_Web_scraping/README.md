# Formation Developpeuse application -Python
# Projet_2  Web-scrapping

 Fichiers category.py & scrapBooks.py (dans la répertoire libScrapBooks) contiennent les fonctions de scraping du site exemple http://books.toscrape.com/index.html

le fichier category.py extrait les données des 1000 livres du site et les enregistre dans des fichiers csv (un fichier par catégorie de livres: category_name.csv). Tous ces fichiers csv sont rangés dans un dossier csv_files. Les images des livres sont également téléchargées et stockées dans un dossier pictures dans ce même répertoire.

Enregistrer l'ensemble des fichiers dans un dossier local de votre choix.

Dans le terminal se mettre dans ce dossier local

Mise en place du projet :

1. Création d'un environnement virtuel
    
    python<version> -m venv nom_env_virtuel
    source nom_env_virtuel/bin/activate

2. Installation des packages
    
    pip<version> install -r requirements.txt

3. Execution du script

    python<version> main.py