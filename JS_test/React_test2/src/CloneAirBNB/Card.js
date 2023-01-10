import React from 'react';

export default function Card(props){
    return (
        <div className='card'>
            <img src={`./src/assets/${props.img}`} className='person-img'/>
            <div className='card-state'>
                <img src='./src/assets/star3.png' className='star'/>
                <span>{props.rating}</span>
                <span className='gray'>({props.reviewCount}) </span>
                <span className='gray'>{props.country}</span>
            </div>
            <p>{props.title}</p>
            <p><span className='bold'>From ${props.price}</span> / person</p>
        </div>
    );
};