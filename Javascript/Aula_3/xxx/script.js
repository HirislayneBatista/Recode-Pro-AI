// function adicionar() {
//     let lista = document.getElementById("lista");
//     let novoItem = document.createElement("li");
 
//     novoItem.textContent = "Novo item da lista";
//     lista.appendChild(novoItem);
// }

function adicionar() {
    // Recupera elemento lista, o campo de entrada e o campo de item da lista
    let lista = document.getElementById("lista"); 
    let itemInput = document.getElementById("input");
    let novoItem = document.createElement("li");
    
    novoItem.textContent = itemInput.value;
    lista.appendChild(novoItem); // O item <li> é adicionado dentro da lista <ul>
}

function remover() {
    let lista = document.getElementById("lista");
    lista.removeChild(lista.lastChild);
}