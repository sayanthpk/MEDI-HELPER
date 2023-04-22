/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - diabetes_prediction
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`diabetes_prediction` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `diabetes_prediction`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add doctor',7,'add_doctor'),(26,'Can change doctor',7,'change_doctor'),(27,'Can delete doctor',7,'delete_doctor'),(28,'Can view doctor',7,'view_doctor'),(29,'Can add login',8,'add_login'),(30,'Can change login',8,'change_login'),(31,'Can delete login',8,'delete_login'),(32,'Can view login',8,'view_login'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add schedule',10,'add_schedule'),(38,'Can change schedule',10,'change_schedule'),(39,'Can delete schedule',10,'delete_schedule'),(40,'Can view schedule',10,'view_schedule'),(41,'Can add rating',11,'add_rating'),(42,'Can change rating',11,'change_rating'),(43,'Can delete rating',11,'delete_rating'),(44,'Can view rating',11,'view_rating'),(45,'Can add complaints',12,'add_complaints'),(46,'Can change complaints',12,'change_complaints'),(47,'Can delete complaints',12,'delete_complaints'),(48,'Can view complaints',12,'view_complaints'),(49,'Can add chat',13,'add_chat'),(50,'Can change chat',13,'change_chat'),(51,'Can delete chat',13,'delete_chat'),(52,'Can view chat',13,'view_chat'),(53,'Can add booking',14,'add_booking'),(54,'Can change booking',14,'change_booking'),(55,'Can delete booking',14,'delete_booking'),(56,'Can view booking',14,'view_booking');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `diabetes_moule_booking` */

DROP TABLE IF EXISTS `diabetes_moule_booking`;

CREATE TABLE `diabetes_moule_booking` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(20) NOT NULL,
  `tocken_no` int(11) NOT NULL,
  `schedule_id_id` bigint(20) NOT NULL,
  `userid_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `diabetes_moule_booki_schedule_id_id_29f03414_fk_diabetes_` (`schedule_id_id`),
  KEY `diabetes_moule_booki_userid_id_95c5be2a_fk_diabetes_` (`userid_id`),
  CONSTRAINT `diabetes_moule_booki_userid_id_95c5be2a_fk_diabetes_` FOREIGN KEY (`userid_id`) REFERENCES `diabetes_moule_user` (`id`),
  CONSTRAINT `diabetes_moule_booki_schedule_id_id_29f03414_fk_diabetes_` FOREIGN KEY (`schedule_id_id`) REFERENCES `diabetes_moule_schedule` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `diabetes_moule_booking` */

insert  into `diabetes_moule_booking`(`id`,`date`,`tocken_no`,`schedule_id_id`,`userid_id`) values (1,'2023-01-02',1,1,2),(2,'2023-01-14',1,1,1),(3,'2023-01-19',1,1,2);

/*Table structure for table `diabetes_moule_chat` */

DROP TABLE IF EXISTS `diabetes_moule_chat`;

CREATE TABLE `diabetes_moule_chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `message` varchar(20) NOT NULL,
  `doctor_id_id` bigint(20) NOT NULL,
  `user_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `diabetes_moule_chat_doctor_id_id_7cf27b06_fk_diabetes_` (`doctor_id_id`),
  KEY `diabetes_moule_chat_user_id_id_11f79166_fk_diabetes_` (`user_id_id`),
  CONSTRAINT `diabetes_moule_chat_user_id_id_11f79166_fk_diabetes_` FOREIGN KEY (`user_id_id`) REFERENCES `diabetes_moule_user` (`id`),
  CONSTRAINT `diabetes_moule_chat_doctor_id_id_7cf27b06_fk_diabetes_` FOREIGN KEY (`doctor_id_id`) REFERENCES `diabetes_moule_doctor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `diabetes_moule_chat` */

insert  into `diabetes_moule_chat`(`id`,`date`,`type`,`message`,`doctor_id_id`,`user_id_id`) values (1,'2023-01-14','user','hi',1,1),(2,'2023-01-14','user','hi',1,1),(3,'2023-01-14','user','hi',1,1),(4,'2023-01-14','doctor','helo',1,1),(5,'2023-01-14','user','hello',1,1),(6,'2023-01-18','doctor','qwsxcv',1,2),(7,'2023-01-18','doctor','dsfsdfsad',1,2),(8,'2023-01-19','user','heloo',1,2),(9,'2023-01-19','user','hey',1,2),(10,'2023-01-19','doctor','helo',1,2),(11,'2023-01-19','doctor','gd evng',1,2),(12,'2023-01-19','doctor','hiiii',1,2);

