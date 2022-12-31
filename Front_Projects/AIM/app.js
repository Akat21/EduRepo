const express = require('express');
const path = require('path');
const app = express();
const fs = require('fs');

app.use('/', express.static(path.join(__dirname, 'static')));


app.get('/', (req, res)=>{
    res.sendFile(path.join(__dirname, 'static/index.html'));
});

app.set('view engine', 'ejs');
app.get('/login', (req, res)=>{
    res.render('login_base', {title:"Login system"});
});

// app.post('/login', (req, res)=>{
//     console.log(req);
// });


app.listen(3000);
