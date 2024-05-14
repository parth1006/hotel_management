-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.33-community


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema hotel_management
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ hotel_management;
USE hotel_management;

--
-- Table structure for table `hotel_management`.`functions`
--

DROP TABLE IF EXISTS `functions`;
CREATE TABLE `functions` (
  `Booking_Id` varchar(20) NOT NULL DEFAULT '',
  `Funtion_Type` varchar(20) DEFAULT NULL,
  `Client_name` varchar(20) DEFAULT NULL,
  `Booking_Date` varchar(30) DEFAULT NULL,
  `Check_in_date` varchar(30) DEFAULT NULL,
  `check_out_date` varchar(30) DEFAULT NULL,
  `room_booked` int(20) DEFAULT NULL,
  `Halls_booked` varchar(30) DEFAULT NULL,
  `Price` int(40) DEFAULT NULL,
  PRIMARY KEY (`Booking_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_management`.`functions`
--

/*!40000 ALTER TABLE `functions` DISABLE KEYS */;
INSERT INTO `functions` (`Booking_Id`,`Funtion_Type`,`Client_name`,`Booking_Date`,`Check_in_date`,`check_out_date`,`room_booked`,`Halls_booked`,`Price`) VALUES 
 ('f123','Birthday Party','Mr. Raman Singh','23/07/2020','25/07/2020','25/07/2020',0,'H1',10000),
 ('f124','Reunion Party','Mrs. Akshita Rathi','10/08/2020','17/08/2020','19/09/2020',4,'H1 and H2',20000),
 ('f125','Marriage','Mr. Aditya Agarwal','24/10/2020','28/11/2020','02/12/2020',30,'H1 ,H2,H3 and ground',20000);
/*!40000 ALTER TABLE `functions` ENABLE KEYS */;


--
-- Table structure for table `hotel_management`.`guest_list`
--

DROP TABLE IF EXISTS `guest_list`;
CREATE TABLE `guest_list` (
  `Guest_Name` varchar(30) NOT NULL,
  `Guest_id` int(10) DEFAULT NULL,
  `moblie_no` int(10) DEFAULT NULL,
  `adhar_no` int(16) DEFAULT NULL,
  `room_no` int(10) DEFAULT NULL,
  `occupancy` int(10) DEFAULT NULL,
  `Booking_date` varchar(30) DEFAULT NULL,
  `check_in_date` varchar(20) DEFAULT NULL,
  `check_out_date` varchar(30) DEFAULT NULL,
  UNIQUE KEY `moblie_no` (`moblie_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_management`.`guest_list`
--

/*!40000 ALTER TABLE `guest_list` DISABLE KEYS */;
INSERT INTO `guest_list` (`Guest_Name`,`Guest_id`,`moblie_no`,`adhar_no`,`room_no`,`occupancy`,`Booking_date`,`check_in_date`,`check_out_date`) VALUES 
 ('Rahul Sharma',1020,90335690,17820939,101,2,'20/02/2020','22/02/2020','28/02/2020'),
 ('Akash Mathur',1021,73000440,92193066,102,2,'29/04/2020','29/04/2020','10/05/2020'),
 ('Samay Raina',1022,87098840,15679860,103,2,'19/04/2020','19/04/2020','23/04/2020'),
 ('Suhani Shah',1023,99546783,19874563,102,3,'20/05/2020','23/05/2020','25/05/2020');
/*!40000 ALTER TABLE `guest_list` ENABLE KEYS */;


--
-- Table structure for table `hotel_management`.`login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `user` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_management`.`login`
--

/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` (`user`,`password`) VALUES 
 ('user','ip');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;


--
-- Table structure for table `hotel_management`.`room_list`
--

DROP TABLE IF EXISTS `room_list`;
CREATE TABLE `room_list` (
  `Room_no` int(200) NOT NULL,
  `room_type` varchar(30) NOT NULL,
  `Floor` varchar(30) DEFAULT NULL,
  `No_of_beds` int(20) DEFAULT NULL,
  `Overnight_Price` int(40) DEFAULT NULL,
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hotel_management`.`room_list`
--

/*!40000 ALTER TABLE `room_list` DISABLE KEYS */;
INSERT INTO `room_list` (`Room_no`,`room_type`,`Floor`,`No_of_beds`,`Overnight_Price`) VALUES 
 (101,'Silver','First',2,3000),
 (102,'Gold',' First',2,5000),
 (103,'Silver',' First',2,3500),
 (104,'Suite',' First',3,8000);
/*!40000 ALTER TABLE `room_list` ENABLE KEYS */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
