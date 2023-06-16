BEGIN TRANSACTION;CREATE TABLE category(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(16) NOT NULL,
            description TEXT
        );INSERT INTO "category" VALUES(1,'gadget','some desc');INSERT INTO "category" VALUES(2,'beverages','');INSERT INTO "category" VALUES(3,'fake_name','fake_description');CREATE TABLE "product"(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL CHECK (length(name) > 1) UNIQUE,
            description TEXT,
            category_id INTEGER NOT NULL,
            manager TEXT,
            wholeprice DECIMAL(10, 2) CHECK (wholeprice > 0),
            price DECIMAL(10, 2) CHECK (price >= wholeprice), weight REAL,
            FOREIGN KEY (category_id) REFERENCES category(id)
        );INSERT INTO "product" VALUES(1,'laptop','111111111',1,NULL,50,100,1.5);INSERT INTO "product" VALUES(2,'sprite','22222222222',2,NULL,1,1.25,NULL);CREATE TABLE user(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            login TEXT NOT NULL CHECK (length(login) > 5) UNIQUE,
            password TEXT NOT NULL
        );INSERT INTO "user" VALUES(1,'Alex','qwerty','45c48cce2e2d7fbdea1afc51c7c6ad26');INSERT INTO "user" VALUES(2,'Max','qwwerty1','c4ca4238a0b923820dcc509a6f75849b');DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('user',2);INSERT INTO "sqlite_sequence" VALUES('category',3);INSERT INTO "sqlite_sequence" VALUES('product',2);COMMIT;