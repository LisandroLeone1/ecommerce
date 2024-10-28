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
