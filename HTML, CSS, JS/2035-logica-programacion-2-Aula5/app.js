let numeroSecreto = 0;
let intentos = 0;
let listaNumerosSorteados = [];
let numeroMaximo = 20;
let maxIntentos = 3; // Límite de intentos

function asignarTextoElemento(elemento, texto) {
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
}

function verificarIntento() {
    let numeroDeUsuario = parseInt(document.getElementById('valorUsuario').value);
    
    if (numeroDeUsuario === numeroSecreto) {
        asignarTextoElemento('p', `🎉 ¡Acertaste el número en ${intentos} ${(intentos === 1) ? 'vez' : 'veces'}!`);
        document.getElementById('reiniciar').removeAttribute('disabled');
    } else {
        if (numeroDeUsuario > numeroSecreto) {
            asignarTextoElemento('p', '❌ El número secreto es menor');
        } else {
            asignarTextoElemento('p', '❌ El número secreto es mayor');
        }

        intentos++;

        if (intentos > maxIntentos) {
            asignarTextoElemento('p', `😢 Has superado el número de intentos. El número era ${numeroSecreto}`);
            document.getElementById('reiniciar').removeAttribute('disabled');
        }
        
        limpiarCaja();
    }
}

function limpiarCaja() {
    document.getElementById('valorUsuario').value = '';
}

function generarNumeroSecreto() {
    let numeroGenerado = Math.floor(Math.random() * numeroMaximo) + 1;

    if (listaNumerosSorteados.length === numeroMaximo) {
        asignarTextoElemento('p', '⚠️ Ya se sortearon todos los números posibles');
        return -1;
    } else {
        if (listaNumerosSorteados.includes(numeroGenerado)) {
            return generarNumeroSecreto();
        } else {
            listaNumerosSorteados.push(numeroGenerado);
            return numeroGenerado;
        }
    }
}

function condicionesIniciales() {
    asignarTextoElemento('h1', '🎯 Juego del número secreto');
    asignarTextoElemento('p', `Adivina un número entre 1 y ${numeroMaximo}. Tienes ${maxIntentos} intentos.`);
    numeroSecreto = generarNumeroSecreto();
    intentos = 1;
}

function reiniciarJuego() {
    limpiarCaja();
    listaNumerosSorteados = [];
    condicionesIniciales();
    document.getElementById('reiniciar').setAttribute('disabled', 'true');
}

condicionesIniciales();
