USE alx_book_store;

SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE table_name = 'books'