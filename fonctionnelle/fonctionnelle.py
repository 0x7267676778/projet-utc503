recettes = {
    "Pizza": {"farine", "eau", "sel", "levure", "tomate", "fromage"},
    "Salade": {"laitue", "tomate", "concombre", "vinaigre", "huile"},
    "Pâtes Carbonara": {"pates", "creme", "lardons", "fromage", "sel", "poivre"},
    "Omelette": {"oeufs", "sel", "poivre", "fromage"},
    "Sandwich Jambon-Beurre": {"pain", "beurre", "jambon"}
}

def recettes_possibles(list_ingr):
	return list(map(lambda r: r[0], filter(lambda r: r[1].issubset(list_ingr), recettes.items())))

ingredients_utilisateur = {"pain", "beurre", "jambon"}
print(recettes_possibles(ingredients_utilisateur))

