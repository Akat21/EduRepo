import React from "react";
import memesData from "../memesData.js";

export default function Meme(){
    const [meme, setMeme] = React.useState({
        topText: "",
        BottomText: "",
        randomImg: "./src/assets/drake.jpg"
    });

    const [allMemeImages, setAllMemeImages] = React.useState(memesData)

    function getMemeImg(){
        const memesArray = allMemeImages.data.memes;
        const randomNum = Math.floor(Math.random() * (memesArray.length));
        const url = memesArray[randomNum].url; 
        setMeme(prevMeme => ({
            ...prevMeme, 
            randomImg: url
        }));
    }

    return(
        <main>
            <div className="form">
                <input className="form--input" type="text" placeholder="Top text"></input>
                <input className="form--input" type="text" placeholder="Bottom text"></input>
                <button className="form--button" onClick={getMemeImg}>Get a new meme image</button>
            </div>
            <img src={meme.randomImg} className="meme--img"/>
        </main>
    )
}