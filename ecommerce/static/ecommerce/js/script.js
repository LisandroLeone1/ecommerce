const boton = document.getElementById('button');
const lista = document.getElementById('lista');

const toggleClase = () => {
    lista.classList.toggle('visible');
};


boton.addEventListener('click', toggleClase);
