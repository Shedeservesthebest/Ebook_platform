-- Step 1: Create tables for each entity
CREATE TABLE User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Fullname VARCHAR(100),
    Address VARCHAR(255),
    Email VARCHAR(100),
    LastLoginDate DATE
);

CREATE TABLE VirtualBookshelf (
    ShelfID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50)
);

CREATE TABLE Review (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    ReviewText TEXT,
    Date DATE,
    UserID INT,
    BookID INT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);

CREATE TABLE BookClub (
    ClubID INT AUTO_INCREMENT PRIMARY KEY,
    ClubName VARCHAR(100),
    Description TEXT
);

CREATE TABLE Book (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(100),
    Genre VARCHAR(50),
    ReleaseDate DATE,
    Publisher VARCHAR(100)
);

CREATE TABLE Tag (
    TagID INT AUTO_INCREMENT PRIMARY KEY,
    TagName VARCHAR(50)
);

-- Step 2: Mapping of M:N Relationships
CREATE TABLE UserBookshelves (
    UserID INT,
    ShelfID INT,
    BookID INT,
    DateAdded DATE,
    PRIMARY KEY (UserID, ShelfID, BookID),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ShelfID) REFERENCES VirtualBookshelf(ShelfID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);

CREATE TABLE BookshelfBooks (
    ShelfID INT,
    BookID INT,
    PRIMARY KEY (ShelfID, BookID),
    FOREIGN KEY (ShelfID) REFERENCES VirtualBookshelf(ShelfID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);

CREATE TABLE UserReviews (
    UserID INT,
    ReviewID INT,
    BookID INT,
    PRIMARY KEY (UserID, ReviewID),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ReviewID) REFERENCES Review(ReviewID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);

CREATE TABLE UserFollows (
    FollowerID INT,
    FolloweeID INT,
    PRIMARY KEY (FollowerID, FolloweeID),
    FOREIGN KEY (FollowerID) REFERENCES User(UserID),
    FOREIGN KEY (FolloweeID) REFERENCES User(UserID)
);

CREATE TABLE UserBookClubs (
    UserID INT,
    ClubID INT,
    DateJoined DATE,
    PRIMARY KEY (UserID, ClubID),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ClubID) REFERENCES BookClub(ClubID)
);

CREATE TABLE BookTags (
    BookID INT,
    TagID INT,
    PRIMARY KEY (BookID, TagID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID),
    FOREIGN KEY (TagID) REFERENCES Tag(TagID)
);

