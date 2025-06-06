const express = require('express');
const cors = require('cors');
require('dotenv').config();

const authRoutes = require('./routes/auth');
const fixtureRoutes = require('./routes/fixtures');
const pickRoutes = require('./routes/picks');
const competitionRoutes = require('./routes/competition');

const app = express();

// --- START: SUPER-PERMISSIVE CORS FOR DEBUGGING ---
// This allows requests from ANY origin. It is for testing only.
app.use(cors({
    origin: '*', // Allow all origins
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'], // Allow all methods
    credentials: true,
}));
// --- END: DEBUGGING CORS CONFIGURATION ---


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
