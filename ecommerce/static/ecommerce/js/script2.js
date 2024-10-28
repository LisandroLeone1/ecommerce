// Selecciona todas las tarjetas y botones
const tarjetas = document.querySelectorAll('.card__container');

tarjetas.forEach(tarjeta => {
    const boton = tarjeta.querySelector('.boton-compra');

    const activarClase = () => {
        tarjeta.classList.add('activa');
        boton.classList.add('activo');
    };

    const desactivarClase = () => {
        tarjeta.classList.remove('activa');
        boton.classList.remove('activo');
    };

    tarjeta.addEventListener('mouseover', activarClase);
    tarjeta.addEventListener('mouseout', desactivarClase);
});
