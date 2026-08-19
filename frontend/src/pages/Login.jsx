import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";


function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");


    const handleSubmit = async (event) => {

        event.preventDefault();

        try {

            const formData = new URLSearchParams();

            formData.append(
                "username",
                username
            );

            formData.append(
                "password",
                password
            );


            const response = await api.post(
                "/auth/token",
                formData,
                {
                    headers: {
                        "Content-Type":
                            "application/x-www-form-urlencoded",
                    },
                }
            );


            localStorage.setItem(
                "token",
                response.data.access_token
            );


            navigate("/products");

        } catch (error) {

            setError(
                error.response?.data?.detail ||
                "Invalid username or password"
            );
        }
    };


    return (
        <div className="page">
            <div className="card">

                <h1>Login</h1>

                {error && (
                    <p className="error">{error}</p>
                )}

                <form onSubmit={handleSubmit}>

                    <input
                        placeholder="Username"
                        value={username}
                        onChange={(e) =>
                            setUsername(e.target.value)
                        }
                        required
                    />

                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                        required
                    />

                    <button type="submit">
                        Login
                    </button>

                </form>

            </div>
        </div>
    );
}


export default Login;