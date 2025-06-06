-- Create the users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_eliminated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create the fixtures table
CREATE TABLE fixtures (
    fixture_id SERIAL PRIMARY KEY,
    game_week INT NOT NULL,
    home_team_name VARCHAR(100) NOT NULL,
    away_team_name VARCHAR(100) NOT NULL,
    kickoff_time TIMESTAMP WITH TIME ZONE NOT NULL,
    home_team_score INT,
    away_team_score INT
);

-- Create the picks table
CREATE TABLE picks (
    pick_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    fixture_id INT NOT NULL,
    selected_team_name VARCHAR(100) NOT NULL,
    game_week INT NOT NULL,
    is_correct BOOLEAN, -- NULL until result is known, TRUE for win, FALSE for loss/draw
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (fixture_id) REFERENCES fixtures(fixture_id)
);

-- Add a constraint to ensure one pick per user per week
ALTER TABLE picks
ADD CONSTRAINT unique_user_pick_per_week UNIQUE (user_id, game_week);