const nome = prompt('\nQual seu nome? ');
const idade = prompt('\nQuantos anos você tem? ');
const linguagem = prompt('\nQual linguagem de programação você está estudando? ');

console.log(`\nOlá ${nome}, você tem ${idade} anos e já está aprendendo ${linguagem}!`);

const gosto_linguagem = parseInt(prompt(`\nVocê gosta da linguagem ${linguagem}? 1 para SIM // 2 para NÃO `));

if (gosto_linguagem === 1) {
    console.log(`\nMuito bom ${nome}! Continue estudando e você terá muito sucesso`);
} else {
    console.log(`\nAhh que pena ${nome}... Já tentou aprender outras linguagens?`);
}
