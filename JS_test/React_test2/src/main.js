import React from 'react';
import ReactDOM from 'react-dom';
import Navbar from './CloneAirBNB/Navbar';
import Hero from './CloneAirBNB/Hero';
import Card from './CloneAirBNB/Card';
import data from './data';

function Page(){
    const dataSet = data.map(data =>{
        return <Card 
            key={data.id}
            img={data.img}
            rating={data.rating}
            reviewCount={data.reviewCount}
            country={data.country}
            title={data.title}
            price={data.price}
            openSpots={data.openSpots}
        /> 
    });
    return(
        <div>
            <Navbar />
            <section className='cards-list'>
                {dataSet}
            </section>
        </div>
    );
};

ReactDOM.render(<Page />, document.getElementById('root'));