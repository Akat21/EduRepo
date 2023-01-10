import React from 'react';
import ReactDOM from 'react-dom';
import Navbar from './CloneAirBNB/Navbar';
import Hero from './CloneAirBNB/Hero';
import Card from './CloneAirBNB/Card';

function Page(){
    return(
        <div>
            <Navbar />
            <Card 
                img="some_dud.jpg"
                rating="5.0"
                reviewCount={6}
                country="USA"
                title="Life lessons with Katie Zafares"
                price={136}
            />
        </div>
    );
};

ReactDOM.render(<Page />, document.getElementById('root'));