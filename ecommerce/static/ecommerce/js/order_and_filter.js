document.getElementById('order-form').addEventListener('submit', function(event) {
    // Evitar que el formulario se envíe inmediatamente
    event.preventDefault();

    const filterForm = document.getElementById('filter-form');
    const checkboxes = filterForm.querySelectorAll('input[type="checkbox"]:checked');
    
    // Para cada checkbox seleccionado, crear un campo oculto
    checkboxes.forEach(function(checkbox) {
        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = checkbox.name; // El nombre del filtro (marca, colores, talles)
        hiddenInput.value = checkbox.value; // El valor del checkbox (ID de la marca, color, talle)

        // Verificar si ya existe un campo oculto con el mismo nombre
        const existingInput = this.querySelector(`input[name="${checkbox.name}"]`);
        if (existingInput) {
            // Si ya existe, añadimos el nuevo valor al valor existente, separados por comas
            existingInput.value += `,${checkbox.value}`;
        } else {
            // Si no existe, añadimos el campo oculto como un nuevo input
            this.appendChild(hiddenInput);
        }
    }, this);

    // Ahora, podemos enviar el formulario
    this.submit();
});

