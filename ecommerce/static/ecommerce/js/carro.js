/*
document.addEventListener("DOMContentLoaded", function() {
    const botonesAgregar = document.querySelectorAll(".boton-carrito");

    botonesAgregar.forEach(boton => {
        boton.addEventListener("click", function(event) {
            event.preventDefault(); // Evita que se recargue la página

            const productoId = this.dataset.id;

            fetch(`/carro/agregar/${productoId}/`, {
                method: 'POST', // Cambiar a POST
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // Agregar token CSRF
                }
            })
            .then(response => {
                if (response.ok) {
                    return response.json(); // Espera el JSON de respuesta
                }
                throw new Error('Error en la solicitud');
            })
            .then(data => {
                console.log(data); // Puedes actualizar el UI aquí
                alert("Producto agregado al carrito!");
                
                    // Lógica para actualizar el carrito en la UI
                    const carritoGrid = document.querySelector('.carro__grid');
                    carritoGrid.innerHTML = ''; // Limpiar el contenido actual
                
                    // Iterar sobre los productos en el carrito y crear el nuevo HTML
                    Object.entries(data.carro).forEach(([key, item]) => {
                        const itemHTML = `
                            <div class="carro__item">
                                <img src="${item.imagen}" alt="${item.nombre}">
                                <div class="carro__data">
                                    <h3>${item.nombre}</h3>
                                    <p>Cantidad: ${item.cantidad}</p>
                                    <h4>Precio: $${item.precio.toFixed(2)}</h4>
                                    <button class="eliminar" data-id="${key}">Eliminar</button>
                                </div>
                            </div>
                        `;
                        carritoGrid.innerHTML += itemHTML; // Agregar el nuevo item al carrito
                    });
                
                    // Si quieres mostrar el total actualizado, puedes calcularlo aquí y actualizarlo
                    let total = Object.values(data.carro).reduce((acc, item) => acc + parseFloat(item.precio), 0);
                    document.querySelector('.total p:last-child').textContent = `$${total.toFixed(2)}`;
                })
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });


// Función para obtener el token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Comprobar si este es el cookie que buscamos
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
*/

