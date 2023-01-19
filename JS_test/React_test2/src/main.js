import React from 'react';
import ReactDOM from 'react-dom';
import Header from './Meme_Generator/Header';
import Meme from './Meme_Generator/Meme';

function Page(){
    return (
        <div>
            <Header />
            <Meme />
        </div>
    );
};

ReactDOM.render(<Page />, document.getElementById('root'));