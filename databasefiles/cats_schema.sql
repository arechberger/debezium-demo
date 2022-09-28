CREATE TABLE cats (
    id serial PRIMARY KEY,
    name VARCHAR(200) UNIQUE NOT NULL,
    character VARCHAR(200)
);

CREATE TABLE furcolor (
    id serial PRIMARY KEY,
    title VARCHAR(200) UNIQUE NOT NULL
);

CREATE TABLE cat_fur (
    cat_id INT NOT NULL,
    furcolor_id INT NOT NULL,
    PRIMARY KEY(cat_id, furcolor_id),
    FOREIGN KEY (cat_id) REFERENCES cats(id),
    FOREIGN KEY (furcolor_id) REFERENCES furcolor(id)
);