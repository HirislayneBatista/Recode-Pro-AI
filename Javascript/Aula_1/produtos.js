let produtos = []

function adicionarProduto(nome, preco, estoque){
    const id = produtos.length + 1;
    const novoItem = { id, nome, preco, estoque };
    produtos.push(novoItem) 
    console.log("Produto cadastrado:", novoItem);
}

function listarProdutos (array){
    console.log("Lista de produtos: ", produtos);
}

function removerProdutos (id){
    const index = produtos.findIndex(produto => produto.id === id); //  busca o primeiro elemento que atende a condição
    if (index !== -1) {
        const removido = produtos.splice(index, 1); // Adiciona/Remove elementos de acordo com a posição
        console.log("Produto removido:", removido[0]);
    } else {
        console.log("Produto não encontrado.");
    }
}

function alterarProdutos(id, novoNome, novoPreco, novoEstoque){
    const produto = produtos.find(produto => produto.id === id);
    if (produto) {
        produto.nome = novoNome;
        produto.preco = novoPreco;
        produto.estoque = novoEstoque;
        console.log("Produto atualizado:", produto);
    } else {
        console.log("Produto não encontrado.");
    }
}

// Exporta a lista de produtos
// export { produtos };