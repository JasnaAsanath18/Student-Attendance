/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.22-MariaDB : Database - ekm_student_attendance
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ekm_student_attendance` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `ekm_student_attendance`;

/*Table structure for table `assign_teacher` */

DROP TABLE IF EXISTS `assign_teacher`;

CREATE TABLE `assign_teacher` (
  `assigntchr_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`assigntchr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `assign_teacher` */

insert  into `assign_teacher`(`assigntchr_id`,`teacher_id`,`subject_id`) values (1,1,2),(2,1,1),(3,2,2);

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`student_id`,`teacher_id`,`status`,`date`,`time`) values (1,1,1,'present','11/2/23','11.03'),(2,1,2,'present','2023-03-01','2023-03-01 17:00:25'),(9,1,2,'present','2023-03-15','2023-03-13 17:13:08'),(10,1,2,'leave','2023-03-14','2023-03-14 09:32:40'),(11,1,2,'leave','2023-03-16','2023-03-14 09:34:40'),(12,1,2,'leave','2023-03-13','2023-03-14 09:35:37'),(13,1,2,'leave','2023-03-09','2023-03-14 09:36:16'),(14,1,2,'leave','2023-03-01','2023-03-14 09:38:19'),(15,1,2,'leave','2023-03-02','2023-03-14 09:39:15');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `chat` */

/*Table structure for table `chats` */

DROP TABLE IF EXISTS `chats`;

CREATE TABLE `chats` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `sender_type` varchar(50) DEFAULT NULL,
  `reciever_id` int(11) DEFAULT NULL,
  `reciever_type` varchar(50) DEFAULT NULL,
  `messages` varchar(50) DEFAULT NULL,
  `date_time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

/*Data for the table `chats` */

