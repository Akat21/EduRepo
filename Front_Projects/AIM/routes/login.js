const express = require('express');
const router = express.Router();

const fs = require('fs');

//middleware
router.use((req, res, next)=>{
    console.log("Time: ", Date.now());
    next();
});

router.get('/', (req, res)=>{
    res.render('login_base', {title:"Login system"});
});

//login
router.post('/', (req, res)=>{
    console.log(req.body);
    if(fs.existsSync('./database/username.txt')){
        const data = fs.readFileSync('./database/username.txt','utf-8').split(",");
        if (data.includes(req.body.username) == false){
            fs.appendFile('./database/username.txt', "," + req.body.username, 'utf-8', (err)=>{
                if (err){
                    console.log(err);
                }
                else{
                    console.log("File appended successfully");
                }
            });
        }
    }
    else{
        fs.writeFile('./database/username.txt', req.body.username, 'utf-8', (err)=>{
            if (err){
                console.log(err);
            }
            else{
                console.log("File created successfully");
            }
        });

    }
    res.redirect('/');
});

module.exports = router;
