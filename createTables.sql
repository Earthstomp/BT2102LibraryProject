CREATE TABLE Member(  
     ID    			VARCHAR(10)   NOT NULL UNIQUE,
	 Name           VARCHAR(30)    NOT NULL,
     Faculty        VARCHAR(15)   NOT NULL,
     PhoneNumber    VARCHAR(8)    NOT NULL,
     Email			VARCHAR(35)   NOT NULL UNIQUE,
	 PRIMARY KEY (ID)); 
     
CREATE TABLE Book(
     AccessionNumber VARCHAR(10)  NOT NULL UNIQUE,
     Title           VARCHAR(100)  NOT NULL,
     Author1         VARCHAR(30)  NOT NULL,
     Author2         VARCHAR(30),
     Author3         VARCHAR(30),
     ISBN            VARCHAR(13)  NOT NULL,
     Publisher       VARCHAR(50)  NOT NULL,  
     PublicationYear VARCHAR(4)   NOT NULL);
     
     
     
CREATE TABLE BookUpdated(
     AccessionNumber VARCHAR(10)  NOT NULL UNIQUE,
     Title           VARCHAR(100)  NOT NULL,
     Author1         VARCHAR(30)  NOT NULL,
     Author2         VARCHAR(30),
     Author3         VARCHAR(30),
     ISBN            VARCHAR(13)  NOT NULL,
     Publisher       VARCHAR(50)  NOT NULL,  
     PublicationYear VARCHAR(4)   NOT NULL,
	 BorrowDate      DATE,
	 ReserveDate     DATE,
	 ReturnDate      DATE,
     DueDate         DATE,
     MemberBorrowID  VARCHAR(10),
     MemberReserveID VARCHAR(10),
     PRIMARY KEY (AccessionNumber),
     FOREIGN KEY (MemberBorrowID) REFERENCES Member(ID),
     FOREIGN KEY (MemberReserveID) REFERENCES Member(ID));
 
CREATE TABLE Fine(
	 MemberID        VARCHAR(10)  NOT NULL UNIQUE,
     Amount          VARCHAR(1000)   NOT NULL,     
     FOREIGN KEY (MemberID) REFERENCES Member(ID) ON DELETE CASCADE);
     

     
     
     
     
     
    
