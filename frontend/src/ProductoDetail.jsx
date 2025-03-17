import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import './ProductoDetail.css';
import Contador from './componentes/Contador.jsx';

const ProductDetail = () => {
    const { id } = useParams();
    const [producto, setProducto] = useState(null);
    const [imagenActual, setImagenActual] = useState(null);
    const [VentanaVisible, setVentanaVisible] = useState(false);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/v1/producto/${id}/`)
        .then((response) => {
        if (!response.ok) {
            throw new Error("Error al obtener el producto");
        }
        return response.json();
        })
        .then((data) => {
            setProducto(data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    }, [id]);

    useEffect(() => {
        if (producto) {
            setImagenActual(producto.imagen_principal);
        }
    }, [producto]);

    if (!producto) {
        return <p>Cargando...</p>;
    }

    const talles = [
        ...producto.talles_indumentaria,
        ...producto.talles_calzado,
        ...producto.talles_accesorios
    ];

const PrecioEnCuotas = (precio) => {
    return precio/3
}

const PrecioConDescuento = (precio, descuento) => {
    return precio - (precio * descuento / 100);
};



const abrirVentana = () => {
    setVentanaVisible(!VentanaVisible);
};


return (<div>
            <div className="container__producto">
                <div className="producto__img">
                    <div className="thumbail__container">
                        {producto.imagen_principal && (
                            <img src={ producto.imagen_principal} alt="" className={`thumbail ${producto.imagen_principal === imagenActual ? 'active' : ''}`} onClick={() => setImagenActual(producto.imagen_principal)}></img>
                        )}
                        {producto.imagen_secundaria_1 && (
                            <img src={ producto.imagen_secundaria_1} alt="" className={`thumbail ${producto.imagen_secundaria_1 === imagenActual ? 'active' : ''}`} onClick={() => setImagenActual(producto.imagen_secundaria_1)}></img>
                        )}
                        {producto.imagen_secundaria_2 && (
                        <img src={ producto.imagen_secundaria_2} alt="" className={`thumbail ${producto.imagen_secundaria_2 === imagenActual ? 'active' : ''}`} onClick={() => setImagenActual(producto.imagen_secundaria_2)}></img>
                        )}
                        {producto.imagen_secundaria_3 && (
                        <img src={ producto.imagen_secundaria_3} alt="" className={`thumbail ${producto.imagen_secundaria_3 === imagenActual ? 'active' : ''}`}  onClick={() => setImagenActual(producto.imagen_secundaria_3)}></img>
                            )}
                    </div>
                    <div className="container__main-img">
                        <img src={imagenActual} alt="" className="main__img"></img>
                        <h1>{producto.nombre}</h1>
                        <p>Retiro en Local Junin  - Junin 5643 Horario de atención: Lunes a Viernes de 8.30 a 12.30 y 16.30 a 20.30 hs // Sábados de 9 a 13 y 16:30 A 20:30 hs</p>
                    </div>
                    
                </div>
            <div className="producto__data">
            {producto.estado === "sale" ? (
                <>
                <div className="producto__sale">
                    <h4>{producto.marca.nombre}</h4>
                    <div className="container__sale">
                        <p>{producto.descuento}%</p>
                        <p>OFF</p>
                    </div>
                </div>
                <h3>{producto.nombre}</h3>
                <div className="container__descuento">
                    <h5 className="precio__descuento producto-desc">${producto.precio}</h5>
                    <h5 className="producto-precio">${PrecioConDescuento(producto.precio, producto.descuento)}</h5>
                </div>
                </>
            ) : (
                <>
                <h4>{producto.marca.nombre}</h4>
                <h3>{producto.nombre}</h3>
                <h5 className="producto-precio">${producto.precio}</h5>
                </>
            )}
            
            <div className="container__cuotas">
                <p className="cuotas"><i className="bi bi-cash"></i> 3 cuotas de ${PrecioEnCuotas(producto.precio)}</p>
                <p className="cuotas"><i className="bi bi-credit-card-2-back"></i>10% de descuento <span>pagando con deposito o transferencia</span></p>
            </div>
            <div className="container__options">
                <div className="form-group">
                    <label htmlFor="color">Color</label>
                    <select name="color" id="color"> 
                    {producto.colores.map((color) => (
                        <option key={color.id} value={color.nombre}>
                            {color.nombre}
                        </option>
                    ))}
                    </select>
                </div>
            
                <div className="form-group">
                    <label htmlFor="talle">Talle</label>
                    <select name="talle" id="talle"> 
                    {talles.length > 0 ? (
                        talles.map((talle) => (
                            <option key={talle.id} value={talle.nombre}>
                                {talle.nombre}
                            </option>
                        ))
                    ): (
                        <option disabled>No hay talles disponibles</option>
                    )}

                    </select>
                </div>
            </div>  
            <Contador ></Contador>
            <div className="envios__container">
                <i className="bi bi-house-up"></i>
                <div>
                    <h5>Retiro gratis por nuestro locales</h5>
                    <button className="button-locales" onClick={abrirVentana}><span className="texto-boton">Ver opciones</span> <i className="bi bi-chevron-down"></i></button>
                    <div className={`ventana-locales ${VentanaVisible ? 'visible': ''}`}>
                        <p>Retiro en Local Junin  - Junin 5643 Horario de atención: Lunes a Viernes de 8.30 a 12.30 y 16.30 a 20.30 hs // Sábados de 9 a 13 y 16:30 A 20:30 hs</p>
                        <p>Retiro en Local Avenida General Paz - Avenida General Paz 660 Horario de atención: Lunes a Sábados de 9 a 13 y 16.00 a 20.00hs</p>
                    </div>
                </div>
            </div>
            <div className="envios__container">
                <i className="bi bi-box-seam"></i>
                <div>
                    <h5>Envios Gratis</h5>
                    <p>Las compras superiores a $ 99..999 tienen ENVIO GRATIS. Si no llegas a ese monto para acceder al beneficio, podés agregar otro producto al carrito o retirar por Nuestros Locales</p>
                </div>
            </div>
            <div className="envios__container">
                <i className="bi bi-box-seam"></i>
                <div>
                    <h5>Envios</h5>
                    <p>Envios por Correo Andrean</p>
                </div>
            </div>
            </div>
        </div>
    </div>
    );
};

export default ProductDetail;