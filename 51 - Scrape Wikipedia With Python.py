import wikipedia as wiki

wiki.set_lang("en")

print(wiki.search("Python"))
print(wiki.suggest("Pyth"))

print(wiki.summary("Python (programming language)", sentences=3))

p = wiki.page("Python (programming language)")

print(p.title)
print(p.url)
print(p.content)
print(p.images[:3])
print(p.links[:10])