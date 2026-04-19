CREATE TABLE file_manager (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(100) NOT NULL,
    file_size INTEGER NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE custom_file_manager (
    id SERIAL PRIMARY KEY,
    file_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    access_level VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES file_manager(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password) VALUES ('admin', 'password123');

INSERT INTO file_manager (file_name, file_type, file_size, file_path) VALUES ('example.txt', 'text/plain', 1024, '/path/to/example.txt');

INSERT INTO custom_file_manager (file_id, user_id, access_level) VALUES (1, 1, 'read');

CREATE OR REPLACE FUNCTION enter_file_manager(p_file_id INTEGER, p_user_id INTEGER)
RETURNS VOID AS $$
DECLARE
    v_file_manager custom_file_manager%ROWTYPE;
BEGIN
    SELECT * INTO v_file_manager FROM custom_file_manager WHERE file_id = p_file_id AND user_id = p_user_id;
    IF v_file_manager.access_level = 'read' THEN
        RAISE NOTICE 'You have read access to this file';
    ELSIF v_file_manager.access_level = 'write' THEN
        RAISE NOTICE 'You have write access to this file';
    ELSE
        RAISE NOTICE 'You do not have access to this file';
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION exit_file_manager(p_file_id INTEGER, p_user_id INTEGER)
RETURNS VOID AS $$
DECLARE
    v_file_manager custom_file_manager%ROWTYPE;
BEGIN
    SELECT * INTO v_file_manager FROM custom_file_manager WHERE file_id = p_file_id AND user_id = p_user_id;
    IF v_file_manager.access_level = 'read' THEN
        RAISE NOTICE 'You have exited the file manager with read access';
    ELSIF v_file_manager.access_level = 'write' THEN
        RAISE NOTICE 'You have exited the file manager with write access';
    ELSE
        RAISE NOTICE 'You do not have access to this file';
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT enter_file_manager(1, 1);
SELECT exit_file_manager(1, 1);