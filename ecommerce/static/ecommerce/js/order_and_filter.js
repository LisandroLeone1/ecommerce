document.getElementById('order-form').addEventListener('submit', function(event) {
    const filterForm = document.getElementById('filter-form');
    const checkboxes = filterForm.querySelectorAll('input[type="checkbox"]:checked');

    checkboxes.forEach(function(checkbox) {
        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = checkbox.name; // Copia el nombre del checkbox
        hiddenInput.value = checkbox.value; // Copia el valor del checkbox
        this.appendChild(hiddenInput);
    }, this);
});
