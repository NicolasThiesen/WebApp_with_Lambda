import React, {useState} from 'react'
import { Formik, Form, Field } from 'formik'

const Login = () => {
    const handleSubmit = async values => {
        const { data } = await api.post('/login', values);
        localStorage.setItem('email', data["email"]);
      }
    return (
        <Formik initialValues={{ email: '', password: '' }} onSubmit={handleSubmit}>
            <Form>
                <label htmlFor="email">Email</label>
                <Field name="email" type="text" required autoFocus></Field>
                <label htmlFor="password">Senha</label>
                <Field name="password" type="password" required></Field>
                <button type="submit">Logar</button>
            </Form>
        </Formik>
    )
}
export default Login;