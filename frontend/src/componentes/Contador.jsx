import { useState } from "react";
import "./Contador.css";

const Contador = ({ productoId }) => {
    const [Numero, setNumero] = useState(1);  // Empieza en 1, no en 0

    const aumentarNumero = () => setNumero(Numero + 1);
    const disminuirNumero = () => {
        if (Numero > 1) setNumero(Numero - 1);
    };

    const getCSRFToken = () => {
        const csrfCookie = document.cookie.split("; ").find(row => row.startsWith("csrftoken="));
        return csrfCookie ? csrfCookie.split("=")[1] : "";
    };

    const agregarAlCarrito = async () => {
        const response = await fetch("http://127.0.0.1:8000/carro/agregar/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(),  // Necesario si usas Django con CSRF
            },
            body: JSON.stringify({ producto_id: productoId, cantidad: Numero }),
            credentials: "include",
        });

        const data = await response.json();
        alert(data.mensaje);
    };

    return (
        <div className="contador-carrito">
            <div className="contador">
                <button className="boton-contador" onClick={disminuirNumero}>-</button>
                <span className="cantidad">{Numero}</span>
                <button className="boton-contador" onClick={aumentarNumero}>+</button>
            </div>
            <button type="button" className="boton-carrito" onClick={agregarAlCarrito}>
                Agregar al carrito
            </button>
        </div>
    );
};

export default Contador;
