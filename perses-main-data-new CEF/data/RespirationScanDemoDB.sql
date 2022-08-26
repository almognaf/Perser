-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: af
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `algorithmmatch`
--

DROP TABLE IF EXISTS `algorithmmatch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `algorithmmatch` (
  `id` int(255) NOT NULL,
  `algorithm` varchar(255) DEFAULT NULL,
  `compound_id` int(255) DEFAULT NULL,
  `cas_rn` varchar(255) DEFAULT NULL,
  `probability` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `compound_id` (`compound_id`),
  CONSTRAINT `algorithmmatch_ibfk_1` FOREIGN KEY (`compound_id`) REFERENCES `compound` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithmmatch`
--

LOCK TABLES `algorithmmatch` WRITE;
/*!40000 ALTER TABLE `algorithmmatch` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithmmatch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analyzer`
--

DROP TABLE IF EXISTS `analyzer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analyzer` (
  `id` int(255) NOT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `site` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analyzer`
--

LOCK TABLES `analyzer` WRITE;
/*!40000 ALTER TABLE `analyzer` DISABLE KEYS */;
/*!40000 ALTER TABLE `analyzer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bacteria`
--

DROP TABLE IF EXISTS `bacteria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bacteria` (
  `id` int(255) NOT NULL,
  `family_id` int(255) DEFAULT NULL,
  `strain` varchar(255) DEFAULT 'unknown',
  PRIMARY KEY (`id`),
  KEY `family_id` (`family_id`),
  CONSTRAINT `bacteria_ibfk_1` FOREIGN KEY (`family_id`) REFERENCES `bacteriafamily` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bacteria`
--

LOCK TABLES `bacteria` WRITE;
/*!40000 ALTER TABLE `bacteria` DISABLE KEYS */;
/*!40000 ALTER TABLE `bacteria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bacteriafamily`
--

DROP TABLE IF EXISTS `bacteriafamily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bacteriafamily` (
  `id` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bacteriafamily`
--

LOCK TABLES `bacteriafamily` WRITE;
/*!40000 ALTER TABLE `bacteriafamily` DISABLE KEYS */;
/*!40000 ALTER TABLE `bacteriafamily` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bacteriaset`
--

DROP TABLE IF EXISTS `bacteriaset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bacteriaset` (
  `id` int(255) NOT NULL,
  `bacteria_strain_id` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bacteria_strain_id` (`bacteria_strain_id`),
  CONSTRAINT `bacteriaset_ibfk_1` FOREIGN KEY (`bacteria_strain_id`) REFERENCES `bacteria` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bacteriaset`
--

LOCK TABLES `bacteriaset` WRITE;
/*!40000 ALTER TABLE `bacteriaset` DISABLE KEYS */;
/*!40000 ALTER TABLE `bacteriaset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compound`
--

DROP TABLE IF EXISTS `compound`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compound` (
  `id` int(255) NOT NULL,
  `measurement_id` int(255) DEFAULT NULL,
  `spectrum_id` int(255) DEFAULT NULL,
  `mass` float DEFAULT NULL,
  `retention_time` float DEFAULT NULL,
  `area` float DEFAULT NULL,
  `max_value` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `measurement_id` (`measurement_id`),
  KEY `spectrum_id` (`spectrum_id`),
  CONSTRAINT `compound_ibfk_1` FOREIGN KEY (`measurement_id`) REFERENCES `measurement` (`id`),
  CONSTRAINT `compound_ibfk_2` FOREIGN KEY (`spectrum_id`) REFERENCES `spectrum` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compound`
--

LOCK TABLES `compound` WRITE;
/*!40000 ALTER TABLE `compound` DISABLE KEYS */;
/*!40000 ALTER TABLE `compound` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnosis`
--

DROP TABLE IF EXISTS `diagnosis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagnosis` (
  `experiment_id` int(255) DEFAULT NULL,
  `pneumonia` tinyint(1) DEFAULT NULL,
  `vap` tinyint(1) DEFAULT NULL,
  `covid19` tinyint(1) DEFAULT NULL,
  KEY `experiment_id` (`experiment_id`),
  CONSTRAINT `diagnosis_ibfk_1` FOREIGN KEY (`experiment_id`) REFERENCES `experiment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnosis`
--

LOCK TABLES `diagnosis` WRITE;
/*!40000 ALTER TABLE `diagnosis` DISABLE KEYS */;
/*!40000 ALTER TABLE `diagnosis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `era`
--

DROP TABLE IF EXISTS `era`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `era` (
  `id` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `date_start` date DEFAULT NULL,
  `date_end` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `era`
--

LOCK TABLES `era` WRITE;
/*!40000 ALTER TABLE `era` DISABLE KEYS */;
/*!40000 ALTER TABLE `era` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiment`
--

DROP TABLE IF EXISTS `experiment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiment` (
  `id` int(255) NOT NULL,
  `label` varchar(255) DEFAULT NULL,
  `measurement_1` int(255) DEFAULT NULL,
  `measurement_2` int(255) DEFAULT NULL,
  `reader_id` int(255) DEFAULT NULL,
  `ventilator_id` int(255) DEFAULT NULL,
  `bed_id` varchar(255) DEFAULT NULL,
  `room_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `label` (`label`),
  KEY `measurement_1` (`measurement_1`),
  KEY `measurement_2` (`measurement_2`),
  CONSTRAINT `experiment_ibfk_1` FOREIGN KEY (`label`) REFERENCES `patientculture` (`experiment_label`),
  CONSTRAINT `experiment_ibfk_2` FOREIGN KEY (`measurement_1`) REFERENCES `invivomeasurement` (`id`),
  CONSTRAINT `experiment_ibfk_3` FOREIGN KEY (`measurement_2`) REFERENCES `invivomeasurement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiment`
--

LOCK TABLES `experiment` WRITE;
/*!40000 ALTER TABLE `experiment` DISABLE KEYS */;
/*!40000 ALTER TABLE `experiment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experimenttype`
--

DROP TABLE IF EXISTS `experimenttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experimenttype` (
  `id` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experimenttype`
--

LOCK TABLES `experimenttype` WRITE;
/*!40000 ALTER TABLE `experimenttype` DISABLE KEYS */;
/*!40000 ALTER TABLE `experimenttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `functionalgroup`
--

DROP TABLE IF EXISTS `functionalgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `functionalgroup` (
  `id` int(255) NOT NULL,
  `group_id` int(255) DEFAULT NULL,
  `prefix` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `functionalgroup_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `functionalgroupref` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `functionalgroup`
--

LOCK TABLES `functionalgroup` WRITE;
/*!40000 ALTER TABLE `functionalgroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `functionalgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `functionalgroupref`
--

DROP TABLE IF EXISTS `functionalgroupref`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `functionalgroupref` (
  `id` int(255) NOT NULL,
  `group` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `functionalgroupref`
--

LOCK TABLES `functionalgroupref` WRITE;
/*!40000 ALTER TABLE `functionalgroupref` DISABLE KEYS */;
/*!40000 ALTER TABLE `functionalgroupref` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incubator`
--

DROP TABLE IF EXISTS `incubator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incubator` (
  `id` int(255) NOT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `usage` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incubator`
--

LOCK TABLES `incubator` WRITE;
/*!40000 ALTER TABLE `incubator` DISABLE KEYS */;
/*!40000 ALTER TABLE `incubator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution`
--

DROP TABLE IF EXISTS `institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institution` (
  `id` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution`
--

LOCK TABLES `institution` WRITE;
/*!40000 ALTER TABLE `institution` DISABLE KEYS */;
/*!40000 ALTER TABLE `institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `internalstandard`
--

DROP TABLE IF EXISTS `internalstandard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `internalstandard` (
  `id` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `analyzer_id` int(255) DEFAULT NULL,
  `retention_time` float DEFAULT NULL,
  `retention_time_stdev` float DEFAULT NULL,
  `cas_rn` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `analyzer_id` (`analyzer_id`),
  CONSTRAINT `internalstandard_ibfk_1` FOREIGN KEY (`analyzer_id`) REFERENCES `analyzer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `internalstandard`
--

LOCK TABLES `internalstandard` WRITE;
/*!40000 ALTER TABLE `internalstandard` DISABLE KEYS */;
/*!40000 ALTER TABLE `internalstandard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `internalstandardsset`
--

DROP TABLE IF EXISTS `internalstandardsset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `internalstandardsset` (
  `id` int(255) NOT NULL,
  `internal_standard_id` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `internal_standard_id` (`internal_standard_id`),
  CONSTRAINT `internalstandardsset_ibfk_1` FOREIGN KEY (`internal_standard_id`) REFERENCES `internalstandard` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `internalstandardsset`
--

LOCK TABLES `internalstandardsset` WRITE;
/*!40000 ALTER TABLE `internalstandardsset` DISABLE KEYS */;
/*!40000 ALTER TABLE `internalstandardsset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invitromeasurement`
--

DROP TABLE IF EXISTS `invitromeasurement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invitromeasurement` (
  `id` int(255) NOT NULL,
  `td_tube_sn` varchar(255) DEFAULT NULL,
  `measurement_id` int(255) DEFAULT NULL,
  `set_number` int(255) DEFAULT NULL,
  `sample_number` int(255) DEFAULT NULL,
  `rep_number` int(255) DEFAULT '0',
  `control` tinyint(1) DEFAULT NULL,
  `time_incubation_start` timestamp NULL DEFAULT NULL,
  `time_incubation_end` timestamp NULL DEFAULT NULL,
  `time_collection_start` timestamp NULL DEFAULT NULL,
  `time_collection_end` timestamp NULL DEFAULT NULL,
  `experiment_type` int(255) DEFAULT NULL,
  `plate_number` int(255) DEFAULT NULL,
  `flow_reg` float DEFAULT NULL,
  `accumulative` tinyint(1) DEFAULT NULL,
  `bacteria_set` int(255) DEFAULT NULL,
  `co2_percent` float DEFAULT NULL,
  `incubator_id` int(255) DEFAULT NULL,
  `medium_id` int(255) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `td_tube_sn` (`td_tube_sn`),
  KEY `measurement_id` (`measurement_id`),
  KEY `experiment_type` (`experiment_type`),
  KEY `bacteria_set` (`bacteria_set`),
  KEY `incubator_id` (`incubator_id`),
  KEY `medium_id` (`medium_id`),
  CONSTRAINT `invitromeasurement_ibfk_1` FOREIGN KEY (`td_tube_sn`) REFERENCES `tdtube` (`id`),
  CONSTRAINT `invitromeasurement_ibfk_2` FOREIGN KEY (`measurement_id`) REFERENCES `measurement` (`id`),
  CONSTRAINT `invitromeasurement_ibfk_3` FOREIGN KEY (`experiment_type`) REFERENCES `experimenttype` (`id`),
  CONSTRAINT `invitromeasurement_ibfk_4` FOREIGN KEY (`bacteria_set`) REFERENCES `bacteriaset` (`id`),
  CONSTRAINT `invitromeasurement_ibfk_5` FOREIGN KEY (`incubator_id`) REFERENCES `incubator` (`id`),
  CONSTRAINT `invitromeasurement_ibfk_6` FOREIGN KEY (`medium_id`) REFERENCES `medium` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invitromeasurement`
--

LOCK TABLES `invitromeasurement` WRITE;
/*!40000 ALTER TABLE `invitromeasurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `invitromeasurement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invivomeasurement`
--

DROP TABLE IF EXISTS `invivomeasurement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invivomeasurement` (
  `id` int(255) NOT NULL,
  `measurement_id` int(255) DEFAULT NULL,
  `td_tube_sn` varchar(255) DEFAULT NULL,
  `time_collection_start` timestamp NULL DEFAULT NULL,
  `time_collection_end` timestamp NULL DEFAULT NULL,
  `vent_tube_number` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `measurement_id` (`measurement_id`),
  KEY `td_tube_sn` (`td_tube_sn`),
  CONSTRAINT `invivomeasurement_ibfk_1` FOREIGN KEY (`measurement_id`) REFERENCES `measurement` (`id`),
  CONSTRAINT `invivomeasurement_ibfk_2` FOREIGN KEY (`td_tube_sn`) REFERENCES `tdtube` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invivomeasurement`
--

LOCK TABLES `invivomeasurement` WRITE;
/*!40000 ALTER TABLE `invivomeasurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `invivomeasurement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `measurement`
--

DROP TABLE IF EXISTS `measurement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `measurement` (
  `id` int(255) NOT NULL,
  `type_id` int(255) DEFAULT NULL,
  `era_id` int(255) DEFAULT NULL,
  `time_analysis` timestamp NULL DEFAULT NULL,
  `internal_standards_set_id` int(255) DEFAULT NULL,
  `analyzer_id` int(255) DEFAULT NULL,
  `injection_pos` int(255) DEFAULT NULL,
  `chromatogram` varchar(255) DEFAULT NULL,
  `cef` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `type_id` (`type_id`),
  KEY `era_id` (`era_id`),
  KEY `internal_standards_set_id` (`internal_standards_set_id`),
  KEY `analyzer_id` (`analyzer_id`),
  CONSTRAINT `measurement_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `measurementtype` (`id`),
  CONSTRAINT `measurement_ibfk_2` FOREIGN KEY (`era_id`) REFERENCES `era` (`id`),
  CONSTRAINT `measurement_ibfk_3` FOREIGN KEY (`internal_standards_set_id`) REFERENCES `internalstandardsset` (`id`),
  CONSTRAINT `measurement_ibfk_4` FOREIGN KEY (`analyzer_id`) REFERENCES `analyzer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `measurement`
--

LOCK TABLES `measurement` WRITE;
/*!40000 ALTER TABLE `measurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `measurement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `measurementtype`
--

DROP TABLE IF EXISTS `measurementtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `measurementtype` (
  `id` int(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `measurementtype`
--

LOCK TABLES `measurementtype` WRITE;
/*!40000 ALTER TABLE `measurementtype` DISABLE KEYS */;
/*!40000 ALTER TABLE `measurementtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medium`
--

DROP TABLE IF EXISTS `medium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medium` (
  `id` int(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medium`
--

LOCK TABLES `medium` WRITE;
/*!40000 ALTER TABLE `medium` DISABLE KEYS */;
/*!40000 ALTER TABLE `medium` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `molecule`
--

DROP TABLE IF EXISTS `molecule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `molecule` (
  `id` int(255) NOT NULL,
  `cas_rn` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `formula` varchar(255) DEFAULT NULL,
  `type_id` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`,`cas_rn`),
  KEY `type_id` (`type_id`),
  CONSTRAINT `molecule_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `moleculetype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `molecule`
--

LOCK TABLES `molecule` WRITE;
/*!40000 ALTER TABLE `molecule` DISABLE KEYS */;
/*!40000 ALTER TABLE `molecule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moleculebacteria`
--

DROP TABLE IF EXISTS `moleculebacteria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moleculebacteria` (
  `match_id` int(255) DEFAULT NULL,
  `bacteria_id` int(255) DEFAULT NULL,
  `retention_time_average` float DEFAULT NULL,
  `area_average` float DEFAULT NULL,
  `height_average` float DEFAULT NULL,
  `rrt1` float DEFAULT NULL,
  `rrt2` float DEFAULT NULL,
  `rrt3` float DEFAULT NULL,
  `rrt4` float DEFAULT NULL,
  KEY `match_id` (`match_id`),
  KEY `bacteria_id` (`bacteria_id`),
  CONSTRAINT `moleculebacteria_ibfk_1` FOREIGN KEY (`match_id`) REFERENCES `algorithmmatch` (`id`),
  CONSTRAINT `moleculebacteria_ibfk_2` FOREIGN KEY (`bacteria_id`) REFERENCES `bacteria` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moleculebacteria`
--

LOCK TABLES `moleculebacteria` WRITE;
/*!40000 ALTER TABLE `moleculebacteria` DISABLE KEYS */;
/*!40000 ALTER TABLE `moleculebacteria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moleculetype`
--

DROP TABLE IF EXISTS `moleculetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moleculetype` (
  `id` int(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moleculetype`
--

LOCK TABLES `moleculetype` WRITE;
/*!40000 ALTER TABLE `moleculetype` DISABLE KEYS */;
/*!40000 ALTER TABLE `moleculetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientculture`
--

DROP TABLE IF EXISTS `patientculture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patientculture` (
  `experiment_label` varchar(255) NOT NULL,
  `invitro_measurement_id` int(255) DEFAULT NULL,
  `source_id` int(255) DEFAULT NULL,
  PRIMARY KEY (`experiment_label`),
  KEY `invitro_measurement_id` (`invitro_measurement_id`),
  KEY `source_id` (`source_id`),
  CONSTRAINT `patientculture_ibfk_1` FOREIGN KEY (`invitro_measurement_id`) REFERENCES `invitromeasurement` (`id`),
  CONSTRAINT `patientculture_ibfk_2` FOREIGN KEY (`source_id`) REFERENCES `patientculturesource` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientculture`
--

LOCK TABLES `patientculture` WRITE;
/*!40000 ALTER TABLE `patientculture` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientculture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientculturesource`
--

DROP TABLE IF EXISTS `patientculturesource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patientculturesource` (
  `id` int(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientculturesource`
--

LOCK TABLES `patientculturesource` WRITE;
/*!40000 ALTER TABLE `patientculturesource` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientculturesource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientemrdata`
--

DROP TABLE IF EXISTS `patientemrdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patientemrdata` (
  `patient_id_barcode` int(255) NOT NULL,
  `age_years` int(255) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `weight_kg` int(255) DEFAULT NULL,
  `stuff1` varchar(255) DEFAULT NULL,
  `stuff2` varchar(255) DEFAULT NULL,
  `stuff3` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`patient_id_barcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientemrdata`
--

LOCK TABLES `patientemrdata` WRITE;
/*!40000 ALTER TABLE `patientemrdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientemrdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientreference`
--

DROP TABLE IF EXISTS `patientreference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patientreference` (
  `rs_id` varchar(255) NOT NULL,
  `patient_id` int(255) DEFAULT NULL,
  `institution_id` int(255) DEFAULT NULL,
  PRIMARY KEY (`rs_id`),
  KEY `patient_id` (`patient_id`),
  KEY `institution_id` (`institution_id`),
  CONSTRAINT `patientreference_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patientemrdata` (`patient_id_barcode`),
  CONSTRAINT `patientreference_ibfk_2` FOREIGN KEY (`institution_id`) REFERENCES `institution` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientreference`
--

LOCK TABLES `patientreference` WRITE;
/*!40000 ALTER TABLE `patientreference` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientreference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spectrum`
--

DROP TABLE IF EXISTS `spectrum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spectrum` (
  `id` int(255) NOT NULL,
  `x` json DEFAULT NULL,
  `y` json DEFAULT NULL,
  `z` json DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spectrum`
--

LOCK TABLES `spectrum` WRITE;
/*!40000 ALTER TABLE `spectrum` DISABLE KEYS */;
/*!40000 ALTER TABLE `spectrum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tdtube`
--

DROP TABLE IF EXISTS `tdtube`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tdtube` (
  `id` varchar(255) NOT NULL,
  `type_id` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `type_id` (`type_id`),
  CONSTRAINT `tdtube_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `tdtubetype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tdtube`
--

LOCK TABLES `tdtube` WRITE;
/*!40000 ALTER TABLE `tdtube` DISABLE KEYS */;
/*!40000 ALTER TABLE `tdtube` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tdtubetype`
--

DROP TABLE IF EXISTS `tdtubetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tdtubetype` (
  `id` int(255) NOT NULL,
  `manufacturer` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tdtubetype`
--

LOCK TABLES `tdtubetype` WRITE;
/*!40000 ALTER TABLE `tdtubetype` DISABLE KEYS */;
/*!40000 ALTER TABLE `tdtubetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visit`
--

DROP TABLE IF EXISTS `visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit` (
  `id` int(255) NOT NULL,
  `experiment_id` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `experiment_id` (`experiment_id`),
  CONSTRAINT `visit_ibfk_1` FOREIGN KEY (`experiment_id`) REFERENCES `experiment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit`
--

LOCK TABLES `visit` WRITE;
/*!40000 ALTER TABLE `visit` DISABLE KEYS */;
/*!40000 ALTER TABLE `visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visithistory`
--

DROP TABLE IF EXISTS `visithistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visithistory` (
  `rs_id` varchar(255) DEFAULT NULL,
  `visit_id` int(255) DEFAULT NULL,
  KEY `rs_id` (`rs_id`),
  KEY `visit_id` (`visit_id`),
  CONSTRAINT `visithistory_ibfk_1` FOREIGN KEY (`rs_id`) REFERENCES `patientreference` (`rs_id`),
  CONSTRAINT `visithistory_ibfk_2` FOREIGN KEY (`visit_id`) REFERENCES `visit` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visithistory`
--

LOCK TABLES `visithistory` WRITE;
/*!40000 ALTER TABLE `visithistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `visithistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-24 21:27:13
