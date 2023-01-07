import React from 'react';
import ReactDOM from 'react-dom';
import Navbar from './CloneAirBNB/Navbar';
import Hero from './CloneAirBNB/Hero';

function Page(){
    return(
        <div>
            <Navbar />
            <Hero />      
        </div>
    );
};

ReactDOM.render(<Page />, document.getElementById('root'));