// Selecciona todas las tarjetas
const tarjetas = document.querySelectorAll('.card__container');

tarjetas.forEach(tarjeta => {
    const boton = tarjeta.querySelector('.boton-compra');

    const activarClase = () => {
        tarjeta.classList.add('card-activa'); // Aplica la clase común
        boton.classList.add('activo');
    };

    const desactivarClase = () => {
        tarjeta.classList.remove('card-activa'); // Elimina la clase común
        boton.classList.remove('activo');
    };

    tarjeta.addEventListener('mouseover', activarClase);
    tarjeta.addEventListener('mouseout', desactivarClase);
});

