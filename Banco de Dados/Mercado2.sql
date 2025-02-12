create database mercado2;
use mercado2;
 
create table cliente(
	id_cli int,
    nome_cli varchar(50) not null,
    endereco_cli varchar(100) not null,
    cidade_cli varchar(50) not null,
    cep_cli varchar(20) not null,
    uf_cli char(2) not null,
    primary key(id_cli)
);
 
CREATE TABLE VENDEDOR(
	ID_VENDEDOR INT,
	NOME_VEND VARCHAR(40),
	SALARIO_VEND FLOAT,
	COMISSAO FLOAT,
	PRIMARY KEY (ID_VENDEDOR)
);
CREATE TABLE PRODUTO(	
    ID_PRODUTO INT,
	UNIDADE CHAR(2),
	DESCRICAO VARCHAR(20),
	VAL_UNIT FLOAT,
	PRIMARY KEY(ID_PRODUTO)
);
 
CREATE TABLE PEDIDO (
	NUM_PEDIDO INT,
	ID_CLI INT,
	ID_VENDEDOR INT,
	PRAZO_ENTREGA DATE,
	PRIMARY KEY (NUM_PEDIDO),
	FOREIGN KEY (ID_CLI) REFERENCES CLIENTE (ID_CLI),
	FOREIGN KEY (ID_VENDEDOR) REFERENCES VENDEDOR(ID_VENDEDOR)
);
 
 
CREATE TABLE ITENS_PEDIDO
(
	ID_ITEM_PEDIDO INT,
	NUM_PEDIDO INT,
	ID_PRODUTO INT,
	QUANTIDADE INT,
	PRIMARY KEY(ID_ITEM_PEDIDO),
	FOREIGN KEY(NUM_PEDIDO) REFERENCES PEDIDO(NUM_PEDIDO),
	FOREIGN KEY(ID_PRODUTO) REFERENCES PRODUTO(ID_PRODUTO)
);