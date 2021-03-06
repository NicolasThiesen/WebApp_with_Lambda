import React from 'react'
import { Formik, Form, Field } from 'formik'
import api from "../../service/api"

const Login = ({email}) => {
    const handleSubmit = async values => {
        const { data } = await api.post('/login', values);
        localStorage.setItem('email', data["email"]);
        email(data["email"]);
      }
    return (
        <>
            <h3> Login</h3>
            <Formik initialValues={{ email: '', password: '' }} onSubmit={handleSubmit}>
                <Form>
                    <label htmlFor="email">Email</label>
                    <Field name="email" type="text" required autoFocus></Field>
                    <label htmlFor="password">Senha</label>
                    <Field name="password" type="password" required></Field>
                    <button type="submit">Logar</button>
                </Form>
            </Formik>
        </>
    )
}
export default Login;