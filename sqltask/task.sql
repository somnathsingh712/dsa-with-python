-- the code run on powershell terminal
-- //1. Display UserName, RestaurantName, BillAmount

mysql> create database assessment_db;
Query OK, 1 row affected (0.01 sec)
mysql> USE assessment_db;
Database changed
mysql> SELECT DATABASE();
+---------------+
| DATABASE()    |
+---------------+
| assessment_db |
+---------------+
1 row in set (0.00 sec)

mysql> SELECT DATABASE();
+---------------+
| DATABASE()    |
+---------------+
| assessment_db |
+---------------+
1 row in set (0.00 sec)
mysql> SHOW TABLES;
Empty set (0.01 sec)

mysql> CREATE TABLE Users (
    ->     UserID INT PRIMARY KEY,
    ->     UserName VARCHAR(50),
    ->     City VARCHAR(50),
    ->     AccountType VARCHAR(20)
    -> );
Query OK, 0 rows affected (0.05 sec)


-- //2 . List unique RestaurantName having delivery records
mysql> CREATE TABLE Restaurants (
    ->     RestaurantID INT PRIMARY KEY,
    ->     RestaurantName VARCHAR(100),
    ->     Cuisine VARCHAR(50),
    ->     Rating DECIMAL(2,1)
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> CREATE TABLE Orders (
    ->     OrderID INT PRIMARY KEY,
    ->     UserID INT,
    ->     RestaurantID INT,
    ->     BillAmount DECIMAL(10,2),
    ->     OrderDate DATE,
    ->     FOREIGN KEY (UserID) REFERENCES Users(UserID),
    ->     FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID)
    -> );
Query OK, 0 rows affected (0.07 sec)

mysql> CREATE TABLE Deliveries (
    ->     DeliveryID INT PRIMARY KEY,
    ->     OrderID INT,
    ->     DeliveryStatus VARCHAR(20),
    ->     DeliveryTimeMinutes INT,
    ->     FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    -> );
Query OK, 0 rows affected (0.13 sec)

mysql> INSERT INTO Users VALUES
    -> (1,'Aman Verma','Delhi','Premium'),
    -> (2,'Riya Sen','Mumbai','Regular');
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql>
mysql> INSERT INTO Restaurants VALUES
    -> (101,'Spice Symphony','North Indian',4.5),
    -> (102,'Pizza Express','Italian',3.9);
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql>
mysql> INSERT INTO Orders VALUES
    -> (501,1,101,1200.00,'2026-07-15'),
    -> (502,2,102,450.00,'2026-07-16');
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql>
mysql> INSERT INTO Deliveries VALUES
    -> (901,501,'Delivered',25),
    -> (902,502,'Delivered',42);
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> SELECT
    ->     u.UserName,
    ->     r.RestaurantName,
    ->     o.BillAmount
    -> FROM Users u
    -> JOIN Orders o
    ->     ON u.UserID = o.UserID
    -> JOIN Restaurants r
    ->     ON o.RestaurantID = r.RestaurantID;
+------------+----------------+------------+
| UserName   | RestaurantName | BillAmount |
+------------+----------------+------------+
| Aman Verma | Spice Symphony |    1200.00 |
| Riya Sen   | Pizza Express  |     450.00 |
+------------+----------------+------------+
2 rows in set (0.00 sec)

mysql> SHOW TABLES;
+-------------------------+
| Tables_in_assessment_db |
+-------------------------+
| deliveries              |
| orders                  |
| restaurants             |
| users                   |
+-------------------------+
4 rows in set (0.00 sec)

mysql> SELECT DISTINCT
    ->     r.RestaurantName
    -> FROM Restaurants r
    -> JOIN Orders o
    ->     ON r.RestaurantID = o.RestaurantID
    -> JOIN Deliveries d
    ->     ON o.OrderID = d.OrderID;
+----------------+
| RestaurantName |
+----------------+
| Spice Symphony |
| Pizza Express  |
+----------------+
2 rows in set (0.00 sec)

-- //3.Show OrderID and UserName where delivery time > 35 minutes
mysql> SELECT
    ->     o.OrderID,
    ->     u.UserName
    -> FROM Users u
    -> JOIN Orders o
    ->     ON u.UserID = o.UserID
    -> JOIN Deliveries d
    ->     ON o.OrderID = d.OrderID
    -> WHERE d.DeliveryTimeMinutes > 35;
