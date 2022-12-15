import React from 'react'
import { Formik, Form, Field } from 'formik'
import api from "../../service/api"

const Submit = () => {
    const handleSubmit = async values => {
        const { data } = await api.post('/message', values);
        alert(data.Status)
      }
    return (
        <>
            <h3>Enviar Mensagem</h3>
            <Formik initialValues={{ subject: '', message: '' }} onSubmit={handleSubmit}>
                <Form>
                    <label htmlFor="subject">Tópico</label>
                    <Field name="subject" type="text" required autoFocus></Field><br></br>
                    <label htmlFor="message">Mensagem</label>
                    <Field name="message" type="text" required></Field> <br></br>
                    <button type="submit">Enviar</button>
                </Form>
            </Formik>
        </>
    )
}
export default Submit;