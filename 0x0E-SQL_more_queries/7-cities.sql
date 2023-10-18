-- Create the database hbtn_0d_usa if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table cities if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	FOREIGN KEY (state_id) REFERENCES states(id)
);

-- If success Display a success message
SELECT 'Database hbtn_0d_usa and table cities created' AS Status;

EXIT;
