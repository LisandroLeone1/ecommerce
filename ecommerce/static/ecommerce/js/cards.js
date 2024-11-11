
// funcion para cambiar de imagen al pasar el mouse por la img de las cards
(function() {
    const cards = document.querySelectorAll('.card__container');

cards.forEach(card => {
    const img = card.querySelector('.card-img-top');
    img.dataset.original = img.src; 
    const img_secundary = img.dataset.secondary;

    const activarImg = () => {
        if (img_secundary) {
            img.src = img_secundary; 
        }
    };

    const desativarImg = () => {
        img.src = img.dataset.original; 
    };

    img.addEventListener('mouseover', activarImg);
    img.addEventListener('mouseout', desativarImg);
});
})();

// funcion para darle la clase activa a las cards
(function() {

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
})();
