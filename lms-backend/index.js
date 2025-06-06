const express = require('express');
const cors = require('cors');
require('dotenv').config();

const authRoutes = require('./routes/auth');
const fixtureRoutes = require('./routes/fixtures');
const pickRoutes = require('./routes/picks');
const competitionRoutes = require('./routes/competition');

const app = express();

// --- START: CORS Configuration with Logging ---

const allowedOrigins = [
    'https://mag7-lms.vercel.app',
    'https://mag7-colsubi1y-james-projects-042a09cc.vercel.app',
    'http://localhost:3000'
];

const corsOptions = {
    origin: function (origin, callback) {
        // Log the incoming request's origin for debugging
        console.log(`[CORS] Request received from origin: ${origin}`);

        if (allowedOrigins.indexOf(origin) !== -1 || !origin) {
            console.log(`[CORS] Origin allowed: ${origin}`);
            callback(null, true);
        } else {
            console.error(`[CORS] Origin blocked: ${origin}`);
            callback(new Error('Not allowed by CORS'));
        }
    },
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    credentials: true,
};

app.use(cors(corsOptions));

// --- END: CORS Configuration with Logging ---

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
