const express = require('express');
const router = express.Router();
const db = require('../db');
const auth = require('../middleware/authMiddleware');

// @route   GET api/fixtures/current
// @desc    Get current week's fixtures (Week 37 for now)
router.get('/current', auth, async (req, res) => {
    try {
        const currentWeek = 37; // Hardcoded for this build
        const fixtures = await db.query('SELECT * FROM fixtures WHERE game_week = $1 ORDER BY kickoff_time ASC', [currentWeek]);
        res.json(fixtures.rows);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server Error');
    }
});

module.exports = router;