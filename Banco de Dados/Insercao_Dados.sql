-- Uso do banco de dados 'mercado2'
use mercado2;

-- Visualizando a tabela cliente para inserção de dados
select * from cliente;

insert into cliente (id_cli, nome_cli, endereco_cli, cidade_cli, cep_cli, uf_cli) values
	('01', 'João Silva', 'Rua A, 123', 'São Paulo', '12345-678', 'SP'),
    ('02', 'Maria Souza', 'Avenida B, 456', 'São Paulo', '9876-543', 'SP'),
    ('03', 'Pedro Santos', 'Rua C, 789', 'São Paulo', '24680-135', 'SP');
    
-- Usando o Update para alterar algum valor
update cliente set cep_cli = '98765-432' where id_cli = '02';

-- Inserindo dados as outras tabelas do banco
insert into cliente (id_cli, nome_cli, endereco_cli, cidade_cli, cep_cli, uf_cli) values
    ('04', 'Hirislayne Batista', 'Rua José de Alencar', 'São Luis', '65045-690', 'MA'),
    ('05', 'Ana Oliveira', 'Avenida D, 101', 'São Paulo', '78932-145', 'SP');

INSERT INTO vendedor (ID_VENDEDOR, NOME_VEND, SALARIO_VEND, COMISSAO) VALUES
    (1, 'Carlos Mendes', 3500.00, 5.0),
    (2, 'Fernanda Lima', 4200.00, 6.5),
    (3, 'Ricardo Alves', 3800.00, 4.5),
    (4, 'Juliana Souza', 4000.00, 5.2),
    (5, 'Marcos Ferreira', 3700.00, 4.8);
    
INSERT INTO PRODUTO (ID_PRODUTO, UNIDADE, DESCRICAO, VAL_UNIT) VALUES
	(101, 'KG', 'Arroz', 5.50),
	(102, 'UN', 'Leite', 4.20),
	(103, 'UN', 'Óleo de Soja', 7.80),
	(104, 'KG', 'Açúcar', 3.90),
	(105, 'UN', 'Detergente', 2.30);

INSERT INTO pedido (NUM_PEDIDO, ID_CLI, ID_VENDEDOR, PRAZO_ENTREGA) VALUES
    (1001, 1, 2, '2025-02-05'),
    (1002, 2, 3, '2025-02-07'),
    (1003, 3, 1, '2025-02-10'),
    (1004, 4, 5, '2025-02-12'),
    (1005, 5, 4, '2025-02-15');

INSERT INTO ITENS_PEDIDO (ID_ITEM_PEDIDO, NUM_PEDIDO, ID_PRODUTO, QUANTIDADE) VALUES
    (1, 1001, 101, 3),  -- 3 kg de Arroz
    (2, 1002, 103, 2),  -- 2 unidades de Óleo de Soja
    (3, 1003, 102, 6),  -- 6 unidades de Leite
    (4, 1004, 104, 2),  -- 2 kg de Açúcar
    (5, 1005, 105, 4);  -- 4 unidades de Detergente

select * from itens_pedido;