/*Table structure for table `diabetes_moule_complaints` */

DROP TABLE IF EXISTS `diabetes_moule_complaints`;

CREATE TABLE `diabetes_moule_complaints` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaints` varchar(20) NOT NULL,
  `complaint_date` varchar(200) NOT NULL,
  `reply` varchar(20) NOT NULL,
  `reply_date` varchar(20) NOT NULL,
  `userid_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `diabetes_moule_compl_userid_id_21fcd1b5_fk_diabetes_` (`userid_id`),
  CONSTRAINT `diabetes_moule_compl_userid_id_21fcd1b5_fk_diabetes_` FOREIGN KEY (`userid_id`) REFERENCES `diabetes_moule_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `diabetes_moule_complaints` */

insert  into `diabetes_moule_complaints`(`id`,`complaints`,`complaint_date`,`reply`,`reply_date`,`userid_id`) values (1,'tss','2023-01-14','pending','pending',1);

/*Table structure for table `diabetes_moule_doctor` */

DROP TABLE IF EXISTS `diabetes_moule_doctor`;

CREATE TABLE `diabetes_moule_doctor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `doctorname` varchar(20) NOT NULL,
  `doctorplace` varchar(20) NOT NULL,
  `doctorpost` varchar(20) NOT NULL,
  `doctorpin` int(11) NOT NULL,
  `email` varchar(20) NOT NULL,
  `pho_no` bigint(20) NOT NULL,
  `qualification` varchar(30) NOT NULL,
  `category` varchar(30) NOT NULL,
  `doctorid_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `diabetes_moule_docto_doctorid_id_a28d3701_fk_diabetes_` (`doctorid_id`),
  CONSTRAINT `diabetes_moule_docto_doctorid_id_a28d3701_fk_diabetes_` FOREIGN KEY (`doctorid_id`) REFERENCES `diabetes_moule_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `diabetes_moule_doctor` */

insert  into `diabetes_moule_doctor`(`id`,`doctorname`,`doctorplace`,`doctorpost`,`doctorpin`,`email`,`pho_no`,`qualification`,`category`,`doctorid_id`) values (1,'dn','pl','po',0,'e',0,'q','c',1);

/*Table structure for table `diabetes_moule_login` */

DROP TABLE IF EXISTS `diabetes_moule_login`;

CREATE TABLE `diabetes_moule_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `diabetes_moule_login` */

insert  into `diabetes_moule_login`(`id`,`username`,`password`,`usertype`) values (1,'d','d','doctor'),(2,'@gmail.com','s','user'),(3,'ak@gmail.com','ak','user'),(4,'admin','admin','admin');

/*Table structure for table `diabetes_moule_rating` */

DROP TABLE IF EXISTS `diabetes_moule_rating`;

CREATE TABLE `diabetes_moule_rating` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rating` varchar(30) NOT NULL,
  `doctorid_id` bigint(20) NOT NULL,
  `userid_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `diabetes_moule_ratin_doctorid_id_78b68885_fk_diabetes_` (`doctorid_id`),
  KEY `diabetes_moule_ratin_userid_id_a5937399_fk_diabetes_` (`userid_id`),
  CONSTRAINT `diabetes_moule_ratin_userid_id_a5937399_fk_diabetes_` FOREIGN KEY (`userid_id`) REFERENCES `diabetes_moule_login` (`id`),
  CONSTRAINT `diabetes_moule_ratin_doctorid_id_78b68885_fk_diabetes_` FOREIGN KEY (`doctorid_id`) REFERENCES `diabetes_moule_doctor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `diabetes_moule_rating` */

/*Table structure for table `diabetes_moule_schedule` */

DROP TABLE IF EXISTS `diabetes_moule_schedule`;

