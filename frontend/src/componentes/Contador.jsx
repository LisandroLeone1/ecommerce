import { useState, useEffect } from "react";
import './Contador.css';

const Contador = () => {
    const [Numero, setNumero] = useState(0);

    const aumentarNumero = () => {
        setNumero(Numero + 1);
    };

    const disminuirNumero = () => {
        if (Numero>1) {
            setNumero(Numero - 1);
        }
    };


return <div className="contador-carrito">
                <div className="contador">
                <button className="boton-contador" onClick={disminuirNumero}>-</button>
                <span className="cantidad">{Numero}</span>
                <button className="boton-contador" onClick={aumentarNumero}>+</button>
            </div>
            <button type="submit" className="boton-carrito">Agregar al carrito</button>

</div>
}

export default Contador;