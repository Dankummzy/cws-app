import React, { useState } from 'react';
import { fetchStockData } from '../services/apiService';
import { Button, Form, Container } from 'react-bootstrap';
import { Line } from 'react-chartjs-2';

const StockTracker = () => {
    const [symbol, setSymbol] = useState('');
    const [stockData, setStockData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await fetchStockData(symbol);
        setStockData(data);
    };

    return (
        <Container>
            <h2>Stock Tracker</h2>
            <Form onSubmit={handleSubmit}>
                <Form.Group>
                    <Form.Label>Stock Symbol</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="e.g., AAPL"
                        value={symbol}
                        onChange={(e) => setSymbol(e.target.value)}
                        required
                    />
                </Form.Group>
                <Button type="submit" variant="primary">Track Stock</Button>
            </Form>
            {stockData && stockData.prices && (
                <div className="mt-4">
                    <Line
                        data={{
                            labels: Object.keys(stockData.prices).slice(0, 10),
                            datasets: [
                                {
                                    label: 'Stock Price',
                                    data: Object.values(stockData.prices).slice(0, 10).map(p => parseFloat(p['4. close'])),
                                    borderColor: 'rgba(75,192,192,1)',
                                    fill: false,
                                },
                            ],
                        }}
                    />
                </div>
            )}
        </Container>
    );
};

export default StockTracker;
