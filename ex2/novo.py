import pandas as pd
from rdflib import Graph, Literal, RDF, RDFS, Namespace, URIRef, BNode
import json, ast, re


LIVROS = Namespace("http://rpcw.di.uminho.pt/2024/LIVROS/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF_NS = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
XML = Namespace("http://www.w3.org/XML/1998/namespace")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
RDFS_NS = Namespace("http://www.w3.org/2000/01/rdf-schema#")


g = Graph()

g.bind("livros", LIVROS)
g.bind("owl", OWL)
g.bind("rdf", RDF_NS)
g.bind("xml", XML)
g.bind("xsd", XSD)
g.bind("rdfs", RDFS_NS)

hasAuthor = LIVROS.hasAuthor
g.add((hasAuthor, RDF.type, OWL.ObjectProperty))
fromSerie = LIVROS.fromSerie
g.add((fromSerie, RDF.type, OWL.ObjectProperty))
fromGenero = LIVROS.fromGenero
g.add((fromGenero, RDF.type, OWL.ObjectProperty))


def clean_and_convert_json(json_str):
    if pd.isna(json_str):
        return []
    if isinstance(json_str, str):
        json_str = re.sub(r"'", r'"', json_str)
        json_str = re.sub(r'\bNone\b', 'null', json_str)
        json_str = re.sub(r'\bTrue\b', 'true', json_str)
        json_str = re.sub(r'\bFalse\b', 'false', json_str)
        return json.loads(json_str)
    return []

lista_generos =  []
lista_personagens = []
dicionario = {}
with open("dataset.json", 'r', encoding='utf-8') as arquivo:
        dicionario = json.load(arquivo)
print(dicionario[0].keys())

def limpa_autores(aut, item_uri):
    for x in aut.split(","):
        autor = x.split("(")[0]
        nome = autor.split(" ")
        nome_p = nome[0]
        apelido = nome[-1]
        autor_id = re.sub(r'\W+', '_', autor.lower())
        autor_uri = LIVROS[autor_id]
        g.add((autor_uri, RDF.type, LIVROS.Author))
        g.add((autor_uri, LIVROS.name_p, Literal(nome_p, datatype=XSD.string)))
        g.add((autor_uri, LIVROS.apelido, Literal(apelido, datatype=XSD.string)))
        g.add((item_uri, LIVROS.hasAuthor, autor_uri))

def limpa_series(x, item_uri):
    serie = x.split("#")[0]
    serie_id = re.sub(r'\W+', '_', serie.lower())
    serie_uri = LIVROS[serie_id]
    g.add((serie_uri, RDF.type, LIVROS.Serie))
    g.add((serie_uri, LIVROS.name, Literal(serie, datatype=XSD.string)))
    g.add((item_uri, LIVROS.fromSerie, serie_uri))

def limpa_genero(x, item_uri):
    lista_real = ast.literal_eval(x)
    for genero in lista_real:
        if genero not in lista_generos:
            lista_generos.append(genero)
            serie_id = re.sub(r'\W+', '_', genero.lower())
            serie_uri = LIVROS[serie_id]
            g.add((serie_uri, RDF.type, LIVROS.Serie))
            g.add((serie_uri, LIVROS.name, Literal(genero, datatype=XSD.string)))
        g.add((item_uri, LIVROS.fromGenero, serie_uri))

def limpa_personagens(x, item_uri):
    lista_real = ast.literal_eval(x)
    for genero in lista_real:
        g.add((item_uri, LIVROS.character, Literal(genero, datatype=XSD.string)))


authors = []
livro = dicionario[1]
bookid = livro["isbn"]
item_uri = LIVROS[bookid]
autores = livro["author"]

g.add((item_uri, RDF.type, LIVROS.Book))
g.add((item_uri, LIVROS.name, Literal(livro['title'], datatype=XSD.string)))

g.add((item_uri, LIVROS.rating, URIRef(livro['rating'])))

g.add((item_uri, LIVROS.language, Literal(livro['language'], datatype=XSD.string)))
g.add((item_uri, LIVROS.description, Literal(livro['description'], datatype=XSD.string)))
g.add((item_uri, LIVROS.pages, Literal(livro['pages'], datatype=XSD.string)))
g.add((item_uri, LIVROS.publishDate, Literal(livro['publishDate'], datatype=XSD.string)))
g.add((item_uri, LIVROS.firstPublishDate, Literal(livro['firstPublishDate'], datatype=XSD.string)))
g.add((item_uri, LIVROS.awards, Literal(livro['awards'], datatype=XSD.string)))
g.add((item_uri, LIVROS.numRatings, Literal(livro['numRatings'], datatype=XSD.string)))
g.add((item_uri, LIVROS.ratingsByStars, Literal(livro['ratingsByStars'], datatype=XSD.string)))
g.add((item_uri, LIVROS.likedPercent, Literal(livro['likedPercent'], datatype=XSD.string)))
g.add((item_uri, LIVROS.coverImg, Literal(livro['coverImg'], datatype=XSD.string)))
g.add((item_uri, LIVROS.bbeScore, Literal(livro['bbeScore'], datatype=XSD.string)))
g.add((item_uri, LIVROS.bbeVotes, Literal(livro['bbeVotes'], datatype=XSD.string)))
g.add((item_uri, LIVROS.price, Literal(livro['price'], datatype=XSD.string)))
limpa_autores(livro["author"], item_uri)
limpa_series(livro["series"], item_uri)
limpa_genero(livro["genres"], item_uri)
limpa_personagens(livro["characters"], item_uri)

    
output_file = "teste.ttl"
with open(output_file, "wb") as f:
    f.write(g.serialize(format='turtle').encode('utf-8'))

print(f"RDF data has been written to {output_file}")
