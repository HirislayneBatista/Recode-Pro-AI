-- Consultas base de dados Locadora
use locadora;

-- select aluguel_id from locadora.aluguel;
-- consultar o nome do cliente que fez a locacao numero 1000
select cliente.primeiro_nome, cliente.ultimo_nome
from cliente, aluguel
where aluguel.aluguel_id = 1000
and cliente.cliente_id = aluguel.cliente_id;

-- consultar quais as cidades e seu pais correspondente que pertencem a um pais que inicie com a letra E
select cidade.cidade, pais.pais
from cidade, pais
where pais.pais like 'E%'
and cidade.pais_id = pais.pais_id;

select count(filme.titulo) as 'Classificado_como_G_OU_PG', categoria.nome
from filme, categoria, filme_categoria
where (filme.classificacao like 'G' or filme.classificacao like 'PG')
and categoria.categoria_id = filme_categoria.categoria_id
and filme.filme_id = filme_categoria.filme_id
GROUP BY categoria.categoria_id;

-- resolucao professor:
SELECT CLIENTE.PRIMEIRO_NOME, aluguel.aluguel_id
FROM CLIENTE,ALUGUEL
WHERE ALUGUEL.ALUGUEL_ID = 1000
AND CLIENTE.CLIENTE_ID = ALUGUEL.CLIENTE_ID;
 
SELECT C.CIDADE, P.PAIS FROM PAIS P, CIDADE C WHERE P.PAIS_ID = C.PAIS_ID AND P.PAIS LIKE 'E%';
 
SELECT COUNT(F.TITULO) as 'Total Filme', C.NOME
FROM FILME F, FILME_CATEGORIA FC,CATEGORIA C
WHERE F.FILME_ID = FC.FILME_ID
AND C.CATEGORIA_ID = FC.CATEGORIA_ID
AND F.CLASSIFICACAO ='G' OR 'PG'
GROUP BY C.CATEGORIA_ID;

-- conclusao: após correção, percebi que confundi somente um pouco as relações entre as chaves

