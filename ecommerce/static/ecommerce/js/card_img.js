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

