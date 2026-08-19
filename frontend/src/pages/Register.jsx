import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";


function Register() {

    const navigate = useNavigate();

    const [form, setForm] = useState({
        username: "",
        email: "",
        first_name: "",
        last_name: "",
        password: "",
    });

    const [error, setError] = useState("");


    const handleChange = (event) => {

        setForm({
            ...form,
            [event.target.name]: event.target.value,
        });
    };


    const handleSubmit = async (event) => {

        event.preventDefault();

        try {

            await api.post(
                "/auth/register",
                form
            );

            navigate("/login");

        } catch (error) {

            setError(
                error.response?.data?.detail ||
                "Registration failed"
            );
        }
    };


    return (
        <div className="page">
            <div className="card">

                <h1>Create Account</h1>

                {error && (
                    <p className="error">{error}</p>
                )}

                <form onSubmit={handleSubmit}>

                    <input
                        name="username"
                        placeholder="Username"
                        value={form.username}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="email"
                        type="email"
                        placeholder="Email"
                        value={form.email}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="first_name"
                        placeholder="First name"
                        value={form.first_name}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="last_name"
                        placeholder="Last name"
                        value={form.last_name}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="password"
                        type="password"
                        placeholder="Password"
                        value={form.password}
                        onChange={handleChange}
                        required
                    />

                    <button type="submit">
                        Register
                    </button>

                </form>

            </div>
        </div>
    );
}


export default Register;