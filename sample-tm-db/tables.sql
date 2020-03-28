CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydb`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `error_log`
--

DROP TABLE IF EXISTS `error_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `error_log` (
  `timestamp` datetime DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `error_log`
--

LOCK TABLES `error_log` WRITE;
/*!40000 ALTER TABLE `error_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `error_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telecommands`
--

DROP TABLE IF EXISTS `telecommands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `telecommands` (
  `receive_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `telecommand` varchar(200) DEFAULT NULL,
  `executed` tinyint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telecommands`
--

LOCK TABLES `telecommands` WRITE;
/*!40000 ALTER TABLE `telecommands` DISABLE KEYS */;
INSERT INTO `telecommands` (`receive_time`, `telecommand`, `executed`) VALUES ('2020-03-21 12:53:04','something',0),('2020-03-21 12:54:55','TURN ON LIGHT#1',0),('2020-03-21 12:55:07','TURN ON LIGHT#2',1),('2020-03-21 14:45:11','TURN ON AIRFAN',0),('2020-03-21 14:45:14','TURN ON HEATER',0),('2020-03-21 14:58:50','TURN ON HEATER',0),('2020-03-21 14:58:59','TURN ON HEATER',0),('2020-03-21 14:59:00','TURN ON HEATER',0),('2020-03-21 14:59:02','TURN ON HEATER',0),('2020-03-21 15:00:47','TURN ON HEATER',0),('2020-03-21 15:03:18','TURN ON HEATER',0),('2020-03-21 15:17:58','TURN ON HEATER',0),('2020-03-21 15:25:14','TURN ON HEATER',0),('2020-03-22 10:53:44','TURN ON HEATER',0),('2020-03-22 10:54:00','TURN ON HEATER',0),('2020-03-22 11:22:10','trhjeytkjrhrg',0),('2020-03-22 11:31:03','TURN ON HEATER',0),('2020-03-28 14:04:20','fefewgere',0),('2020-03-28 20:20:31','TURN ON HEATER',0),('2020-03-28 21:38:41','jkryukdtjrhrkr7',0);
/*!40000 ALTER TABLE `telecommands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telemetry`
--

DROP TABLE IF EXISTS `telemetry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `telemetry` (
  `gathered_time` datetime NOT NULL,
  `humidity` double DEFAULT NULL,
  `temperature` double DEFAULT NULL,
  `pressure` double DEFAULT NULL,
  `luminosity` double DEFAULT NULL,
  `lamps` int DEFAULT NULL,
  `airfan` tinyint DEFAULT NULL,
  `heater` tinyint DEFAULT NULL,
  PRIMARY KEY (`gathered_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telemetry`
--

LOCK TABLES `telemetry` WRITE;
/*!40000 ALTER TABLE `telemetry` DISABLE KEYS */;
INSERT INTO `telemetry` (`gathered_time`, `humidity`, `temperature`, `pressure`, `luminosity`, `lamps`, `airfan`, `heater`) VALUES ('2020-03-21 13:56:53',98,24,1024,0.4,2,1,0),('2020-03-21 13:56:55',98,24,1024,0.4,2,1,0),('2020-03-21 13:56:56',98,24,1024,0.4,2,1,0),('2020-03-21 13:57:10',98,25,1024,0.4,2,1,0),('2020-03-21 13:57:14',98,26,1024,0.4,2,1,0),('2020-03-21 13:57:18',98,27,1024,0.4,2,1,0),('2020-03-21 13:57:21',98,27.5,1024,0.4,2,1,0),('2020-03-21 13:57:27',98,27.5,200,0.4,2,1,0),('2020-03-21 13:57:31',98,27.5,100,0.4,2,1,0),('2020-03-21 16:10:49',90,22,990,0.8,3,1,1),('2020-03-21 16:14:14',90,22,990,0.8,3,1,1),('2020-03-21 16:17:58',90,22,990,0.8,3,1,1),('2020-03-21 16:25:14',90,23,990,0.7,1,1,1),('2020-03-22 11:53:44',90,23,990,0.7,1,1,1),('2020-03-22 11:54:00',90,23,990,0.7,1,1,1),('2020-03-22 12:19:42',89,19,999,0.5,0,0,0),('2020-03-22 12:31:03',90,23,990,0.7,1,1,1),('2020-03-28 16:33:46',90,23,999,0.9,2,0,1),('2020-03-28 19:40:10',90,23,999,0.9,2,0,1),('2020-03-28 21:20:31',90,23,999,0.9,2,0,1);
/*!40000 ALTER TABLE `telemetry` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-28 23:01:25
