
(function() {
    const extraItems = document.querySelector('.header__extra');
const navList = document.querySelector('.header__nav');
const container = document.querySelector('.header__container');

function moveExtraItems() {
    if (window.innerWidth < 768) {
        navList.appendChild(extraItems);
    } else {
        container.appendChild(extraItems);
    }
}

window.addEventListener('resize', moveExtraItems);
window.addEventListener('load', moveExtraItems);
})();



// funcion para hacer visible el navbar en pantallas pequeñas
(function() {
    const boton = document.getElementById('button');
const lista = document.getElementById('lista');

const toggleClase = () => {
    lista.classList.toggle('visible');
};


boton.addEventListener('click', toggleClase);

})();



// funcion para hacer visibles las ventanas de ayuda e iniciar sesion
(function() {
const icon = document.getElementById('account');
const ventana = document.getElementById('ventana');
const ventana_help = document.getElementById('ventana-help');
const icon_help = document.getElementById('help');

const activarClase = (element, clase) => {
    element.classList.add(clase);
};

const desactivarClase = (element, clase) => {
    element.classList.remove(clase);
};

const agregarListeners = (trigger, target, clase) => {
    trigger.addEventListener('mouseover', () => activarClase(target, clase));
    trigger.addEventListener('mouseout', () => {
        if (!target.matches(':hover')) { // si el target no esta en modo hover se desactiva la clase
            desactivarClase(target, clase);
        }
    });
    target.addEventListener('mouseover', () => activarClase(target, clase));
    target.addEventListener('mouseout', () => {
        if (!trigger.matches(':hover')) {
            desactivarClase(target, clase);
        }
    });
};

agregarListeners(icon, ventana, 'activa');
agregarListeners(icon_help, ventana_help, 'activa');
})();


