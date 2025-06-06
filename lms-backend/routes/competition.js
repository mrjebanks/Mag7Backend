const express = require('express');
const router = express.Router();
const db = require('../db');
const auth = require('../middleware/authMiddleware');

// @route   GET api/competition/status
// @desc    Get a list of users still in the competition
router.get('/status', auth, async (req, res) => {
    try {
        const standingUsers = await db.query(
            "SELECT user_id, first_name, last_name FROM users WHERE is_eliminated = FALSE ORDER BY last_name, first_name"
        );
        res.json(standingUsers.rows);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server Error');
    }
});

module.exports = router;