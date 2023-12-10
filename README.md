# Projet Web Sémantique - Conversion de Recettes en RDF

Ce projet propose un script Python (`main.py`) pour convertir des données de recettes à partir d'un fichier CSV en format RDF (Resource Description Framework). L'objectif est de fournir une représentation structurée des recettes utilisant des triplets RDF pour une utilisation ultérieure dans des applications web sémantiques.

## Dépendances

- pandas
- rdflib

Installez les dépendances en utilisant la commande suivante :

```bash
pip install pandas rdflib
```

## Utilisation

1. Clonez le dépôt :

```bash
git clone https://github.com/Aichael29/websemantique_turtle.git
cd websemantique_turtle
```

2. Assurez-vous que votre fichier CSV est correctement formaté et mettez à jour le chemin du fichier dans `main.py` :

```python
df = pd.read_csv('chemin/vers/votre/fichier.csv', sep=';', encoding='ISO-8859-1')
```

3. Exécutez le script :

```bash
python main.py
```

## Fonctionnement

Le script effectue les étapes suivantes :

1. Crée un espace de noms RDF.
2. Lit les données du fichier CSV.
3. Parcourt les lignes et crée des triplets RDF pour chaque recette.
4. Sérialise le graphe RDF dans un fichier Turtle (`output.ttl`).

## Schéma RDF

Le script utilise un schéma RDF simple avec des propriétés telles que `Recipe`, `hasAuthor`, `hasTotalTime`, `hasDescription`, `hasCategory`, `hasKeyword`, `hasIngredient`, et `hasInstructions`.

## Exemple

Un exemple de triplet RDF pour une recette :

```turtle
<http://example.org/recipe_123> rdf:type <http://example.org/Recipe> .
<http://example.org/recipe_123> rdfs:label "Spaghetti Bolognese" .
<http://example.org/recipe_123> <http://example.org/hasAuthor> "John Doe" .
<http://example.org/recipe_123> <http://example.org/hasTotalTime> "60 minutes" .
<http://example.org/recipe_123> <http://example.org/hasDescription> "Plat de pâtes italien classique..." .
<http://example.org/recipe_123> <http://example.org/hasCategory> "Pâtes" .
<http://example.org/recipe_123> <http://example.org/hasKeyword> "Italien, Dîner, Plat principal" .
<http://example.org/recipe_123> <http://example.org/hasIngredient> "Spaghetti" .
<http://example.org/recipe_123> <http://example.org/hasInstructions> "Faire bouillir l'eau, cuire les spaghetti, faire dorer la viande, ajouter la sauce..." .
```

## Sortie

Les triplets RDF résultants seront stockés dans un fichier Turtle nommé `output.ttl` dans le même répertoire que le script.
