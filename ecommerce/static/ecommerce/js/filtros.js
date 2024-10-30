const boton_colores = document.getElementById('button-filtro')
const filtro_colores = document.getElementById('more-filters')
const boton_talles = document.getElementById('button-filtro-talles')
const filtro_talles = document.getElementById('more-filters-talles')
const boton_marcas = document.getElementById('button-filtro-marca')
const filtro_marcas = document.getElementById('filters-marca')


const VerFiltros = (element, element2, className) => {
    if (element.classList.contains(className)) {
        element.classList.remove(className);
        element2.textContent = 'Ver menos';
    } else {
        element.classList.add(className);
        element2.textContent = 'Ver todos';
    }
};

const AgregarEvento = (element, element2, className) => {
    element2.addEventListener('click', () => VerFiltros(element, element2, className))
}

AgregarEvento(filtro_colores, boton_colores, 'more-filters');
AgregarEvento(filtro_talles, boton_talles, 'more-filters-talles');
AgregarEvento(filtro_marcas, boton_marcas, 'more-filters-marca');


