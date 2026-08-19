import { Link, useNavigate } from "react-router-dom";


function Navbar() {

    const navigate = useNavigate();

    const token = localStorage.getItem(
        "token"
    );


    const logout = () => {

        localStorage.removeItem("token");

        navigate("/login");
    };


    return (
        <nav>

            <Link to="/">
                ShopCart
            </Link>

            <Link to="/products">
                Products
            </Link>

            {token ? (
                <>
                    <Link to="/products/create">
                        Add Product
                    </Link>

                    <button onClick={logout}>
                        Logout
                    </button>
                </>
            ) : (
                <>
                    <Link to="/login">
                        Login
                    </Link>

                    <Link to="/register">
                        Register
                    </Link>
                </>
            )}

        </nav>
    );
}


export default Navbar;