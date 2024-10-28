button_filters = document.querySelector('#toggle-filters');
close_filters = document.querySelector('#close-filters');
aside = document.querySelector('#aside-filters');
main = document.querySelector('#main')


button_filters.addEventListener('click', function() { 
    aside.classList.add('show'); // Agrega la clase que muestra el aside
    main.style.display = 'None';
});

close_filters.addEventListener('click', function() { 
    aside.classList.remove('show'); // Quita la clase para ocultar el aside
    main.style.display = 'Block';
});
