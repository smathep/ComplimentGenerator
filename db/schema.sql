DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS compliments;
-- DROP TABLE IF EXISTS view_count;

CREATE TABLE authors(
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    l_name TEXT NOT NULL,
    f_name TEXT NOT NULL
);

CREATE TABLE compliments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER,
    content TEXT NOT NULL,
    view_count INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(author_id) REFERENCES authors(author_id)
);

-- CREATE TABLE view_count(
--     compliment_id INTEGER PRIMARY KEY,
--     view_count INTEGER NOT NULL DEFAULT 0,
--     FOREIGN KEY(compliment_id) REFERENCES compliments(id)
-- );
