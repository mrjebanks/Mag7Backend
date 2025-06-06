const express = require('express');
const cors = require('cors');
require('dotenv').config();

const authRoutes = require('./routes/auth');
const fixtureRoutes = require('./routes/fixtures');
const pickRoutes = require('./routes/picks');
const competitionRoutes = require('./routes/competition');

const app = express();

// --- START: Production-Ready CORS Configuration ---

// Define the list of allowed origins (your frontend URLs)
const allowedOrigins = [
    'https://mag7-lms.vercel.app', // Your production frontend
    'http://localhost:3000'        // Your local development frontend
];

const corsOptions = {
    origin: function (origin, callback) {
        // The 'origin' is the URL of the site making the request (e.g., https://mag7-lms.vercel.app)
        // We check if this origin is in our list of allowed sites.
        if (allowedOrigins.indexOf(origin) !== -1 || !origin) {
            // If it is, or if the request has no origin (like a mobile app or curl), allow it.
            callback(null, true);
        } else {
            // If it's not, block it.
            callback(new Error('Not allowed by CORS'));
        }
    },
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    credentials: true,
};

// Use the new CORS options
app.use(cors(corsOptions));

// --- END: Production-Ready CORS Configuration ---


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
