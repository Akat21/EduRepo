const express = require('express');
const path = require('path');
const app = express();
const fs = require('fs');
const bodyparser = require('body-parser');
const session = require('express-session');

const router = require('./router');

//paths
app.use('/', express.static(path.join(__dirname, 'static')));

//bodyparser
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended:true}));

//router
app.use('/route', router);

//ejs set
app.set('view engine', 'ejs');

//routes
app.get('/', (req, res)=>{
    res.sendFile(path.join(__dirname, 'static/index.html'));
});

app.get('/login', (req, res)=>{
    res.render('login_base', {title:"Login system"});
});

app.get('/dashboard', (req,res)=>{
    res.render('dashboard', {title:"Main Page"});
});

//listen to port
app.listen(3000);
