const express = require('express');
const router = express.Router();

//middleware
router.use((req, res, next)=>{
    next();
});

router.get('/', (req, res)=>{
    res.sendFile(path.join(__dirname, 'static/index.html'));
});


module.exports = router;
