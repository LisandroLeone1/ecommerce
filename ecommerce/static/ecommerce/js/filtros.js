document.addEventListener("DOMContentLoaded", function () {
    // Obtenemos los elementos del DOM
    const boton_colores = document.getElementById('button-filtro');
    const filtro_colores = document.getElementById('more-filters');
    
    const boton_talles = document.getElementById('button-filtro-talles');
    const filtro_talles = document.getElementById('more-filters-talles');
    
    const boton_marcas = document.getElementById('button-filtro-marca');
    const filtro_marcas = document.getElementById('filters-marca');


    // Función para mostrar/ocultar los filtros
    const VerFiltros = (element, element2, className) => {
        if (element.classList.contains(className)) {
            element.classList.remove(className);
            element2.textContent = 'Ver menos';  // Cambiar el texto a "Ver todos"
        } else {
            element.classList.add(className);
            element2.textContent = 'Ver todos';  // Cambiar el texto a "Ver menos"
        }
    };

    // Agregar el evento al botón de colores
    if (boton_colores && filtro_colores) {
        boton_colores.addEventListener('click', function() {
            VerFiltros(filtro_colores, boton_colores, 'more-filters');
        });
    }

    // Agregar el evento al botón de talles
    if (boton_talles && filtro_talles) {
        boton_talles.addEventListener('click', function() {
            VerFiltros(filtro_talles, boton_talles, 'more-filters-talles');
        });
    }

    // Agregar el evento al botón de marcas
    if (boton_marcas && filtro_marcas) {
        boton_marcas.addEventListener('click', function() {
            VerFiltros(filtro_marcas, boton_marcas, 'more-filters-marca');
        });
    }
});



