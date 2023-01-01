const express = require('express');
const router = express.Router();

const credential = {
    username:"kejkej",
    password:"1234"
};

//login
router.post('/login', (req, res)=>{
    console.log(req.body);
    if(req.body.username == credential.username && req.body.password == credential.password){
        res.redirect('/');
    }
    else{
        res.end("Invalid username");
    }
});

module.exports = router;
