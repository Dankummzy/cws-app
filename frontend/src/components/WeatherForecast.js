import React, { useState } from 'react';
import { fetchWeather } from '../services/apiService';
import { Button, Form, Container } from 'react-bootstrap';

const WeatherForecast = () => {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await fetchWeather(city);
        setWeather(data);
    };

    return (
        <Container>
            <h2>Weather Prediction</h2>
            <Form onSubmit={handleSubmit}>
                <Form.Group>
                    <Form.Label>City</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter city name"
                        value={city}
                        onChange={(e) => setCity(e.target.value)}
                        required
                    />
                </Form.Group>
                <Button type="submit" variant="primary">Get Weather</Button>
            </Form>
            {weather && (
                <div className="mt-4">
                    <h4>{weather.name}</h4>
                    <p>Temperature: {weather.main.temp}°C</p>
                    <p>Condition: {weather.weather[0].description}</p>
                </div>
            )}
        </Container>
    );
};

export default WeatherForecast;