CREATE TABLE `diabetes_moule_schedule` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tocken_count` int(11) NOT NULL,
  `schedulingtime` time(6) NOT NULL,
  `schedulingdate` date NOT NULL,
  `doctorid_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `diabetes_moule_sched_doctorid_id_a615a9b3_fk_diabetes_` (`doctorid_id`),
  CONSTRAINT `diabetes_moule_sched_doctorid_id_a615a9b3_fk_diabetes_` FOREIGN KEY (`doctorid_id`) REFERENCES `diabetes_moule_doctor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `diabetes_moule_schedule` */

insert  into `diabetes_moule_schedule`(`id`,`tocken_count`,`schedulingtime`,`schedulingdate`,`doctorid_id`) values (1,10,'01:00:00.000000','2022-09-08',1);

/*Table structure for table `diabetes_moule_user` */

DROP TABLE IF EXISTS `diabetes_moule_user`;

CREATE TABLE `diabetes_moule_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `height` varchar(20) NOT NULL,
  `weight` varchar(20) NOT NULL,
  `age` varchar(20) NOT NULL,
  `userid_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `diabetes_moule_user_userid_id_b47acfbf_fk_diabetes_` (`userid_id`),
  CONSTRAINT `diabetes_moule_user_userid_id_b47acfbf_fk_diabetes_` FOREIGN KEY (`userid_id`) REFERENCES `diabetes_moule_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `diabetes_moule_user` */

insert  into `diabetes_moule_user`(`id`,`username`,`place`,`phone`,`email`,`height`,`weight`,`age`,`userid_id`) values (1,'aa','knr',7945389486,'@gmail.com','165','55','21',2),(2,'ak','az',46795679795,'ak@gmail.com','165','56','20',3);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(14,'diabetes_moule','booking'),(13,'diabetes_moule','chat'),(12,'diabetes_moule','complaints'),(7,'diabetes_moule','doctor'),(8,'diabetes_moule','login'),(11,'diabetes_moule','rating'),(10,'diabetes_moule','schedule'),(9,'diabetes_moule','user'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-01-02 06:14:31.684580'),(2,'auth','0001_initial','2023-01-02 06:14:32.045083'),(3,'admin','0001_initial','2023-01-02 06:14:32.130804'),(4,'admin','0002_logentry_remove_auto_add','2023-01-02 06:14:32.134199'),(5,'admin','0003_logentry_add_action_flag_choices','2023-01-02 06:14:32.144906'),(6,'contenttypes','0002_remove_content_type_name','2023-01-02 06:14:32.222720'),(7,'auth','0002_alter_permission_name_max_length','2023-01-02 06:14:32.258604'),(8,'auth','0003_alter_user_email_max_length','2023-01-02 06:14:32.295622'),(9,'auth','0004_alter_user_username_opts','2023-01-02 06:14:32.298786'),(10,'auth','0005_alter_user_last_login_null','2023-01-02 06:14:32.348982'),(11,'auth','0006_require_contenttypes_0002','2023-01-02 06:14:32.353099'),(12,'auth','0007_alter_validators_add_error_messages','2023-01-02 06:14:32.363570'),(13,'auth','0008_alter_user_username_max_length','2023-01-02 06:14:32.397728'),(14,'auth','0009_alter_user_last_name_max_length','2023-01-02 06:14:32.433465'),(15,'auth','0010_alter_group_name_max_length','2023-01-02 06:14:32.469606'),(16,'auth','0011_update_proxy_permissions','2023-01-02 06:14:32.481095'),(17,'auth','0012_alter_user_first_name_max_length','2023-01-02 06:14:32.515664'),(18,'diabetes_moule','0001_initial','2023-01-02 06:14:32.986059'),(19,'sessions','0001_initial','2023-01-02 06:14:33.020760');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('glkx33uw1n9da1c3xu4fysuzdwo4690n','eyJsaWQiOjF9:1pI4Vw:kXsSlBowhfKhFfvnDjJz4JkhSylZMsqTkol4ZebDA38','2023-02-01 09:13:48.396440'),('hvkcymguj4iktwrhd30fsbalqobvu561','eyJsaWQiOjF9:1pIRfI:-igkmvqcWCQgC6aBeB1qPmpGuue-PZ8z02ffy00Oc_o','2023-02-02 09:57:00.121699');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
