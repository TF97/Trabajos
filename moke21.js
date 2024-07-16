let ataqueJugador
let ataqueEnemigo
let vidasJugador = 3
let vidasEnemigo = 3

function iniciarJuego(){
	let sectionSeleccionarAtaque = document.getElementById('seleccionar-ataque')
	sectionSeleccionarAtaque.style.display = 'none'

	let sectionReiniciar = document.getElementById('reiniciar')
	sectionReiniciar.style.display = 'none'

	let botonMascotaJugador = document.getElementById('boton-mascota')
	botonMascotaJugador.addEventListener('click', seleccionarMascotaJugador)	
	
	let botonFuego = document.getElementById('boton-fuego')
	botonFuego.addEventListener('click', ataqueFuego)
	
	let botonAgua  = document.getElementById('boton-agua')
	botonAgua.addEventListener('click', ataqueAgua)
	
	let botonTierra = document.getElementById('boton-tierra')
	botonTierra.addEventListener('click', ataqueTierra)
	
	let botonReiniciar = document.getElementById('boton-reiniciar')
	botonReiniciar.addEventListener('click', reiniciarJuego)
}

function seleccionarMascotaJugador(){
	let sectionSeleccionarAtaque = document.getElementById('seleccionar-ataque')
	sectionSeleccionarAtaque.style.display = 'flex'
	
	let sectionSeleccionarMascota = document.getElementById('seleccionar-mascota')
	sectionSeleccionarMascota.style.display = 'none'
	
	
	
	
	let inputHipodoge = document.getElementById('hipodoge')
	let inputCapipepo = document.getElementById('capipepo')
	let inputRatigueya = document.getElementById('ratigueya')
	let spanMascotaJugador = document.getElementById('mascota-jugador')
	
	
	if(inputHipodoge.checked){
		spanMascotaJugador.innerHTML = 'Hipodoge'
	}else if (inputCapipepo.checked){
		spanMascotaJugador.innerHTML = 'Capipepo'
	}else if (inputRatigueya.checked){
		spanMascotaJugador.innerHTML = 'Ratigueya'
	}else{
		alert('selecciona una mascota')
	}
	
	seleccionarMascotaEnemigo()
}
function seleccionarMascotaEnemigo(){
	let mascotaAleatoria = aleatorio(1,3)
	let spanMascotaEnemigo = document.getElementById('mascota-enemigo')
	
	if(mascotaAleatoria == 1){
		spanMascotaEnemigo.innerHTML = 'Hipodoge'
	} else if(mascotaAleatoria == 2){
		spanMascotaEnemigo.innerHTML = 'Capipepo'
	} else {
		spanMascotaEnemigo.innerHTML = 'Ratigueya'
	}
	
}
function ataqueFuego(){
	ataqueJugador = 'FUEGO'
	ataqueAleatorioEnemigo()
}
function ataqueAgua(){
	ataqueJugador = 'AGUA'
	ataqueAleatorioEnemigo()
}
function ataqueTierra(){
	ataqueJugador = 'TIERRA'
	ataqueAleatorioEnemigo()
}
function ataqueAleatorioEnemigo(){
	let ataqueAleatorio = aleatorio(1,3)
	
	if(ataqueAleatorio == 1){
		ataqueEnemigo = 'FUEGO'
	} else if(ataqueAleatorio == 2){
		ataqueEnemigo = 'AGUA'
	} else{
		ataqueEnemigo = 'TIERRA' 
	}
	
	combate()
}
function combate(){
let spanVidasJugador = document.getElementById('vidas-jugador')
let spanVidasEnemigo = document.getElementById('vidas-enemigo')

	
	if(ataqueEnemigo == ataqueJugador){
			crearMensaje("Empate")
			} else if(ataqueJugador == 'FUEGO' && ataqueEnemigo == 'TIERRA'){
				crearMensaje("Ganaste")
				vidasEnemigo--
				spanVidasEnemigo.innerHTML = vidasEnemigo
			} else if(ataqueJugador == 'AGUA' && ataqueEnemigo == 'FUEGO'){
				crearMensaje("Ganaste")
				vidasEnemigo--
				spanVidasEnemigo.innerHTML = vidasEnemigo
			} else if(ataqueJugador == 'TIERRA' && ataqueEnemigo == 'AGUA'){
			crearMensaje("Ganaste")
				vidasEnemigo--
				spanVidasEnemigo.innerHTML = vidasEnemigo
			} else{
				crearMensaje("Perdiste")
				vidasJugador--
				spanVidasJugador.innerHTML = vidasJugador
			}
			
			revisarVidas()
}

function revisarVidas(){
	if(vidasEnemigo ==0){
		crearMensajeFinal("FELICITACIONES! ganaste 🎉")
	}else if (vidasJugador == 0){
		crearMensajeFinal('lo siento, perdiste 😭')
	}
}

function crearMensaje(resultado){
	let sectionMensajes = document.getElementById('resultado')
	let notificacion = document.createElement('p')
	let nuevoAtaqueDelJugador = document.createElement('p')
	let nuevoAtaqueDelEnemigo = document.createElement('p')
	
	sectionMensajes.innerHTML = resultado
	
	
	nuevoAtaqueDelJugador.innerHTML = ataqueJugador
	nuevoAtaqueDelEnemigo.innerHTML = ataqueEnemigo
	
	let ataqueDelJugador = document.getElementById('ataque-del-jugador')
	ataqueDelJugador.appendChild(nuevoAtaqueDelJugador)
	
	let ataqueDelEnemigo = document.getElementById('ataque-del-enemigo')
	ataqueDelEnemigo.appendChild(nuevoAtaqueDelEnemigo)
}

function crearMensajeFinal(resultadoFinal){
	let sectionMensajes = document.getElementById('resultado')
	
	sectionMensajes.innerHTML = resultadoFinal
	
	
	
	
	let botonFuego = document.getElementById('boton-fuego')
		botonFuego.disabled = true
		let botonAgua  = document.getElementById('boton-agua')
		botonAgua.disabled = true
		let botonTierra = document.getElementById('boton-tierra')
		botonTierra.disabled = true
		
	let sectionReiniciar = document.getElementById('reiniciar')
	sectionReiniciar.style.display = 'block'
}

function reiniciarJuego(){
	
	location.reload()
}

function aleatorio(min, max){
	return Math.floor(Math.random() * (max - min + 1)+ min)
}


window.addEventListener('load', iniciarJuego)
	
