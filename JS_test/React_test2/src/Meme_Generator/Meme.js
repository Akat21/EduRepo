import React from "react";
import memesData from "../memesData.js";

export default function Meme(){
    const [meme, setMeme] = React.useState({
        topText: "",
        bottomText: "",
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

    function handleChange(event){
        const {name, value} = event.target
        setMeme(prevMeme =>({
            ...prevMeme,
            [name]: value
        }))
    }

    return(
        <main>
            <div className="form">
                <input 
                    className="form--input" 
                    type="text" 
                    placeholder="Top text" 
                    name="topText" 
                    value={meme.topText}
                    onChange={handleChange}
                />
                <input 
                    className="form--input" 
                    type="text" 
                    placeholder="Bottom text" 
                    name="bottomText" 
                    value={meme.bottomText}
                    onChange={handleChange}
                />
                <button className="form--button" onClick={getMemeImg}>Get a new meme image</button>
            </div>
            <div>
                <img src={meme.randomImg} className="meme--img"/>
                <h2 className="meme--text--top">{meme.topText}</h2>
                <h2 className="meme--text--bottom">{meme.bottomText}</h2>
            </div>
        </main>
    )
}