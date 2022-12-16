const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext('2d');
const CANVAS_WIDTH = canvas.width = 600;
const CANVAS_HEIGHT = canvas.height = 600;
const AIM_WIDTH = 50;
const AIM_HEIGHT = 50;

const coo = [RandomNumberGenerator(CANVAS_WIDTH - AIM_WIDTH),RandomNumberGenerator(CANVAS_HEIGHT - AIM_HEIGHT)];

setInterval(SetXY, 1000);

function draw(){
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    ctx.fillRect(coo[0], coo[1], AIM_WIDTH, AIM_HEIGHT);
    ctx.fillStyle = "#FF0000";
    requestAnimationFrame(draw);
}

function RandomNumberGenerator(max){
    return Math.floor(Math.random() * max);
}

function SetXY(){
    coo[0] = RandomNumberGenerator(CANVAS_WIDTH - AIM_WIDTH);
    coo[1] = RandomNumberGenerator(CANVAS_HEIGHT - AIM_HEIGHT);
}

draw();