insert  into `chats`(`chat_id`,`sender_id`,`sender_type`,`reciever_id`,`reciever_type`,`messages`,`date_time`) values (1,10,'doctor',2,'patient','wdwf','2023-03-15 13:19:45'),(2,10,'teacher',12,'parent','qqqqqqqqqqqqqqqqqqqqqqqq','2023-03-15 13:27:18'),(3,2,'student',1,'teacher','shhssn','2023-03-15'),(4,2,'student',1,'teacher','hsjsns','2023-03-15'),(5,2,'student',1,'teacher','gdns','2023-03-15'),(6,2,'student',1,'teacher','gsjnz','2023-03-15'),(7,2,'student',1,'teacher','hdn','2023-03-15'),(8,12,'parent',0,'teacher','bdusns','2023-03-15'),(9,3,'teacher',2,'student','hello jasna','2023-03-15 20:46:14'),(10,3,'teacher',24,'student','Hello Sheza','2023-03-15 20:55:53'),(11,3,'teacher',25,'parent','Hello Shibina','2023-03-15 20:56:15'),(12,2,'student',1,'teacher','hyy','2023-03-16'),(13,2,'student',2,'teacher','hiii from jasna','2023-03-16'),(14,4,'student',10,'teacher','helloo','2023-03-16'),(15,4,'student',10,'teacher','message from student jasna','2023-03-16'),(16,4,'student',10,'teacher','hellllllooooooooooo','2023-03-16'),(17,2,'student',10,'teacher','fr','2023-03-16'),(18,12,'parent',0,'teacher','message from parent of jasna','2023-03-16'),(19,10,'teacher',2,'student','message from teacher amrutha','2023-03-16 09:43:13'),(20,10,'teacher',12,'parent','message from teacher amrutha','2023-03-16 09:43:37');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  KEY `complaint_id` (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`student_id`,`complaint`,`reply`,`date`) values (1,1,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','xxxxxxxxxx','2022-11-18 08:54:35'),(2,2,'ccccccccccc','llllllllllll','2022-11-18 09:27:31'),(3,2,'qwertyuiop','asdfgh','2022-11-19 12:04:39');

/*Table structure for table `fee` */

DROP TABLE IF EXISTS `fee`;

CREATE TABLE `fee` (
  `fee_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(50) DEFAULT NULL,
  `fee` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `fee` */

insert  into `fee`(`fee_id`,`student_id`,`fee`,`amount`,`date`) values (1,0,'500',NULL,NULL),(2,1,'term','12345','2023-03-31'),(4,2,'semester','20000','2023-03-31');

/*Table structure for table `fee_notification` */

DROP TABLE IF EXISTS `fee_notification`;

CREATE TABLE `fee_notification` (
  `fee_not_id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `notification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fee_not_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `fee_notification` */

insert  into `fee_notification`(`fee_not_id`,`parent_id`,`notification`) values (1,1,'sdfghjkklkjhgf'),(2,3,'dsfedg'),(3,5,'sadsfsdew');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `location` */

insert  into `location`(`location_id`,`student_id`,`latitude`,`longitude`,`date`) values (1,1,'10.5155191','76.2180307','2023-03-12'),(2,2,NULL,NULL,'2023-03-10'),(3,5,NULL,NULL,'2023-03-15');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values (1,'admin','123','admin'),(2,'user1','123','student'),(3,'teacher1','123','teacher'),(4,'user2','123','student'),(5,'user4','123','student'),(10,'jessi','123','teacher'),(11,'staff','staff','staff'),(12,'parent','parent','parent'),(14,'zz','zz','parent'),(15,'ff','ff','parent'),(16,'bb','bb','parent'),(20,'nimal','123','teacher'),(21,'sd','dss','teacher'),(24,'sheza','123','student'),(25,'shibina','123','parent');

/*Table structure for table `marks` */

DROP TABLE IF EXISTS `marks`;

CREATE TABLE `marks` (
  `mark_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `mark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mark_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `marks` */

insert  into `marks`(`mark_id`,`teacher_id`,`student_id`,`subject_id`,`mark`) values (1,2,1,2,'56'),(2,1,1,2,'123');

/*Table structure for table `notes` */

DROP TABLE IF EXISTS `notes`;

CREATE TABLE `notes` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `note` varchar(200) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `notes` */

insert  into `notes`(`note_id`,`teacher_id`,`note`,`subject_id`) values (2,2,'C:/RISS PROJECTS D/EKM/Student Attendance/static/notes/online_car_rentall.pdf',1),(3,2,'static/notes/6eaa2739-bf8a-4b80-b759-277202dc0bdfinvoice (1).doc',1),(4,1,'static/notes/e5b3fa0d-4988-4e29-80ca-143f3d4c47baDjango.docx',2);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`notification`) values (1,'dsvdsdvds');

/*Table structure for table `parent` */

DROP TABLE IF EXISTS `parent`;

CREATE TABLE `parent` (
  `parent_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `p_fname` varchar(50) DEFAULT NULL,
  `p_lname` varchar(50) DEFAULT NULL,
  `p_place` varchar(50) DEFAULT NULL,
  `p_phone` varchar(50) DEFAULT NULL,
  `p_email` varchar(50) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `parent` */

insert  into `parent`(`parent_id`,`login_id`,`p_fname`,`p_lname`,`p_place`,`p_phone`,`p_email`,`student_id`) values (1,12,'jasnas parent','aaaaaaaaaaa','tyuiofksjnf','741852963','sdbcjs@fdh',1),(2,14,'we','gdb','rr','7485263','55.',0),(3,15,'qwr','df','eeee','52825353','5.8',0),(4,16,'er','sf','wwww','56365.365','.56',0),(10,25,'Shibina','Rasheed','tsr','0987654321','shibina@mail',5);

/*Table structure for table `parent_student` */

DROP TABLE IF EXISTS `parent_student`;

CREATE TABLE `parent_student` (
  `par_stu_id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`par_stu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `parent_student` */

insert  into `parent_student`(`par_stu_id`,`parent_id`,`student_id`) values (1,1,1);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `fee_id` int(11) DEFAULT NULL,
  `amt` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`pay_id`,`fee_id`,`amt`,`date`) values (1,2,'12345','12-3-2023'),(2,2,'12345','2023-03-15');

/*Table structure for table `questionpaper` */

DROP TABLE IF EXISTS `questionpaper`;

CREATE TABLE `questionpaper` (
  `qp_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `qp` varchar(300) DEFAULT NULL,
  `details` varchar(200) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`qp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `questionpaper` */

insert  into `questionpaper`(`qp_id`,`teacher_id`,`subject_id`,`qp`,`details`,`date`) values (1,0,0,NULL,NULL,NULL),(2,1,2,'static/ffed5c53-3da1-41a7-8ad5-ed5ea6d7d8f3invoice (2).doc','stgyhj','2023-03-02');

/*Table structure for table `sm` */

DROP TABLE IF EXISTS `sm`;

CREATE TABLE `sm` (
  `sm_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `sm` */

insert  into `sm`(`sm_id`,`teacher_id`,`subject_id`,`title`,`details`) values (1,1,2,'asd','bfdjgbkd');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values (1,11,'stafff','aaaaaaa','adegedg','8765432','dfgdxfd@dvsh');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `student` */

insert  into `student`(`student_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values (1,2,'jasna','jamal','aaaaaaaaa','6549461645','jasna@mail'),(2,4,'Anu','Anamika','qqqqqqq','1203654789','anu@mail'),(3,5,'niall','aaa','wqwertyuiop','9526970050','anu@mail'),(5,24,'Sheza','Mariyam','tsr','987654321','sheza@mail');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`subject`) values (1,'maths'),(2,'english'),(3,'Chemistry');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `designation` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`designation`,`qualification`) values (1,3,'Aasha','Rajeev','zzzzz','1236547890','asha@mail','teacher','b.ed'),(2,10,'amrutha','harish','asdfghjkl','123456789','dscsfcs@nbds','jdbcdsk','dvdsjbvjds'),(3,20,'nimal','a a','asd','963852741','nimal@mail','teacher','qesad'),(4,21,'ds','sd','dds','0657567575','4dfge@sfs','sedgv','sdgex');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
