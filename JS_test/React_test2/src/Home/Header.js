import React from 'react';
import ReactDOM from 'react-dom'

export default function Header(){
    return (
        <header>
            <nav className="nav">
                <img src="./src/assets/react.png" width="40px"/>
                <ul className="nav-items">
                    <li>Pricing</li>
                    <li>About</li>
                    <li>Contact</li>
                </ul>
            </nav>
        </header>
    );
};