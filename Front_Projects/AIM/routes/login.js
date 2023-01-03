const express = require('express');
const router = express.Router();

const fs = require('fs');

let data = [0];
//middleware
router.use((req, res, next)=>{
    next();
});

router.get('/', (req, res)=>{
    res.render('login_base', {title:"Login system"});
});

//login
router.post('/', (req, res)=>{
    if(fs.existsSync('./database/username.txt')){
        const data = fs.readFileSync('./database/username.txt','utf-8').split(",");
        if (data.includes(req.body.username) == false){
            fs.appendFileSync('./database/username.txt', "," + req.body.username, 'utf-8');
        }
    }
    else{
        fs.writeFileSync('./database/username.txt', req.body.username, 'utf-8');
    }
    if(fs.existsSync('./database/points.txt')){
        data = fs.readFileSync('./database/points.txt', 'utf-8').split(',');
        data = data.map(Number);
    }
    res.redirect('/logged/?user=' + req.body.username + '&hs=' + Math.max(...data));
});

module.exports = router;
