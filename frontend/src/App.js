import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AppNavbar from './components/Navbar';
import Footer from './components/Footer';
import CurrencyConverter from './components/CurrencyConverter';
import WeatherForecast from './components/WeatherForecast';
import StockTracker from './components/StockTracker';

const App = () => (
    <Router>
        <AppNavbar />
        <div className="app-content">
            <Routes>
                <Route path="/" element={<CurrencyConverter />} />
                <Route path="/currency" element={<CurrencyConverter />} />
                <Route path="/weather" element={<WeatherForecast />} />
                <Route path="/stocks" element={<StockTracker />} />
            </Routes>
        </div>
        <Footer />
    </Router>
);

export default App;
