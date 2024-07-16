const registroForm = document.querySelector('#registroForm')
registroForm.addEventListener('submit', (e)=>{
    e.preventDefault()
    const nombre1 = document.querySelector('#name').value
    const apellido = document.querySelector('#lastName').value
    const email = document.querySelector('#email').value
    const contraseña = document.querySelector('#password1').value
    const repetircontraseña = document.querySelector('#password2').value

    const Users = JSON.parse(localStorage.getItem('users')) || []
    const usuarioRegistrado = Users.find(user => user.email === email)
    if ( usuarioRegistrado){
        return alert('El usuario ya esta registrado')
    }

    Users.push({name: nombre1, lastName: apellido, email: email, passwordL: contraseña, passwordL1: repetircontraseña})
    localStorage.setItem('users', JSON.stringify(Users))
    alert("Registro Existoso")
    window.location.href = "login.html"
})