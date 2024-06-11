# RPCW2024-Recurso

Para criar o ficheiro books_base.ttl eu utilizei o script novo.py, utilzando apenas o primeiro elemento da lista forneceida no json para tal.
o books_id foi utilizado como item_uri uma vez que era o que aparecia com menos repetiçoes. Pensei em utilizar o valor ibsn mas o valor 9999999 aparecia muitas vezes repetida.
grande parte dos valores lá existentes utilzei como sendo uma data property, os que foram tratados de maneira diferente foram apenas o genero o author e a serie uma vez que este podiam ser repetidos para varios livros.
Pensei fazer o mesmo tratamento para as personagens mas devido ao facto de personagens com nomes iguais em series diferentes poderem aparecer decidi manter estas dados como data property.

o ficheiro novo.py foi o que utilizei para gerer a ontologia do ficheiro json fornecido que lê item a item e vai adicionando os valors aos grafo a medida que o faz, tendo em conta as restirções prévias.
aqui existe um tratamento especial aos autores, generos, serie e personagens, uma vez que podem aparecer como listas.
