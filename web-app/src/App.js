import React, {useState, useEffect} from 'react';

import {Cadastro, Login, Submit} from "./components"
import api from './service/api';

function App (){
    const [cadastro, setCadastro] = useState(false);
    const [login, setLogin] = useState(false);
    const [email, setEmail] = useState("");
    const [send, setSend] = useState(false);
    const [reload, setReload] = useState(false);
    const [statusConfirm, setStatusConfirm] = useState("Confirmação pendente");
    const [enviar, setEnviar] = useState(false);
    
    const changeEmail = (email) => {
        setEmail(email);
    }
    useEffect(() => {
        localStorage.setItem("email","");    
    }, []);
    useEffect(() => {
        setLogin(false);
        setCadastro(false);
        if(email!== null && email !==""){
            setSend(true);
            handle_subscribe();
        }
    }, [email]);

    const handle_reload = async () => {
        const {data} = await api.post("/confirm-subscription",{"email":email});
        setStatusConfirm(data.Status);
        if( data.Status=="Confirmed"){
            setReload(false);
            setEnviar(true)
        }
    }

    const handle_subscribe = async () => {
        await api.post("/subscribe",{"email":email});
        setReload(true);
    }

    return (
    <div className="app">
        <h1>Web App</h1>
        <h2>Já efetuou Cadastro?</h2>
        <button className="btn" onClick={function(event){ setCadastro(!cadastro); setLogin(false)}  }>Efetuar Cadastro</button>
        <button className="btn" onClick={function(event){ setLogin(!login); setCadastro(false)}  }>Logar</button><br></br>
        {
            login && (<Login email={changeEmail}></Login>)
        }
        {
            cadastro && (<Cadastro email={changeEmail}></Cadastro>)
        }
        {
            reload &&
            ( 
                <div>
                    <h4>Um e-mail foi enviado para a confirmação do seu e-mail.</h4>
                    <button onClick={() => handle_reload()}>Reload</button>
                    <span>Status: {statusConfirm}</span>
                </div>
            ) 
        }
        {
            enviar && (
                    <Submit></Submit>
            )
        }
        

    </div>)
}

export default App;
