const canvas = document.getElementById("canvas1");
const printHighscore = document.getElementById("highscore");
const ctx = canvas.getContext('2d');
const CANVAS_WIDTH = canvas.width = 600;
const CANVAS_HEIGHT = canvas.height = 600;
const AIM_WIDTH = 50;
const AIM_HEIGHT = 50;

const coo = [RandomNumberGenerator(CANVAS_WIDTH - AIM_WIDTH),RandomNumberGenerator(CANVAS_HEIGHT - AIM_HEIGHT)];

let rect_color = "#FF0000"; //red
let change_pos = setInterval(SetXY, 1000);
let points = 0;
let highscore = 0;

canvas.addEventListener("click", x => {
    if ((x.layerX > coo[0]) && (x.layerX < coo[0] + 50) && (x.layerY > coo[1]) && (x.layerY < coo[1] + 50)){
        //Change pos of Aim Rect if correct
        rect_color = "green";
        points += 1;
        SetXY();
        clearInterval(change_pos);
        change_pos = setInterval(SetXY, 1000);
    }
    else{
        //Change pos of Aim Rect if not correct
        rect_color = "#FF0000";
        if (points > highscore){
            highscore = points;
            points = 0;
            console.log(printHighscore.childNodes[3].value);
            printHighscore.childNodes[1].innerText = ("Highscore: " + highscore);
            printHighscore.childNodes[3].value = highscore;
        }
        points = 0;
    }
});

function draw(){
    //AIM RECT DRAW
    ctx.fillStyle = rect_color;
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    ctx.fillRect(coo[0], coo[1], AIM_WIDTH, AIM_HEIGHT);

    //POINTS DRAW
    ctx.fillStyle = "black";
    ctx.font = "30px Arial";
    ctx.fillText(points, 10, 30);

    //REFRESH FRAMES
    requestAnimationFrame(draw);
}

function RandomNumberGenerator(max){
    //Generate Random Number beetwen 0 and max
    return Math.floor(Math.random() * max);
}

function SetXY(){
    //Set Aim Rect to x - coo[0], y - coo[1]
    coo[0] = RandomNumberGenerator(CANVAS_WIDTH - AIM_WIDTH);
    coo[1] = RandomNumberGenerator(CANVAS_HEIGHT - AIM_HEIGHT);
}

draw();