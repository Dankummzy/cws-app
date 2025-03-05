import React, { useState } from 'react';
import { fetchCurrencyConversion } from '../services/apiService';
import { Button, Form, Container } from 'react-bootstrap';

const CurrencyConverter = () => {
    const [baseCurrency, setBaseCurrency] = useState('');
    const [targetCurrency, setTargetCurrency] = useState('');
    const [amount, setAmount] = useState('');
    const [result, setResult] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await fetchCurrencyConversion(baseCurrency, targetCurrency, amount);
        setResult(data);
    };

    return (
        <Container>
            <h2>Currency Conversion</h2>
            <Form onSubmit={handleSubmit}>
                <Form.Group>
                    <Form.Label>Base Currency</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="e.g., USD"
                        value={baseCurrency}
                        onChange={(e) => setBaseCurrency(e.target.value)}
                        required
                    />
                </Form.Group>
                <Form.Group>
                    <Form.Label>Target Currency</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="e.g., EUR"
                        value={targetCurrency}
                        onChange={(e) => setTargetCurrency(e.target.value)}
                        required
                    />
                </Form.Group>
                <Form.Group>
                    <Form.Label>Amount</Form.Label>
                    <Form.Control
                        type="number"
                        placeholder="Enter amount"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        required
                    />
                </Form.Group>
                <Button type="submit" variant="primary">Convert</Button>
            </Form>
            {result && (
                <div className="result-card">
                    <h4>Converted Amount: {result.converted_amount}</h4>
                    <p>Rate: {result.rate}</p>
                </div>
            )}
        </Container>
    );
};

export default CurrencyConverter;
