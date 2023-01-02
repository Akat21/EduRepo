const express = require('express');
const router = express.Router();

const credential = {
    username:"kejkej",
    password:"1234"
};

//middleware
router.use((req, res, next)=>{
    console.log("Time: ", Date.now());
    next();
});

router.get('/', (req, res)=>{
    res.sendFile(path.join(__dirname, 'static/index.html'));
});


module.exports = router;
