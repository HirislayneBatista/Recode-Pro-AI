function adicionar() {
    var meuInput = document.getElementById("meuInput");
    var lista = document.getElementById("lista");
    var texto = meuInput.value;

    if (texto !== "") {
        // Criar o <li> e estilizar com Bootstrap
        var novoItem = document.createElement("li");
        novoItem.className = "list-group-item";

        // Criar o checkbox para concluir
        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.style.marginRight = "10px";
        checkbox.onclick = function() {
            if (checkbox.checked) {
                novoItem.style.textDecoration = "line-through";
                novoItem.style.backgroundColor = "#e6ffe6";
            } else {
                novoItem.style.textDecoration = "none";
                novoItem.style.backgroundColor = "";
            }
        };

        // Criar um <span> para o texto
        var spanTexto = document.createElement("span");
        spanTexto.textContent = texto; // Usando textContent aqui

        // Criar o botão "X" para remover
        var botaoRemover = document.createElement("button");
        botaoRemover.textContent = "X";
        botaoRemover.className = "btn btn-danger btn-xs pull-right";
        botaoRemover.onclick = function() {
            lista.removeChild(novoItem);
        };

        // Adicionar tudo ao <li>
        novoItem.appendChild(checkbox);
        novoItem.appendChild(spanTexto);
        novoItem.appendChild(botaoRemover);

        // Adicionar o <li> à lista
        lista.appendChild(novoItem);

        // Limpar o input
        meuInput.value = "";
    } else {
        alert("Digite algo antes de adicionar!");
    }
}