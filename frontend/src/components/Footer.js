import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const Footer = () => (
    <footer className="bg-dark text-light py-3">
        <Container>
            <Row>
                <Col className="text-center">
                    <p>&copy; {new Date().getFullYear()} Currency-Weather-Stocks | All Rights Reserved</p>
                </Col>
            </Row>
            <Row>
                <Col className="text-center">
                    <a
                        href="https://github.com/"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-light mx-2"
                    >
                        GitHub
                    </a>
                    <a
                        href="https://www.linkedin.com/in/"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-light mx-2"
                    >
                        LinkedIn
                    </a>
                </Col>
            </Row>
        </Container>
    </footer>
);

export default Footer;
