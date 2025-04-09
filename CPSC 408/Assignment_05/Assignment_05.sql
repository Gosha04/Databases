CREATE TABLE `driver` (
  `driverID` int NOT NULL,
  `Name` varchar(40) DEFAULT NULL,
  `Rating` int DEFAULT NULL,
  `Driving` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`driverID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver`
--

LOCK TABLES `driver` WRITE;
/*!40000 ALTER TABLE `driver` DISABLE KEYS */;
INSERT INTO `driver` VALUES (0,'Josh',3,0),(1,'Ethan',4,0);
/*!40000 ALTER TABLE `driver` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `rider` (
  `riderID` int NOT NULL,
  `lastrideID` int DEFAULT NULL,
  `Name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`riderID`),
  KEY `lastrideID` (`lastrideID`),
  CONSTRAINT `fk_lastrideID` FOREIGN KEY (`lastrideID`) REFERENCES `rides` (`rideID`),
  CONSTRAINT `lastrideID` FOREIGN KEY (`lastrideID`) REFERENCES `rides` (`rideID`),
  CONSTRAINT `rider_ibfk_1` FOREIGN KEY (`lastrideID`) REFERENCES `rides` (`rideID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rider`
--

LOCK TABLES `rider` WRITE;
/*!40000 ALTER TABLE `rider` DISABLE KEYS */;
INSERT INTO `rider` VALUES (0,NULL,'Maks'),(1,NULL,'Edward');
/*!40000 ALTER TABLE `rider` ENABLE KEYS */;
UNLOCK TABLES;

CREATE TABLE `rides` (
  `rideID` int NOT NULL,
  `riderID` int DEFAULT NULL,
  `driverID` int DEFAULT NULL,
  `startSpot` varchar(40) DEFAULT NULL,
  `endSpot` varchar(40) DEFAULT NULL,
  `Completed` tinyint(1) DEFAULT NULL,
  `driveRating` int DEFAULT NULL,
  PRIMARY KEY (`rideID`),
  KEY `riderID` (`riderID`),
  KEY `driverID` (`driverID`),
  CONSTRAINT `rides_ibfk_1` FOREIGN KEY (`riderID`) REFERENCES `rider` (`riderID`),
  CONSTRAINT `rides_ibfk_2` FOREIGN KEY (`driverID`) REFERENCES `driver` (`driverID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rides`
--

LOCK TABLES `rides` WRITE;
/*!40000 ALTER TABLE `rides` DISABLE KEYS */;
INSERT INTO `rides` VALUES (0,0,0,'Chapman','Grand',1,4),(1,1,1,'Chapman','Grand',1,5),(2,1,0,'Chapman','Court',1,2),(3,0,1,'Chapman','Court',1,3);
/*!40000 ALTER TABLE `rides` ENABLE KEYS */;
UNLOCK TABLES;