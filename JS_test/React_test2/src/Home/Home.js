import React from 'react';
import ReactDOM from 'react-dom'
import Header from './Header';
import MainHome from './MainHome';
import Footer from './Footer';

export default function Home(){
    return(
        <div>
            <Header />
            <MainHome />
            <Footer />
        </div>
    );
};