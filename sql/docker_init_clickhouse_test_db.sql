-- Create custom tables for the testing
CREATE TABLE test_table(
    id            INT,
    integer       INT NULL,
    text_col      TEXT,
    attribute_col TEXT NULL,
    bool_col      BOOL
)
ENGINE = MergeTree
PRIMARY KEY(id);

-- Insert dummy data into test_table
INSERT INTO test_table(
	id,
    integer,
	text_col,
	attribute_col,
	bool_col)
VALUES
(1, 1, 'first', 'attr_1', false);

INSERT INTO test_table(
	id,
    integer,
	text_col,
	attribute_col,
	bool_col)
VALUES
(2, 2, 'second', NULL,  true);

INSERT INTO test_table(
	id,
    integer,
	text_col,
	attribute_col,
	bool_col)
VALUES
(3, NULL, 'third', 'attr_1', false);

INSERT INTO test_table(
	id,
    integer,
	text_col,
	attribute_col,
	bool_col)
VALUES
(4, 4, 'fourth', 'attr_3', true);