+---------+----------+
| OrderID | UserName |
+---------+----------+
|     502 | Riya Sen |
+---------+----------+
1 row in set (0.00 sec)

--4  Total money spent by each user

mysql> SELECT
    ->     u.UserName,
    ->     SUM(o.BillAmount) AS TotalSpent
    -> FROM Users u
    -> JOIN Orders o
    ->     ON u.UserID = o.UserID
    -> GROUP BY u.UserName;
+------------+------------+
| UserName   | TotalSpent |
+------------+------------+
| Aman Verma |    1200.00 |
| Riya Sen   |     450.00 |
+------------+------------+
2 rows in set (0.00 sec)

-- //5. Show every user with total number of orders

mysql> SELECT
    ->     u.UserName,
    ->     COUNT(o.OrderID) AS OrderCount
    -> FROM Users u
    -> LEFT JOIN Orders o
    ->     ON u.UserID = o.UserID
    -> GROUP BY u.UserName;
+------------+------------+
| UserName   | OrderCount |
+------------+------------+
| Aman Verma |          1 |
| Riya Sen   |          1 |
+------------+------------+
2 rows in set (0.00 sec)

-- //6. Restaurants with revenue > ₹5000 from Delhi users
mysql> SELECT
    ->     r.RestaurantName,
    ->     SUM(o.BillAmount) AS TotalRevenue
    -> FROM Restaurants r
    -> JOIN Orders o
    ->     ON r.RestaurantID = o.RestaurantID
    -> JOIN Users u
    ->     ON o.UserID = u.UserID
    -> WHERE u.City = 'Delhi'
    -> GROUP BY r.RestaurantName
    -> HAVING SUM(o.BillAmount) > 5000;
Empty set (0.00 sec)
  
-- //7. Restaurants having Cancelled orders

mysql> SELECT
    ->     r.RestaurantName,
    ->     COUNT(*) AS CancelledOrders
    -> FROM Restaurants r
    -> JOIN Orders o
    ->     ON r.RestaurantID = o.RestaurantID
    -> JOIN Deliveries d
    ->     ON o.OrderID = d.OrderID
    -> WHERE d.DeliveryStatus = 'Cancelled'
    -> GROUP BY r.RestaurantName;
Empty set (0.00 sec)

-- //8. Users whose single order is greater than average order value

mysql> SELECT
    ->     u.UserName,
    ->     u.City
    -> FROM Users u
    -> JOIN Orders o
    ->     ON u.UserID = o.UserID
    -> WHERE o.BillAmount >
    -> (
    ->     SELECT AVG(BillAmount)
    ->     FROM Orders
    -> );
+------------+-------+
| UserName   | City  |
+------------+-------+
| Aman Verma | Delhi |
+------------+-------+
1 row in set (0.00 sec)

-- //9. Average delivery time for cuisines with average rating > 4.0

mysql> SELECT
    ->     r.Cuisine,
    ->     AVG(d.DeliveryTimeMinutes) AS AvgDeliveryTime
    -> FROM Restaurants r
    -> JOIN Orders o
    ->     ON r.RestaurantID = o.RestaurantID
    -> JOIN Deliveries d
    ->     ON o.OrderID = d.OrderID
    -> GROUP BY r.Cuisine
    -> HAVING AVG(r.Rating) > 4.0;
+--------------+-----------------+
| Cuisine      | AvgDeliveryTime |
+--------------+-----------------+
| North Indian |         25.0000 |
+--------------+-----------------+
1 row in set (0.00 sec)

-- //10. Rank restaurants within each cuisine by total orders

mysql> SELECT
    ->     r.Cuisine,
    ->     r.RestaurantName,
    ->     COUNT(o.OrderID) AS OrderCount,
    ->     RANK() OVER (
    ->         PARTITION BY r.Cuisine
    ->         ORDER BY COUNT(o.OrderID) DESC
    ->     ) AS RestaurantRank
    -> FROM Restaurants r
    -> LEFT JOIN Orders o
    ->     ON r.RestaurantID = o.RestaurantID
    -> GROUP BY
    ->     r.Cuisine,
    ->     r.RestaurantName;
+--------------+----------------+------------+----------------+
| Cuisine      | RestaurantName | OrderCount | RestaurantRank |
+--------------+----------------+------------+----------------+
| Italian      | Pizza Express  |          1 |              1 |
| North Indian | Spice Symphony |          1 |              1 |
+--------------+----------------+------------+----------------+
2 rows in set (0.00 sec)

mysql>