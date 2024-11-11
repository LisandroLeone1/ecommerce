
// funcion para mover el los elementos del intro-container
(function() {
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
})();



// funcion para mostrar todos los filtros disponibles haciendo click en el boton
(function() {
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
                element2.textContent = 'Ver menos';  
            } else {
                element.classList.add(className);
                element2.textContent = 'Ver todos';  
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
})();


// funcion para mostrar el aside en pantallas pequeñas
(function() {
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
        if (window.innerWidth > 768) { 
            hideAside();
        }
    });
    
})();


// funcion para que el forumulario de ordenar productos tambien tome los valores del formulario de filtros
(function() {
    document.getElementById('order-form').addEventListener('submit', function(event) {
        // Evitar que el formulario se envíe inmediatamente
        event.preventDefault();
    
        const filterForm = document.getElementById('filter-form');
        const checkboxes = filterForm.querySelectorAll('input[type="checkbox"]:checked');
        
        // para cada checkbox seleccionado, crear un campo oculto
        checkboxes.forEach(function(checkbox) {
            const hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            hiddenInput.name = checkbox.name; // el nombre del filtro (marca, colores, talles)
            hiddenInput.value = checkbox.value; // el valor del checkbox (ID de la marca, color, talle)
            
            // Añadir el campo oculto al formulario de ordenación
            this.appendChild(hiddenInput);
        }, this);
    
        // Finalmente, enviar el formulario de ordenación con los filtros aplicados
        this.submit();
    });
})();





