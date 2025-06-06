const express = require('express');
const cors = require('cors');
require('dotenv').config();

const authRoutes = require('./routes/auth');
const fixtureRoutes = require('./routes/fixtures');
const pickRoutes = require('./routes/picks');
const competitionRoutes = require('./routes/competition');

const app = express();

// --- START: NEW CORS CONFIGURATION ---

// Define the list of allowed origins (your frontend URLs)
const allowedOrigins = [
    'https://mag7-lms.vercel.app', // Your production frontend
    'http://localhost:3000'        // Your local development frontend
];

const corsOptions = {
    origin: function (origin, callback) {
        // Allow requests with no origin (like mobile apps or curl requests)
        if (!origin) return callback(null, true);
        
        if (allowedOrigins.indexOf(origin) === -1) {
            const msg = 'The CORS policy for this site does not allow access from the specified Origin.';
            return callback(new Error(msg), false);
        }
        return callback(null, true);
    },
    credentials: true,
};

// Use the new CORS options
app.use(cors(corsOptions));

// --- END: NEW CORS CONFIGURATION ---


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
