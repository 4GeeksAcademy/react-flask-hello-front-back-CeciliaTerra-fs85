import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";

export const Profile = () => {
    const {  actions } = useContext(Context);


    useEffect(()=>{
        actions.getProfile()
    },[])

    return (
        <div className="text-center mt-5">
            <h1>Profile</h1>
        </div>
    );
};
