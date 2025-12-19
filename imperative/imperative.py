recettes = {
    "Pizza": {"farine", "eau", "sel", "levure", "tomate", "fromage"},
    "Salade": {"laitue", "tomate", "concombre", "vinaigre", "huile"},
    "Pâtes Carbonara": {"pates", "creme", "lardons", "fromage", "sel", "poivre"},
    "Omelette": {"oeufs", "sel", "poivre", "fromage"},
    "Sandwich Jambon-Beurre": {"pain", "beurre", "jambon"}
}

def recettes_possibles(liste_ingr):
	possibles = []
	for nom, ingredients in recettes.items():
		if ingredients.issubset(liste_ingr):
			possibles.append(nom)
	return possibles


ingredients_utilisateur = {"oeufs", "sel", "poivre", "fromage"}
print(recettes_possibles(ingredients_utilisateur))
