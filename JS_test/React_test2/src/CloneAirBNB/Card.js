import React from 'react';

export default function Card(props){
    return (
        <div className='card'>
            {props.openSpots === 0 && <div className='card-badge'>SOLD OUT</div>}
            <img src={`./src/assets/${props.img}`} className='person-img'/>
            <div className='card-state'>
                <img src='./src/assets/star3.png' className='star'/>
                <span>{props.rating}</span>
                <span className='gray'>({props.reviewCount}) </span>
                <span className='gray'>{props.country}</span>
            </div>
            <p className='card-title'>{props.title}</p>
            <p><span className='bold'>From ${props.price}</span> / person</p>
        </div>
    );
};