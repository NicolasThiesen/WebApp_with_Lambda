import React from 'react';
import { Formik, Form, Field } from 'formik';

import api from "../../service/api"

const Cadastro = () => {
    const handleSubmit = async values => {
      const { data } = await api.post('/create-user', values);
      localStorage.setItem('email', data["email"]);

    }
    return (
        <>
          <h3>Efetuar Cadastro</h3>
          <Formik initialValues={{ username: '', password: '', email: ""}} onSubmit={handleSubmit}>
            <Form>
              <label htmlFor="username">Login</label>
              <Field name="username" type="text" required autoFocus></Field> <br></br>
              <label htmlFor="email">Email</label>
              <Field name="email" type="email" required></Field><br></br>
              <label htmlFor="password">Senha</label>
              <Field name="password" type="password" required></Field><br></br>
              <button type="submit">Logar</button>
            </Form>
          </Formik>
        </>
    )
}

export default Cadastro;