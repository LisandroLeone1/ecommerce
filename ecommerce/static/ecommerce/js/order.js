boton_filtro = document.getElementById('toggle-filters'); 
container_filtro = document.getElementById('container-filtro');

function moveItems() {
    if (window.innerWidth > 768) {
        boton_filtro.style.display = 'none'; // Cambiado 'None' a 'none'
        container_filtro.style.justifyContent = 'flex-end'; // Cambiado a camelCase
    } else {
        boton_filtro.style.display = 'flex'; // Muestra el botón en pantallas más pequeñas
        container_filtro.style.justifyContent = 'flex-start'; // Ajuste opcional para pantallas más pequeñas
    }
}


console.log('hola')
window.addEventListener('resize', moveItems);
window.addEventListener('load', moveItems);