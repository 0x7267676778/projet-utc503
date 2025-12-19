recette(pizza, [farine, eau, sel, levure, tomate, fromage]).
recette(salade, [laitue, tomate, concombre, vinaigre, huile]).
recette(pates_carbonara, [pates, creme, lardons, fromage, sel, poivre]).
recette(omelette, [oeufs, sel, poivre, fromage]).
recette(sandwich_jambon_beurre, [pain, beurre, jambon]).

recette_possible(IngredientsDispo, Recette) :-
    recette(Recette, IngredientsRecette),
    subset(IngredientsRecette, IngredientsDispo).
