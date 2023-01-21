import React from "react";
import memesData from "../memesData";

export default function Meme(){
    const [memeImg, setMemeImg] = React.useState("");

    function getMemeImg(){
        const memesArray = memesData.data.memes;
        const randomNum = Math.floor(Math.random() * (memesArray.length));
        console.log(randomNum)
        setMemeImg(memesArray[randomNum].url)
    }

    return(
        <main>
            <div className="form">
                <input className="form--input" type="text"></input>
                <input className="form--input" type="text"></input>
                <button className="form--button" onClick={getMemeImg}>Get a new meme image</button>
            </div>
            <img src={memeImg} className="meme--img"/>
        </main>
    )
}