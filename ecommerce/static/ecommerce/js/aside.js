button_filters = document.querySelector('#toggle-filters');
close_filters = document.querySelector('#close-filters');
aside = document.querySelector('#aside-filters');
main = document.querySelector('#main');
genero_cont = document.querySelector('#container-genero');
filters_cont = document.querySelector('#container-filters');

button_filters.addEventListener('click', function() { 
    aside.classList.add('show'); // Agrega la clase que muestra el aside
    main.style.display = 'none';
    filters_cont.appendChild(genero_cont); // Añade genero_cont a filters_cont
});

close_filters.addEventListener('click', function() { 
    aside.classList.remove('show'); // Quita la clase para ocultar el aside
    main.style.display = 'block';
    if (genero_cont.parentNode === filters_cont) { // Verifica si genero_cont está en filters_cont
        filters_cont.removeChild(genero_cont); // Quita genero_cont de filters_cont
    }
});
