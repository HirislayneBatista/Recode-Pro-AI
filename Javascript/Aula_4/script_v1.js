let contatos = [];
let contatoAtual = null;
 
function adicionarContato() {
    const nome = document.getElementById('nome').value;
    const telefone = document.getElementById('telefone').value;
 
 
    if(contatoAtual !== null){
        contatos[contatoAtual] = { nome, telefone };
        contatoAtual = null;
    } else {
        contatos.push({ nome, telefone });
    }
 
    document.getElementById('nome').value = '';
    document.getElementById('telefone').value = '';
 
    listarContatos();
}
 
function listarContatos() {
    const lista = document.getElementById('listaContatos');
    lista.innerHTML = '';
    contatos.forEach((contato, index) => {
        lista.innerHTML += `<li>${contato.nome} - ${contato.telefone}
                            <button onclick="editarContato(${index})">Editar</button>
                            <button onclick="removerContato(${index})">Excluir</button></li>`;
    });
}
 
function removerContato(index) {
    contatos.splice(index, 1);
    listarContatos();
}
 
function editarContato(index){
    document.getElementById('nome').value = contatos[index].nome;
    document.getElementById('telefone').value = contatos[index].telefone;
    contatoAtual = index;
}