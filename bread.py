#!/usr/bin/env python3

import yaml

def get_recipe(filename):
    f = open(filename, "r")
    s = f.read()
    f.close()
    return(s)

recipe = get_recipe("rhyeSour.yml")
recipe_yaml = yaml.load(recipe)

print(recipe_yaml)
