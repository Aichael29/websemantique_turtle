import pandas as pd
from rdflib import Graph, Literal, BNode, Namespace, RDF, RDFS, OWL, URIRef

# Create an RDF namespace
my_ns = Namespace("http://example.org/")

# Create an RDF graph
g = Graph()

# Read the CSV file
df = pd.read_csv(r'C:\Users\dell latitude 7400\Desktop\web_semantique\Morocain_food_02.csv', sep=';', encoding='ISO-8859-1')

# Add RDFS ontology triplets
g.add((my_ns.Recipe, RDF.type, OWL.Class))
g.add((my_ns.hasAuthor, RDF.type, OWL.DatatypeProperty))
g.add((my_ns.hasTotalTime, RDF.type, OWL.DatatypeProperty))
g.add((my_ns.hasDescription, RDF.type, OWL.DatatypeProperty))
g.add((my_ns.hasCategory, RDF.type, OWL.DatatypeProperty))
g.add((my_ns.hasKeyword, RDF.type, OWL.DatatypeProperty))
g.add((my_ns.hasIngredient, RDF.type, OWL.DatatypeProperty))
g.add((my_ns.hasInstructions, RDF.type, OWL.DatatypeProperty))

# Iterate over the rows of the dataframe
for index, row in df.iterrows():
    # Create a resource for each recipe
    recipe = URIRef(my_ns + "recipe_" + str(row['RecipeId']))
    g.add((recipe, RDF.type, my_ns.Recipe))
    g.add((recipe, RDFS.label, Literal(row['Name'])))
    g.add((recipe, my_ns.hasAuthor, Literal(row['AuthorName'])))
    g.add((recipe, my_ns.hasTotalTime, Literal(row['TotalTime'])))
    g.add((recipe, my_ns.hasDescription, Literal(row['Description'])))
    g.add((recipe, my_ns.hasCategory, Literal(row['RecipeCategory'])))
    g.add((recipe, my_ns.hasKeyword, Literal(row['Keywords'])))

    # For comma-separated lists
    categories = [c.strip('"') for c in row['RecipeCategory'].split(',')]
    for category in categories:
        g.add((recipe, my_ns.hasCategory, Literal(category)))

    ingredients = [i.strip('"') for i in row['RecipeIngredientParts'].split(',')]
    for ingredient in ingredients:
        g.add((recipe, my_ns.hasIngredient, Literal(ingredient)))

    instructions = [i.strip('"') for i in row['RecipeInstructions'].split('", "')]
    for instruction in instructions:
        g.add((recipe, my_ns.hasInstructions, Literal(instruction)))

# Query the RDF graph without inferencing
query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX my_ns: <http://example.org/>

    SELECT ?recipe ?label
    WHERE {
        ?recipe rdf:type my_ns:Recipe .
        ?recipe rdfs:label ?label .
    }
"""

# Execute the query
result = g.query(query)

# Display the results
for row in result:
    print(f"Recipe: {row['recipe']}, Label: {row['label']}")
g.serialize(destination='output_with_ontology.ttl', format='turtle')