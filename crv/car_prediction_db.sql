-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2023 at 12:11 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_prediction_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `carsaletable`
--

CREATE TABLE `carsaletable` (
  `srno` int(10) NOT NULL,
  `year` int(10) NOT NULL,
  `showroom_price` float(10,2) NOT NULL,
  `km_drived` bigint(20) NOT NULL,
  `previous_owner` int(10) NOT NULL,
  `fuel_type` varchar(100) NOT NULL,
  `seller_type` varchar(100) NOT NULL,
  `transmission` varchar(100) NOT NULL,
  `price` float(10,2) NOT NULL,
  `sold_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `carsaletable`
--

INSERT INTO `carsaletable` (`srno`, `year`, `showroom_price`, `km_drived`, `previous_owner`, `fuel_type`, `seller_type`, `transmission`, `price`, `sold_on`) VALUES
(2, 2015, 5.00, 5000, 0, 'Petrol', 'Dealer', 'Manual', 4.76, '2023-05-04'),
(3, 2015, 5.00, 50000, 0, 'Petrol', 'Individual', 'Manual', 1.73, '2023-05-04');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `carsaletable`
--
ALTER TABLE `carsaletable`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `carsaletable`
--
ALTER TABLE `carsaletable`
  MODIFY `srno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
