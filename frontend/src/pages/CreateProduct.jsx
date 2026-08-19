import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";


function CreateProduct() {

    const navigate = useNavigate();

    const [form, setForm] = useState({
        name: "",
        description: "",
        price: "",
        stock: "",
        image_url: "",
    });

    const [error, setError] = useState("");


    const handleChange = (event) => {

        setForm({
            ...form,
            [event.target.name]:
                event.target.value,
        });
    };


    const handleSubmit = async (event) => {

        event.preventDefault();

        try {

            await api.post(
                "/products/",
                {
                    ...form,
                    price: Number(form.price),
                    stock: Number(form.stock),
                }
            );

            navigate("/products");

        } catch (error) {

            setError(
                error.response?.data?.detail ||
                "Unable to create product"
            );
        }
    };


    return (
        <div className="page">

            <div className="card">

                <h1>Create Product</h1>

                {error && (
                    <p className="error">{error}</p>
                )}

                <form onSubmit={handleSubmit}>

                    <input
                        name="name"
                        placeholder="Product name"
                        value={form.name}
                        onChange={handleChange}
                        required
                    />

                    <textarea
                        name="description"
                        placeholder="Description"
                        value={form.description}
                        onChange={handleChange}
                    />

                    <input
                        name="price"
                        type="number"
                        step="0.01"
                        placeholder="Price"
                        value={form.price}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="stock"
                        type="number"
                        placeholder="Stock"
                        value={form.stock}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="image_url"
                        placeholder="Image URL"
                        value={form.image_url}
                        onChange={handleChange}
                    />

                    <button type="submit">
                        Create Product
                    </button>

                </form>

            </div>

        </div>
    );
}


export default CreateProduct;