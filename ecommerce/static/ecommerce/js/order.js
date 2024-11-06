const containerCategoria = document.querySelector('.container__categoria');
const cont1 = document.querySelector('#cont1');
const rutasContainer = document.querySelector('.rutas__container');
const toggleFiltersButton = document.querySelector('#toggle-filters');
const containerFiltro = document.getElementById('container-filtro')

const originalParent = rutasContainer.parentElement;
const originalNextSibling = rutasContainer.nextElementSibling;
    
function moveItems() {
    if (window.innerWidth > 768) {
        toggleFiltersButton.style.display = 'none'; // Cambiado 'None' a 'none'
        toggleFiltersButton.parentElement.insertBefore(rutasContainer, toggleFiltersButton);

    } else {

        toggleFiltersButton.style.display = 'flex'; // Muestra el botón en pantallas más pequeñas
        cont1.insertBefore(rutasContainer, containerCategoria);
    }
}

window.addEventListener('resize', moveItems);
window.addEventListener('load', moveItems);