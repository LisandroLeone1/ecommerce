const button_filters = document.querySelector('#toggle-filters');
const close_filters = document.querySelector('#close-filters');
const aside = document.querySelector('#aside-filters');
const main = document.querySelector('#main');
const containerGenero = document.getElementById('container-genero');
const form = document.getElementById('filter-form');
const title = document.querySelector('.container__filtros-tittle');

button_filters.addEventListener('click', function() { 
    aside.classList.add('show'); // Agrega la clase que muestra el aside
    main.style.display = 'none';
    if (!form.contains(containerGenero)) {
        form.insertBefore(containerGenero, title.nextSibling); // muevo el contenedor dentro del form justo debajo de container tittle
    }
});

function hideAside() {
    aside.classList.remove('show'); 
    main.style.display = 'block';
    if (containerGenero.parentNode === form) {
        form.parentNode.insertBefore(containerGenero, form); // Mueve el contenedor fuera del formulario
    }
}

close_filters.addEventListener('click', function() { 
    hideAside();
});

window.addEventListener('resize', function() {
    if (window.innerWidth > 768) { // Cambia 768 por el ancho deseado
        hideAside();
    }
});
