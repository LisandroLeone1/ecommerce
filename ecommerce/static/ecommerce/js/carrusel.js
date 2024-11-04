const buttonPrev = document.getElementById('button-prev');
const buttonNext = document.getElementById('button-next');
const track = document.getElementById('track');
const slickList = document.getElementById('slick-list');
const slick = document.querySelectorAll('.slick');

const slickWidth = slick[0].offsetWidth; // guardo el ancho del primer elemento del carrusel

buttonPrev.onclick = () => Move(1);
buttonNext.onclick = () => Move(2);

function Move(value) {
    const trackWidth = track.offsetWidth;  // ancho del contenedor que contiene las imagenes
    const listWidth = slickList.offsetWidth;  // ancho del contenedor del carrusel

    track.style.left == "" ? leftPosition = track.style.left = 0 : leftPosition = parseFloat(track.style.left.slice(0, -2) * -1)
    // si la propiedad del track esta vacia, se establece la variable leftPosition con valor left 0 para el track
    // en caso de que no este vacia convierto el valor a numero, le elimino los "px" y se convierte a numero negativo al multiplicarlo por -1

    
    if(leftPosition < (trackWidth - listWidth) && value == 2) {
        track.style.left = `${-1 * (leftPosition + slickWidth)}px`;
    } else if(leftPosition > 0 && value == 1) {
        track.style.left = `${-1 * (leftPosition - slickWidth)}px`;
    }
}