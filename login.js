const loginForm = document.querySelector('#loginFormulario')
loginForm.addEventListener('submit', (e) =>{
    e.preventDefault()
    const email = document.querySelector('#correo').value
    const password = document.querySelector('#contrasenia').value
    const Users = JSON.parse(localStorage.getItem('users')) || []

    const usuarioRegistrado = Users.find(user => user.correo === email && user.contrasenia === password)

    if(!usuarioRegistrado){
        return alert('Usuario y/o contraseña incorrecta')
    }
    alert(`Bienvenido ${usuarioRegistrado.name}`)
    localStorage.setItem('loguin_success', JSON.stringify(usuarioRegistrado))
    window.location.href = 'upLoad.html'
})

// function login(){
//     var user, password

//     user = document.getElementById("usuario").value;
//     password = document.getElementById("password").value;

//     if(user == "prueba@g" && password == "123"){
//         window.location = "upLoad.html"
//     } else{
//         alert("datos invalidos")
//     }
// }

