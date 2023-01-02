const express = require('express');
const path = require('path');
const app = express();
const fs = require('fs');
const bodyparser = require('body-parser');

const login = require('./routes/login');
const home = require('./routes/home');

//paths
app.use('/', express.static(path.join(__dirname, 'static')));

//bodyparser
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended:true}));

//ejs set
app.set('view engine', 'ejs');

//router
app.use('/', home);
app.use('/login', login);

app.get('/dashboard', (req,res)=>{
    res.render('dashboard', {title:"Main Page"});
});

//listen to port
app.listen(3000);
