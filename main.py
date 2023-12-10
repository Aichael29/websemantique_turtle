import pandas as pd
from rdflib import Graph, Literal, BNode, Namespace, RDF, RDFS, URIRef

# Créer un espace de noms RDF
my_ns = Namespace("http://example.org/")

# Créer un graph RDF
g = Graph()

# Lire le fichier CSV
df = pd.read_csv(r'C:\Users\dell latitude 7400\Desktop\web_semantique\Morocain_food_02.csv', sep=';', encoding='ISO-8859-1')

# Parcourir les lignes du dataframe
for index, row in df.iterrows():
    # Créer une ressource pour chaque recette
    recipe = URIRef(my_ns + "recipe_" + str(row['RecipeId']))
    g.add((recipe, RDF.type, my_ns.Recipe))
    g.add((recipe, RDFS.label, Literal(row['Name'])))
    g.add((recipe, my_ns.hasAuthor, Literal(row['AuthorName'])))
    g.add((recipe, my_ns.hasTotalTime, Literal(row['TotalTime'])))
    g.add((recipe, my_ns.hasDescription, Literal(row['Description'])))
    g.add((recipe, my_ns.hasCategory, Literal(row['RecipeCategory'])))
    g.add((recipe, my_ns.hasKeyword, Literal(row['Keywords'])))

    # Pour les listes séparées par des virgules
    categories = [c.strip('"') for c in row['RecipeCategory'].split(',')]
    for category in categories:
        g.add((recipe, my_ns.hasCategory, Literal(category)))

    ingredients = [i.strip('"') for i in row['RecipeIngredientParts'].split(',')]
    for ingredient in ingredients:
        g.add((recipe, my_ns.hasIngredient, Literal(ingredient)))

    instructions = [i.strip('"') for i in row['RecipeInstructions'].split('", "')]
    for instruction in instructions:
        g.add((recipe, my_ns.hasInstructions, Literal(instruction)))

# les triplets RDF dans un fichier Turtle
g.serialize(destination='output.ttl', format='turtle')

