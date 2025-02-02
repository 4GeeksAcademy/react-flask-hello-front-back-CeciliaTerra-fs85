import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { Link, useNavigate } from "react-router-dom";

export const LoginForm = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const { store, actions } = useContext(Context)
    let navigate = useNavigate();

    async function handleSubmit(e) {
        e.preventDefault()
        let logged = await actions.login(email, password); //con el await espera a que se carguen los datos que le mando de paramentros, sin esto no funciona     
        if (logged == true) {
            navigate("/profile")
        }
        else{
            alert("Correo o contraseña erroneo")
        }

    }

    return (
        <form onSubmit={handleSubmit} className="mx-auto w-50">
            <div className="mb-3">
                <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" onChange={(e) => setEmail(e.target.value)} value={email} />
                <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div className="mb-3">
                <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                <input type="password" className="form-control" id="exampleInputPassword1" onChange={(e) => setPassword(e.target.value)} value={password} />
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
        </form>
    );
};