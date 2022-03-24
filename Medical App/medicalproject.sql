-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 05, 2020 at 03:58 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medicalproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `profile_user`
--

DROP TABLE IF EXISTS `profile_user`;
CREATE TABLE IF NOT EXISTS `profile_user` (
  `username` varchar(32) NOT NULL,
  `firstname` varchar(32) DEFAULT NULL,
  `lastname` varchar(32) DEFAULT NULL,
  `gender` varchar(32) DEFAULT NULL,
  `date_of_birth` longtext DEFAULT NULL,
  `job` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profile_user`
--

INSERT INTO `profile_user` (`username`, `firstname`, `lastname`, `gender`, `date_of_birth`, `job`) VALUES
('user', 'trang', 'minh', 'Male', '16/9/1999', 'student'),
('doctor', NULL, NULL, NULL, NULL, NULL),
('admin', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
CREATE TABLE IF NOT EXISTS `requests` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `phone_number` varchar(16) NOT NULL,
  `title` varchar(64) NOT NULL,
  `description` varchar(255) NOT NULL,
  `status` varchar(64) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `requests`
--

INSERT INTO `requests` (`ID`, `username`, `phone_number`, `title`, `description`, `status`) VALUES
(4, 'user', '1', '1', '1', 'Pending'),
(3, 'user', '12321321', 'dasdsad', 'dsadas', 'Pending'),
(5, 'user', '1234', 'hi', 'hello', 'Pending'),
(6, 'user', '4321', 'Hello', 'Xin chao', 'Pending'),
(7, 'user', '7653', 'Chao mung', 'Can I have a question', 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `pwd` text NOT NULL,
  `email` varchar(255) NOT NULL,
  `role` int(11) NOT NULL DEFAULT 0,
  `verified` int(11) NOT NULL DEFAULT 0,
  `status` int(11) NOT NULL DEFAULT 1,
  `reason` longtext DEFAULT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `pwd`, `email`, `role`, `verified`, `status`, `reason`, `date_created`) VALUES
(1, 'admin', 'admin', 'admin', 2, 0, 0, NULL, '2020-09-11 15:46:50'),
(2, 'doctor', 'doctor', 'doctor', 1, 0, 0, NULL, '2020-09-15 20:45:27'),
(3, 'user', 'user', 'user', 0, 0, 0, '', '2020-09-15 20:56:19');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
