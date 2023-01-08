import React from 'react';
import ReactDOM from 'react-dom';
import Navbar from './CloneAirBNB/Navbar';
import Hero from './CloneAirBNB/Hero';
import Card from './CloneAirBNB/Card';

function Page(){
    return(
        <div>
            <Navbar />
            <Card />
        </div>
    );
};

ReactDOM.render(<Page />, document.getElementById('root'));