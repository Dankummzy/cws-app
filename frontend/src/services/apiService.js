import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000/api';

export const fetchCurrencyConversion = async (baseCurrency, targetCurrency, amount) => {
    const response = await axios.get(`${API_BASE_URL}/convert/`, {
        params: { base_currency: baseCurrency, target_currency: targetCurrency, amount }
    });
    return response.data;
};

export const fetchWeather = async (city) => {
    const response = await axios.get(`${API_BASE_URL}/weather/`, { params: { city } });
    return response.data;
};

export const fetchStockData = async (symbol) => {
    const response = await axios.get(`${API_BASE_URL}/stock/`, { params: { symbol } });
    return response.data;
};
