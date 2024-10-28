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
