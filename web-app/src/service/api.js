import axios from "axios";

export const api = axios.create({
    baseURL: process.env.REACT_APP_API

});
axios.defaults.headers.post["X-API-KEY"] = process.env.REACT_APP_API_KEY
axios.defaults.headers.post["Content-Type"] = "application/json"

export default api