-- Insert test users
-- Password for both users is "password123"
INSERT INTO users (first_name, last_name, email, password_hash) VALUES
('John', 'Doe', 'john.doe@test.com', '$2a$10$f.wtt8sP5S2pS3zlnLgGfui//21a58q9q.aP3A6bsoPxUFAy8yWj2'),
('Jane', 'Smith', 'jane.smith@test.com', '$2a$10$f.wtt8sP5S2pS3zlnLgGfui//21a58q9q.aP3A6bsoPxUFAy8yWj2');

-- Insert Premier League Week 37 Fixtures (using placeholder future dates for 2025)
INSERT INTO fixtures (game_week, home_team_name, away_team_name, kickoff_time) VALUES
(37, 'Fulham', 'Manchester City', '2025-05-11 12:30:00+00'),
(37, 'Bournemouth', 'Brentford', '2025-05-11 15:00:00+00'),
(37, 'Everton', 'Sheffield United', '2025-05-11 15:00:00+00'),
(37, 'Newcastle United', 'Brighton & Hove Albion', '2025-05-11 15:00:00+00'),
(37, 'Tottenham Hotspur', 'Burnley', '2025-05-11 15:00:00+00'),
(37, 'West Ham United', 'Luton Town', '2025-05-11 15:00:00+00'),
(37, 'Wolverhampton Wanderers', 'Crystal Palace', '2025-05-11 15:00:00+00'),
(37, 'Nottingham Forest', 'Chelsea', '2025-05-11 17:30:00+00'),
(37, 'Manchester United', 'Arsenal', '2025-05-12 16:30:00+00'),
(37, 'Aston Villa', 'Liverpool', '2025-05-13 20:00:00+00');

File: middleware/authMiddleware.js
const jwt = require('jsonwebtoken');

module.exports = function(req, res, next) {
    // Get token from header
    const token = req.header('x-auth-token');

    // Check if not token
    if (!token) {
        return res.status(401).json({ msg: 'No token, authorization denied' });
    }

    // Verify token
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.user = decoded.user;
        next();
    } catch (err) {
        res.status(401).json({ msg: 'Token is not valid' });
    }
};