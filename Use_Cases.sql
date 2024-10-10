SELECT b.Title, b.Author, r.Rating
FROM Book b
JOIN Review r ON b.BookID = r.BookID
WHERE b.Genre = 'sint' AND r.Rating >= 2;

SELECT Title, Author, ReleaseDate
FROM Book
WHERE Genre = 'provident' AND ReleaseDate >= '1973-03-29'
   OR Author = 'esse' AND ReleaseDate >= '1973-03-29'
   ;
   
SELECT u.Email, MAX(ub.DateAdded) AS LastActivity
FROM User u
LEFT JOIN UserBookshelves ub ON u.UserID = ub.UserID
WHERE u.LastLoginDate < DATE_SUB(CURDATE(), INTERVAL 1 DAY)
GROUP BY u.UserID, u.Email;

SELECT b.Title, b.Author
FROM Book b
JOIN Review r ON b.BookID = r.BookID
JOIN UserFollows uf ON uf.FolloweeID = r.UserID
WHERE uf.FollowerID = 6
GROUP BY b.BookID
ORDER BY AVG(r.Rating) DESC
LIMIT 10;

SELECT u.Email, MAX(ub.DateAdded) AS LastActivity, ub.Status
FROM User u
LEFT JOIN UserBookshelves ub ON u.UserID = 3
WHERE u.LastLoginDate < DATE_SUB(CURDATE(), INTERVAL 180 DAY)
GROUP BY u.UserID, u.Email, ub.Status;

SELECT b.Title, b.Author, r.Rating
FROM Book b
JOIN Review r ON b.BookID = r.BookID
WHERE b.Genre = 'sint' AND r.Rating >= 1;






