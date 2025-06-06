const express = require('express');
const router = express.Router();
const db = require('../db');
const auth = require('../middleware/authMiddleware');

// @route   POST api/picks
// @desc    Submit or update a pick for the current week
router.post('/', auth, async (req, res) => {
    const { fixtureId, selectedTeamName } = req.body;
    const userId = req.user.id;
    const currentWeek = 37;

    try {
        // Check if user has already picked this team in the past
        const pastPicks = await db.query('SELECT * FROM picks WHERE user_id = $1 AND selected_team_name = $2 AND game_week != $3', [userId, selectedTeamName, currentWeek]);
        if (pastPicks.rows.length > 0) {
            return res.status(400).json({ msg: 'You have already picked this team. You cannot pick the same team twice.' });
        }

        // Upsert logic: Insert or update pick for the current week
        const upsertQuery = `
            INSERT INTO picks (user_id, fixture_id, selected_team_name, game_week) 
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (user_id, game_week) 
            DO UPDATE SET fixture_id = EXCLUDED.fixture_id, selected_team_name = EXCLUDED.selected_team_name
            RETURNING *;
        `;
        const result = await db.query(upsertQuery, [userId, fixtureId, selectedTeamName, currentWeek]);
        
        // Check if the pick was newly inserted or updated
        const wasUpdated = result.command === 'UPDATE';
        const message = wasUpdated ? 'Your pick has been updated.' : 'Pick submitted successfully!';

        res.json({ msg: message, pick: result.rows[0] });

    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server Error');
    }
});

// @route   GET api/picks/user
// @desc    Get all picks for the logged-in user
router.get('/user', auth, async (req, res) => {
    try {
        const picks = await db.query(
          `SELECT p.game_week, p.selected_team_name, f.home_team_name, f.away_team_name 
           FROM picks p
           JOIN fixtures f ON p.fixture_id = f.fixture_id
           WHERE p.user_id = $1 
           ORDER BY p.game_week DESC`, [req.user.id]);
        res.json(picks.rows);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server Error');
    }
});

module.exports = router;