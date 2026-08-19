import { useEffect, useState } from "react";

import api from "../services/api";


function Products() {

    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);


    useEffect(() => {

        const loadProducts = async () => {

            try {

                const response = await api.get(
                    "/products/"
                );

                setProducts(response.data);

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);
            }
        };


        loadProducts();

    }, []);


    if (loading) {
        return <p>Loading...</p>;
    }


    return (
        <div className="container">

            <h1>Products</h1>

            <div className="products-grid">

                {products.map((product) => (

                    <div
                        className="product-card"
                        key={product.id}
                    >

                        {product.image_url && (
                            <img
                                src={product.image_url}
                                alt={product.name}
                            />
                        )}

                        <h2>{product.name}</h2>

                        <p>
                            {product.description}
                        </p>

                        <strong>
                            ${product.price}
                        </strong>

                        <p>
                            Stock: {product.stock}
                        </p>

                    </div>

                ))}

            </div>

        </div>
    );
}


export default Products;