import React from "react";

export default function Header(){
    return (
        <nav className="navbar">
            <div className="left-side">
                <img className="tf--img" src="./src/assets/tf.png" />
                <h1>Meme Generator</h1>
            </div>
            <h1 className="right-side">React Project 3</h1>
        </nav>
    );
}