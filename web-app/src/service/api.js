import axios from "axios";

export const api = axios.create({
    baseURL: process.env.REACT_APP_API

});
api.defaults.headers.common["X-API-KEY"] = process.env.REACT_APP_API_KEY


export default api