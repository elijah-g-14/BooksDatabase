use library;

DROP PROCEDURE IF EXISTS GetByCategory;
DROP PROCEDURE IF EXISTS GetByYear;
DROP PROCEDURE IF EXISTS GetByAuthor;
DROP PROCEDURE IF EXISTS GetByLangYear;

DELIMITER //

CREATE PROCEDURE GetByCategory(IN category_name VARCHAR(255))
BEGIN
    SELECT B.title, GROUP_CONCAT(C.name SEPARATOR ', ') AS categories
    FROM books_Book B
    INNER JOIN books_BookCategories BC ON B.id = BC.book_id
    INNER JOIN books_Category C ON BC.category_id = C.id
    WHERE C.name = category_name
    GROUP BY B.id
    LIMIT 10;
END//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetByYear(IN year INT)
BEGIN
    SELECT B.title, A.name AS author, F.name AS format
    FROM books_Book B
    INNER JOIN books_BookAuthors BA ON B.id = BA.book_id
    INNER JOIN books_Author A ON BA.author_id = A.id
    INNER JOIN books_Format F ON B.format_id = F.id
    WHERE YEAR(B.publication_date) = year
    LIMIT 10;
END//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetByAuthor(IN author_name VARCHAR(255))
BEGIN
    SELECT B.title, A.name AS author, F.name AS format, GROUP_CONCAT(C.name SEPARATOR ', ') AS categories
    FROM books_Book B
    INNER JOIN books_BookAuthors BA ON B.id = BA.book_id
    INNER JOIN books_Author A ON BA.author_id = A.id
    INNER JOIN books_Format F ON B.format_id = F.id
    INNER JOIN books_BookCategories BC ON B.id = BC.book_id
    INNER JOIN books_Category C ON BC.category_id = C.id
    WHERE A.name LIKE CONCAT('%', author_name, '%')
    GROUP BY B.id
    LIMIT 10;
END//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetByLangYear(IN lang VARCHAR(255), IN year INT)
BEGIN
    SELECT B.title, A.name AS author, F.name AS format, C.name AS category
    FROM books_Book B
    INNER JOIN books_BookAuthors BA ON B.id = BA.book_id
    INNER JOIN books_Author A ON BA.author_id = A.id
    INNER JOIN books_Format F ON B.format_id = F.id
    INNER JOIN books_BookCategories BC ON B.id = BC.book_id
    INNER JOIN books_Category C ON BC.category_id = C.id
    WHERE YEAR(B.publication_date) = year AND B.lang = lang
    LIMIT 10;
END//

DELIMITER ;





