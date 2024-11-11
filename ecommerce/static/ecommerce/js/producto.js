// funcion para cambiar de imagen haciendo click en ellas
(function() {
    const main_img = document.querySelector('.main__img');
const thumbails = document.querySelectorAll('.thumbail');

thumbails.forEach(thumb => {
    thumb.addEventListener('click', function(){
        const active = document.querySelector('.active')
        active.classList.remove('active')
        this.classList.add('active')
        main_img.src = this.src
    })
})
})();

