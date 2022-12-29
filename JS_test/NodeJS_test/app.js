// import React from 'react';
// import ReactDOM  from 'react-dom';

//IMPORTS
// const some_module = require('./some_module'); //imported functions etc
// console.log(new some_module.SomeMathObject); //call a func

//LISTENERS
// const EventEmitter = require('events');
// const eventEmitter = new EventEmitter();

// eventEmitter.on('tutorial', (num1, num2) => {
//     console.log(num1 + num2);
// });
// eventEmitter.emit('tutorial', 1, 2);
// // console.log(sum(1,1));

// class Person extends EventEmitter{
//     constructor(name){
//         super();
//         this.name = name;
//     }
// }

// const john = new Person("John");
// john.on('get_name', () => {
//     console.log("My name is " + john.name);
// })

// john.emit('get_name');

//READ USER INPUT
// const readline = require('readline');
// const rl = readline.createInterface({input: process.stdin, output: process.stdout});

// let num1 = Math.floor((Math.random() * 10) + 1);
// let num2 = Math.floor((Math.random() * 10) + 1);
// let result = num1 + num2;

// rl.question("What is "  + num1 + " + " + num2 + "? \n", (input) => {
//     if (input.trim() == result){
//         rl.close();
//     }
//     else{
//         rl.setPrompt('Incorrect response, try again! \n');
//         rl.prompt();
//         rl.on('line',(input) => {
//             if (input == result){
//                 rl.close();
//             }
//             else{
//                 rl.setPrompt("Your answer is incorrectm try again\n");
//                 rl.prompt();
//             }
//         })
//     }
// });

// rl.on('close', () => {
//     console.log("Correct!");
// });

//FILE SYSTEM
// const fs = require('fs');
// fs.writeFile('example.txt', "this is somethign", (err) =>{ //create file
//     if (err){
//         console.log(err);
//     }
//     else{
//         console.log("file created");
//         fs.readFile('example.txt','utf-8', (err, file)=>{ //read file
//             if(err){
//                 console.log(err);
//             }
//             else{
//                 console.log(file);
//             }
//         });
//     }
// }); 

// fs.rename('example.txt', 'example2.txt', (err)=>{ //rename file
//     if (err){
//         console.log(err);
//     }
//     else{
//         console.log("Succesfully renamed a file");
//     }
// });

// fs.appendFile('example2.txt', 'Some data being appended', (err)=>{
//     if (err){
//         console.log(err);
//     }
//     else{
//         console.log("Succesfoully appended");
//     }
// });

// fs.unlink('example2.txt', (err)=>{
//     if (err){
//         console.log(err);
//     }
//     else{
//         console.log("File sucesfully deleted");
//     }
// });

// const fs = require('fs');
// fs.mkdir('tutorial', (err)=>{
//     if (err){
//         console.log(err);
//     }
//     else{
//         fs.writeFile('./tutorial/example.txt', 'Sometext',(err)=>{
//             if(err){
//                 console.log(err);
//             }
//             else{
//                 console.log("File created succesfully");
//             }
//         });
//     }
// });

// fs.rmdir('tutorial', (err)=>{
//     if (err){
//         console.log(err);
//     }
//     else{
//         console.log("Succesfully deleted a folder");
//     }
// });

// fs.readdir('tutorial', (err,files)=>{
//     if (err){
//         console.log(err);
//     }
//     else{
//         console.log(files);
//     }
// });

//STREAMS - for big files(just use it)
// const fs = require('fs');
// const zlib = require('zlib'); //transform stream
// const gzip = zlib.createGzip(); //example tr to zip file
// const readStream = fs.createReadStream('./tutorial/example.txt','utf-8');
// const writeStream = fs.createWriteStream('example1.txt');
// readStream.pipe(writeStream);

//HTTP SERVER (ROUTES)
// const http = require('http');
// const server = http.createServer((req,res)=>{
//     if(req.url === '/'){
//         res.write("Hello world");
//         res.end();
//     }
//     else{
//         res.write("Using some other domain");
//         res.end();
//     }
// });

// server.listen('3000');


//SEND SOMETHING TO SERVER
// const http = require('http');
// const fs = require('fs');
// http.createServer((req, res)=>{
//     const readStream = fs.createReadStream('./static/index.html');
//     res.writeHead(200,{'Content-type': 'text/html'});
//     readStream.pipe(res);
// }).listen('3000');

//Package.json npm init then NPM instll 'package' !!!!!!!!!!!!!!!!!!!!!!!!!
const _ = require('lodash');
let example = _.fill([1,2,3,4,5], "someshit", 1, 4);
console.log(example);
