import React from 'react';
import ReactDOM from 'react-dom';
import Main from './First_project/Main';
import Navbar from './First_project/Navbar';

function Page(){
    return(
        <div>
            <Navbar />      
            <Main />
        </div>
    );
};

ReactDOM.render(<Page />, document.getElementById('root'));