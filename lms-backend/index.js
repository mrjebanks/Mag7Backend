const express = require('express');
const cors = require('cors');
require('dotenv').config();

const authRoutes = require('./routes/auth');
const fixtureRoutes = require('./routes/fixtures');
const pickRoutes = require('./routes/picks');
const competitionRoutes = require('./routes/competition');

const app = express();

// Middleware
// The origin should be your Vercel deployment URL in production.
app.use(cors({
    origin: process.env.FRONTEND_URL || 'http://localhost:3000',
    credentials: true,
}));
app.use(express.json());

// API Routes
app.use('/api/auth', authRoutes);
app.use('/api/fixtures', fixtureRoutes);
app.use('/api/picks', pickRoutes);
app.use('/api/competition', competitionRoutes);

// Welcome Route
app.get('/', (req, res) => {
  res.send('Last Man Standing API is running...');
});

const PORT = process.env.PORT || 3001;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});