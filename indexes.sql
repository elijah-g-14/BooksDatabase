use library;

DROP INDEX IF EXISTS Category_name_index ON books_Category;
DROP INDEX IF EXISTS publication_date_index ON books_Book;
DROP INDEX IF EXISTS author_name_index ON books_Author;
DROP INDEX IF EXISTS lang_index ON books_Book;

ALTER TABLE `books_Category` ADD INDEX `Category_name_index` (`name`);
ALTER TABLE `books_Book` ADD INDEX `publication_date_index` (`publication_date`);
ALTER TABLE `books_Author` ADD INDEX `author_name_index` (`name`);
ALTER TABLE `books_Book` ADD INDEX `lang_index` (`lang`);