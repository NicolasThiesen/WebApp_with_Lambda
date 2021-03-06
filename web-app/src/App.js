import React, {useState, useEffect} from 'react';

import {Cadastro, Login} from "./components"

function App (){
    const [cadastro, setCadastro] = useState(false);
    const [login, setLogin] = useState(false);
    const [email, setEmail] = useState("");
    const [send, setSend] = useState(false);
    
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
            setSend(true)
        }
    }, [email]);
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
            send && 
            (
                <button>Send Me an E-mail</button>
            )
        }
    </div>)
}

export default App;
