//Você deverá criar a opção de remover algum item da lista, que será exibida junto à pergunta de “você deseja adicionar uma comida na lista de compras”?
//A partir daí, caso a pessoa escolha essa opção, o programa irá imprimir os elementos presentes na lista atual, e a pessoa deverá escrever qual deles deseja remover.
//Depois disso, o programa irá remover o elemento da lista e imprimir a confirmação de que o item realmente não está mais lá.
//Por fim, ele voltará para o ciclo inicial de perguntas.
//Se, na hora de deletar o item, o mesmo não for encontrado na lista, você deverá exibir uma mensagem avisando isso.
//Por exemplo: “Não foi possível encontrar o item dentro da lista!”
//Lembre-se que a opção de remover um item só deverá estar disponível a partir do momento que existir ao menos um elemento dentro da lista de compras.

//inicio do codigo

let frutas = [];
let laticinios = [];
let doces = [];
let congelados = [];
let comida = "";
let categoria = "";

let adicionarMais = "sim";

while (adicionarMais !== "não") {
    adicionarMais = prompt("Você deseja 'adicionar' uma comida ou 'remover' um item da lista de compras? Responda 'adicionar', 'remover' ou 'não'.");

    while (adicionarMais !== "adicionar" && adicionarMais !== "remover" && adicionarMais !== "não") {
        alert("Operação não reconhecida!");
        adicionarMais = prompt("Você deseja 'adicionar' uma comida ou 'remover' um item da lista de compras? Responda 'adicionar', 'remover' ou 'não'.");
    }

    if (adicionarMais === "não") {
        break;
    }

    if (adicionarMais === "adicionar") {
        comida = prompt("Qual comida você deseja inserir?");
        categoria = prompt("Em qual categoria essa comida se encaixa: 'frutas', 'laticínios', 'doces' ou 'congelados'?");
        
        switch (categoria) {
            case 'frutas':
                frutas.push(comida);
                break;
            case 'laticínios':
                laticinios.push(comida);
                break;
            case 'doces':
                doces.push(comida);
                break;
            case 'congelados':
                congelados.push(comida);
                break;
            default:
                alert("Essa categoria não foi pré-definida.");
        }
    } else if (adicionarMais === "remover") {
        if (frutas.length === 0 && laticinios.length === 0 && doces.length === 0 && congelados.length === 0) {
            alert("A lista de compras está vazia, não há nada para remover.");
        } else {
            let listaAtual = `Lista de compras:\n  Frutas: ${frutas}\n  Laticínios: ${laticinios}\n  Doces: ${doces}\n  Congelados: ${congelados}`;
            alert(listaAtual);
            
            let itemRemover = prompt("Qual item você deseja remover?");
            let itemRemovido = false;

            function removerItem(lista, item) {
                let index = lista.indexOf(item);
                if (index !== -1) {
                    lista.splice(index, 1);
                    return true;
                }
                return false;
            }

            if (removerItem(frutas, itemRemover)) {
                itemRemovido = true;
            } else if (removerItem(laticinios, itemRemover)) {
                itemRemovido = true;
            } else if (removerItem(doces, itemRemover)) {
                itemRemovido = true;
            } else if (removerItem(congelados, itemRemover)) {
                itemRemovido = true;
            }

            // Feedback
            if (itemRemovido) {
                alert(`O item '${itemRemover}' foi removido da lista com sucesso.`);
            } else {
                alert("Não foi possível encontrar o item dentro da lista!");
            }
        }
    }
}

alert(`Lista final de compras:\n  Frutas: ${frutas}\n  Laticínios: ${laticinios}\n  Doces: ${doces}\n  Congelados: ${congelados}`);
