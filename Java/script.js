let nome = "Hiris";
// nome = 14;
let idade = 23;
let vetor = [1,2,3]
console.log(vetor.length);

if (nome === "hiris" && idade == 23) { // cond1 = tem que ser identico em tipo e valor
    console.log("Tudo certo.")
} else { // estrutura opcional
    console.log("Nada a declarar.");;
}

// alert(nome);

// document.write("Teste");

// console.log("Ola, mundo!");

// console.log(nome);

function saudacao() {
    alert('Olá! Este é um exemplo com Live Server no VS Code.');
}

function frase() {
    document.write("Tu eh feio");
}
// saudacao()

// let i
// let valor = Number(prompt('Digite o valor: ' + i))
// for(let i = 1; i <= 10;i++){
    // document.write(valor + " x ", i , " = " + valor * i + "<br>")
// }


function calcularDesconto(valorProduto) {
    const desconto = 0.09; // Desconto de 9%
    const valorDesconto = valorProduto * desconto;
    const valorFinal = valorProduto - valorDesconto;
    return valorFinal;
}
// const valorOriginal = parseFloat(prompt("Digite o valor do produto:"));
// const valorComDesconto = calcularDesconto(valorOriginal);
// console.log("O valor do produto com desconto é:", valorComDesconto);

function AntecessorValor() {  
    let numero = Number(prompt("Digite o numero:"));
    let antecessor = numero - 1;

    document.write(`O valor de seu antecessor eh ${antecessor}`)
    console.log("sucesso")
}

function Idade() {
    let nome = prompt("Qual o seu nome? ");
    let anoNascimento = Number(prompt("Qual o ano de seu nascimento? "));
    let anoAtual = Number(prompt("Agora informe o ano atual: "));

    document.write(`Olá, ${nome}! Estamos no ano ${anoAtual} e você tem ${anoAtual-anoNascimento} anos de idade.`)
}


// // solicitacao dos dados ao usuario
// let usuario = {
//     email: prompt("Digite seu email:"),
//     senha: prompt("Digite sua senha.")
// }

// // simulação do banco de dados
// let BD = {
//     email: "hiris@gmail.com",
//     senha: "123abcd"
// }

// if (usuario.email === BD.email && usuario.senha === BD.senha) {
//     alert("Acesso permitido");
// } else {
//     alert("Acesso negado");
// }

let aluno = {
    nome: prompt("Informe seu nome:"),
    rg: prompt("Informe seu RG:"),
    nota1: Number(prompt("Informe sua primeira nota:")),
    nota2: Number(prompt("Informe sua segunda nota:")),
    nota3: Number(prompt("Informe sua terceira nota:")),
    // usando function tradicional
    // media: function() {
    //     return ((this.nota1 + this.nota2 + this.nota3) / 3)}
    // usando arrow function
    media: () => {
        return ((aluno.nota1 + aluno.nota2 + aluno.nota3) / 3);
    }
}

let situacao;
media = aluno.media();

if (media > 7){
    situacao = "Aprovado";
} else if (media > 5 && media <= 7) {
    situacao = "Recuperacao";
} else {
    situacao = "Reprovado";
}

alert(`Sua situcacao eh ${situacao}`);
document.write(`Média: ${media.toFixed(2)}<br>Situação: ${situacao}`);


// Conversao para json
// let conversaoJson = JSON.parse(aluno);

// Conversao de json para string
// let conversaoString = JSON.stringify(aluno)