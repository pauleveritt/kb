from sphinx.ext.intersphinx import fetch_inventory
import warnings

uri = 'https://docs.python.org/3.5/'

# Read inventory into a dictionnary
inv = fetch_inventory(warnings, uri, uri + 'objects.inv')
print(inv)