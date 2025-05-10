// Eventos e Manipulação do DOM

function calcularSalario() {
    // Busca dos valores dos elementos no HTML pelo id
    let nome = document.getElementById("nome").value;
    let salarioBase = parseFloat(document.getElementById("salarioBase").value);
    let inss = parseFloat(document.getElementById("inss").value);
    let ir = parseFloat(document.getElementById("ir").value);
    let outros = parseFloat(document.getElementById("outros").value);

    // Validacao dos campos
    if (isNaN(salarioBase) || isNaN(inss) || isNaN(ir) || isNaN(outros)) {
        alert("Preencha tod xos os campos corretamente!");
        return;
    }

    // Cálculo do salario 
    let salarioLiquido = salarioBase - (inss + ir + outros);

    // Atualização dos campos
    document.getElementById("resNome").textContent = nome;
    document.getElementById("salarioLiquido").textContent = salarioLiquido.toFixed(2);
    
    // Alterar o estilo do elemento - se display: none - faz aparecer depois do cálculo
    // document.querySelector(".resultado").style.display = "block";
    
}

// Adiciona um evento diretamento ao botao - não será necessario o onclick = "calcularSalario()" no HTML 
document.querySelector("button").addEventListener("click", calcularSalario);