// Pegando os elementos do DOM
const containerCards = document.getElementById("containerCards");
 
// Função para adicionar um novo card
function adicionarCard() {
  let titulo = document.getElementById("tituloCard").value;
  let descricao = document.getElementById("descricaoCard").value;
 
  if (titulo.trim() === "" || descricao.trim() === "") { // trim remove espaços em branco no inicio e fim da string
    alert("Por favor, preencha todos os campos.");
    return;
  }
 
  // Criando o card dinamicamente
  let card = document.createElement("div"); // cria um novo elemento HTML do tipo div (card)
  // Adicionando classes de Bootstrap ao card para estilização
  card.classList.add("col-md-4", "mb-3");   // classList manipula as classes CSS de um elemento HTML
 
  card.innerHTML = `
        <div class="card shadow p-3">
            <h5 class="card-title">${titulo}</h5>
            <p class="card-text">${descricao}</p>
            <button class="btn btn-remove" onclick="removerCard(this)">Remover</button>
        </div>
    `;

  // Adicionando animação de entrada
  card.style.animation = "fadeIn 0.3s ease-in-out";
 
  // Adicionando o card ao container
  containerCards.appendChild(card); // appendChild() adiciona um elemento filho dentro de um elemento pai.
 
  // Limpando os campos de input
  document.getElementById("tituloCard").value = "";
  document.getElementById("descricaoCard").value = "";
}
 
// Função para remover um card
function removerCard(botao) {
  let card = botao.parentElement.parentElement;
  card.remove();
  // Adicionando animação de saída
  card.classList.add("fadeOut");
}

// Testes
// let novoParagrafo = document.createElement("h1");
// novoParagrafo.textContent = "Teste: Isso texto foi criado dinamicamente!";
// document.body.appendChild(novoParagrafo);

// let lista = document.getElementById("minhaLista");
// let item = document.createElement("li");
// item.textContent = "Novo item";
// lista.appendChild(item); // O item <li> é adicionado dentro da lista <ul> ou <ol>

 