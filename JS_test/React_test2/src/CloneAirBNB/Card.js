import React from 'react';

export default function Card(){
    return (
        <div className='card'>
            <img src='./src/assets/some_dud.jpg' className='person-img'/>
            <div className='card-state'>
                <img src='./src/assets/star3.png' className='star'/>
                <span>5.0</span>
                <span className='gray'>(6) </span>
                <span className='gray'>USA</span>
            </div>
            <p>Life lessons with Katie Zaferes</p>
            <p><span className='bold'>From $136</span> / person</p>
        </div>
    );
};