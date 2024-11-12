// funcion para cambiar de imagen haciendo click en ellas
(function() {
    const main_img = document.querySelector('.main__img');
const thumbails = document.querySelectorAll('.thumbail');

thumbails.forEach(thumb => {
    thumb.addEventListener('click', function(){
        const active = document.querySelector('.active')
        active.classList.remove('active')
        this.classList.add('active')
        main_img.src = this.src
    })
})
})();

const botonLocales = document.querySelector('.button-locales');
const ventana = document.getElementById('ventana-locales');
const icono = botonLocales.querySelector('i'); // Obtener el icono
const textoBoton = botonLocales.querySelector('.texto-boton'); // Obtener el texto del botón

const VerFiltros = () => {
    if (ventana.style.display === 'none' || ventana.style.display === '') {
        ventana.style.display = 'block';
        textoBoton.textContent = 'Ocultar opciones'; // Cambiar solo el texto
        icono.classList.remove('bi-chevron-down');  // Eliminar el icono de flecha hacia abajo
        icono.classList.add('bi-chevron-up');  // Agregar el icono de flecha hacia arriba
    } else {
        ventana.style.display = 'none';
        textoBoton.textContent = 'Ver opciones'; // Cambiar solo el texto
        icono.classList.remove('bi-chevron-up');  // Eliminar el icono de flecha hacia arriba
        icono.classList.add('bi-chevron-down');  // Agregar el icono de flecha hacia abajo
    }
};

botonLocales.addEventListener('click', VerFiltros);
