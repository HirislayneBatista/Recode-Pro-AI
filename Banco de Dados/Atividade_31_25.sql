-- Mostrando os paises cadastrados
select pais_id from locadora.pais;

-- Quantos paises estão cadastrados
select count(pais) as 'qtde_pais' from locadora.pais;

-- Quantos paises que terminam com a letra A cadastrsdos
select pais as 'paises_termina_com_A' from locadora.pais where pais like 'A%';
select count(pais) as 'paises_termina_com_A' from locadora.pais where pais like 'A%';

-- Listar, sem repetcao, os anos que houveram lancamento de filme
select ano_de_lancamento from locadora.filme;
select distinct ano_de_lancamento from locadora.filme;