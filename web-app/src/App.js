import React, {useState, useEffect} from 'react';

import {Cadastro, Login} from "./components"

function App (){
    const [cadastro, setCadastro] = useState(false);
    const [login, setLogin] = useState(false);
    const [errorLogin, setErrorLogin] = useState(false);
    useEffect(() => {
        localStorage.setItem("email","");    
    })
    return (
    <div className="app">
        <h1>Web App</h1>
        <h2>Já efetuou Cadastro?</h2>
        <button className="btn" onClick={function(event){ setCadastro(!cadastro); setLogin(false)}  }>Efetuar Cadastro</button>
        <button className="btn" onClick={function(event){ setLogin(!login); setCadastro(false)}  }>Logar</button>
        {
            login && (<Login></Login>)
        }
        {
            cadastro && (<Cadastro></Cadastro>)
        }
        {errorLogin && (
            <div className="box-error">
              <span className="error-msg">Login ou senha incorreto</span>
            </div>
        )}
        {
              localStorage.getItem("email") !== null && localStorage.getItem === "" ? setCadastro(false) : ""  
        }
        {
              localStorage.getItem("email") !== null && localStorage.getItem === "" ? setLogin(false) : ""  
        }
          
    </div>)
}

export default App;
