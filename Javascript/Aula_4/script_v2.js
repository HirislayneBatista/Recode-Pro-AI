
// function atualizarContato(index){
//     novoNome = document.getElementById("nome").value;
//     novoTelefone = document.getElementById("telefone").value;
    
//     contatos[index].p_nome = novoNome;
//     contatos[index].p_telefone = novoTelefone;

//     listarContatos();
// }

// function editarContato(index) {
//     let nomeSpan = document.getElementById(`nome-${index}`);
//     let telefoneSpan = document.getElementById(`telefone-${index}`);
//     let listItem = document.getElementById(`contato-${index}`);

//     // Verifica se já está editando para evitar múltiplos botões "Salvar"
//     if (document.getElementById(`novoNome-${index}`)) {
//         return;
//     }

//     // Transformar os spans em inputs para edição
//     nomeSpan.innerHTML = `<input type="text" id="novoNome-${index}" value="${contatos[index].p_nome}">`;
//     telefoneSpan.innerHTML = `<input type="text" id="novoTelefone-${index}" value="${contatos[index].p_telefone}">`;

//     // Adicionar botão para "Salvar"
//     listItem.innerHTML += `<button onclick="salvarContato(${index})">Salvar</button>`;

// }

let contatos = [];

function adicionarContato() {
    let nome = document.getElementById("nome").value;
    let telefone = document.getElementById("telefone").value;

    // Validação
    if (nome.trim() === "" || telefone.trim() === "") {
        alert("Por favor, preencha os campos!");
        return;
    }

    const contato = {
        p_nome: nome,
        p_telefone: telefone,
    };

    contatos.push(contato);
    listarContatos();
}

function listarContatos() {
    const lista = document.getElementById("listaContatos");
    lista.innerHTML = '';  // Sempre limpar a lista antes de atualizar para evitar duplicação

    contatos.forEach((contato, index) => {
        lista.innerHTML += `
            <li id="contato-${index}">
                <span id="nome-${index}">${contato.p_nome}</span>  
                <span id="telefone-${index}">${contato.p_telefone}</span>
                <button id="editar-${index}" class="editar" onclick="editarContato(${index})">Editar</button>
                <button class="excluir" onclick="removerContato(${index})">Excluir</button>
            </li>`;
    });

    // Limpar campos de entrada
    document.getElementById('nome').value = '';
    document.getElementById('telefone').value = '';
}

function removerContato(index) {
    contatos.splice(index, 1);
    listarContatos();
}

function editarContato(index) {
    let nomeSpan = document.getElementById(`nome-${index}`);
    let telefoneSpan = document.getElementById(`telefone-${index}`);
    let listItem = document.getElementById(`contato-${index}`);

    // Verifica se já está editando
    if (document.getElementById(`novoNome-${index}`)) {
        return;
    }

    // Transformar os spans em inputs para edição
    nomeSpan.innerHTML = `<input type="text" id="novoNome-${index}" class="editando" value="${contatos[index].p_nome}">`;
    telefoneSpan.innerHTML = `<input type="text" id="novoTelefone-${index}" class="editando" value="${contatos[index].p_telefone}">`;

    // Esconder botão de editar
    document.getElementById(`editar-${index}`).style.display = "none";

    // Criar botão de salvar
    let salvarBtn = document.createElement("button");
    salvarBtn.innerText = "Salvar";
    salvarBtn.classList.add("salvar");
    salvarBtn.onclick = function() { salvarContato(index); };
    salvarBtn.id = `salvar-${index}`;

    listItem.appendChild(salvarBtn);
}

function salvarContato(index) {
    let novoNome = document.getElementById(`novoNome-${index}`).value;
    let novoTelefone = document.getElementById(`novoTelefone-${index}`).value;

    if (novoNome.trim() === "" || novoTelefone.trim() === "") {
        alert("Os campos não podem estar vazios!");
        return;
    }

    contatos[index].p_nome = novoNome;
    contatos[index].p_telefone = novoTelefone;

    listarContatos();
}
