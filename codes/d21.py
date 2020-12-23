import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r"\2020d21.txt", "r")
text = (f.read()).strip()
lines = text.split('\n')

all_ingredients = []
allergen_to_ingredient = {}

for line in lines:
    ingredients = line.split(' (contains ')[0].split(' ')
    allergens = line.split(' (contains ')[1][:-1].split(', ')
    all_ingredients = all_ingredients + ingredients

    for allergen in allergens:
        allergen_to_ingredient[allergen] = allergen_to_ingredient.get(
            allergen, set(ingredients)) & set(ingredients)


# ingredient_to_allergens = {}
# for allergen in allergen_to_ingredient.keys():
#     ingredients = allergen_to_ingredient[allergen]
#     for ingredient in ingredients:
#         ingredient_to_allergens[ingredient] = ingredient_to_allergens.get(
#             ingredient, set()) | set({allergen})


sorted_allergen_to_ingredient = collections.deque((sorted(
    [[k, allergen_to_ingredient[k]] for k in allergen_to_ingredient.keys()], key=lambda item: len(item[1]))))
decisive_link = {}
while sorted_allergen_to_ingredient:
    leftmost = sorted_allergen_to_ingredient.popleft()
    if len(leftmost[1]) > 1:
        raise ValueError()
    elif len(leftmost[1]) == 0:
        raise ValueError()
    else:
        new_allergen_to_ingredient = []
        decisive_link[leftmost[0]] = leftmost[1]
        ingredient_inferred = leftmost[1]
        for item in sorted_allergen_to_ingredient:
            print(item)
            updated_item = [item[0], item[1].difference(ingredient_inferred)]
            if len(updated_item[1]) >= 1:
                new_allergen_to_ingredient.append(updated_item)
            # item[1] = item[1].difference(allergen_inferred)
        sorted_allergen_to_ingredient = collections.deque(
            sorted(new_allergen_to_ingredient, key=lambda item: len(item[1])))

ans = []

for ingredient in all_ingredients:
    if {ingredient} not in decisive_link.values():
        ans.append(ingredient)
print(len(ans))

decisive_link_inside_out = {list(v)[0]: k for (k, v) in decisive_link.items()}
print(','.join(sorted([i for i in decisive_link_inside_out.keys()],
                      key=lambda x: decisive_link_inside_out[x])))
