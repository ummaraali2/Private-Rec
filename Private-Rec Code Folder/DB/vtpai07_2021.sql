/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 5.5.30 : Database - vtpai07_2021
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`vtpai07_2021` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `vtpai07_2021`;

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `Name` varchar(255) DEFAULT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Mobile` varchar(255) DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `incent` */

DROP TABLE IF EXISTS `incent`;

CREATE TABLE `incent` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UID` varchar(255) DEFAULT NULL,
  `incent` int(11) DEFAULT NULL,
  `Da` varchar(255) DEFAULT NULL,
  KEY `Id` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Model` varchar(255) DEFAULT NULL,
  `Features` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Company` varchar(255) DEFAULT NULL,
  KEY `Id` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Table structure for table `recommendation` */

DROP TABLE IF EXISTS `recommendation`;

CREATE TABLE `recommendation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hashc` varchar(255) DEFAULT NULL,
  `review` varchar(255) DEFAULT NULL,
  `phash` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `Pid` varchar(255) DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Table structure for table `ubuy` */

DROP TABLE IF EXISTS `ubuy`;

CREATE TABLE `ubuy` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Model` varchar(255) DEFAULT NULL,
  `Features` varchar(255) DEFAULT NULL,
  `Price` varchar(255) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `uid` varchar(255) DEFAULT NULL,
  `Company` varchar(255) DEFAULT NULL,
  `Pid` int(11) DEFAULT NULL,
  `Status` varchar(255) DEFAULT NULL,
  KEY `Id` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Table structure for table `urev` */

DROP TABLE IF EXISTS `urev`;

CREATE TABLE `urev` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Uid` varchar(255) DEFAULT NULL,
  `PId` int(11) DEFAULT NULL,
  `Review` longtext,
  `Sta` varchar(255) DEFAULT NULL,
  KEY `Id` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `FName` varchar(255) DEFAULT NULL,
  `LName` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Mobile` varchar(255) DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `Company` varchar(255) DEFAULT NULL,
  `Sta` varchar(255) DEFAULT NULL,
  `UID` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
