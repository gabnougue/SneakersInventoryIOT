CREATE TABLE IF NOT EXISTS sneaker (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    brand VARCHAR(100) NOT NULL,
    size INT NOT NULL,
    color VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS location (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip INT NOT NULL,
    temperature INT NOT NULL
);

CREATE TABLE IF NOT EXISTS sneaker_location (
    id SERIAL PRIMARY KEY,
    sneaker_id INT NOT NULL,
    location_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (sneaker_id) REFERENCES sneaker(id),
    FOREIGN KEY (location_id) REFERENCES location(id)
);
