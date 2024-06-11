# RPCW2024-Recurso

## ex1 
Para criar esta ontologia peguei em elementos de trabalhos que tinha feito préviamente e fui alterando os valores maneualmente até estar satisfeito com o resultado.
Os pontos importantes no texto para além das personagens, Eduardo, Ana, prof. Ratz, Hanna e Carlos, que serão as entidades que compoem a classe de Person é importante salientar as outras entidades:
- Language,
- Course,
- School.
Já que neste contexto se mencioana bastante as linguagens que cada um fala, assim como a que escola/curso pertencem achei que se iriam enquadrar bem estas classes

data properties
são algumas propriedades basicas unica da pessoa,
origem, idade, lingua que fala. não coloquei o nome das pessoas como propriedade uma vez que eram unicos para cada um no exemplo dado, mas coloquei esta propriedade na escola de maneira ao seu identificador ser algo mais simples.

opbjer properties
- aqui estão as relações que as personagens tem umas com as outra(friendsWith)
- em que cursos estoa as nossas personagens(isEnrolledIn)
- que curso ensina(teacherOf)
- e a que escola pertence(teachesCourse)




## ex2
Para criar o ficheiro books_base.ttl eu utilizei o script novo.py, utilzando apenas o segundo elemento da lista forneceida no json para tal.

o books_id foi utilizado como item_uri uma vez que era o que aparecia com menos repetiçoes. Pensei em utilizar o valor ibsn mas o valor 9999999 aparecia muitas vezes repetida.
grande parte dos valores lá existentes utilzei como sendo uma data property, os que foram tratados de maneira diferente foram apenas o genero o author e a serie uma vez que este podiam ser repetidos para varios livros.
Pensei fazer o mesmo tratamento para as personagens mas devido ao facto de personagens com nomes iguais em series diferentes poderem aparecer decidi manter estas dados como data property.

o ficheiro novo.py foi o que utilizei para gerer a ontologia do ficheiro json fornecido que lê item a item e vai adicionando os valors aos grafo a medida que o faz, tendo em conta as restirções prévias.
aqui existe um tratamento especial aos autores, generos, serie e personagens, uma vez que podem aparecer como listas.
