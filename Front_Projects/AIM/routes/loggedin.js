const express = require('express');
const router = express.Router();
const fs = require('fs');
let currUser = '';

//middleware
router.use((req, res, next)=>{
    next();
});

router.get('/', (req, res)=>{
    currUser = req.query.user;
    res.render('home_logged', {title:"AIM Training", user:req.query.user, hs:req.query.hs});
});

router.post('/', (req, res)=>{
    if(fs.existsSync('./database/points.txt')){
        fs.appendFileSync('./database/points.txt', "," + req.body.hs, 'utf-8');
        let data = fs.readFileSync('./database/points.txt', 'utf-8').split(',');
        data = data.map(Number);
        res.redirect('logged/?user=' + currUser + '&hs=' + Math.max(...data));
    }
    else{
        fs.writeFileSync('./database/points.txt', req.body.hs, 'utf-8');
    }
});

module.exports = router;
