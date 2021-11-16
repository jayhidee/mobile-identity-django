BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	bigint NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "organization_issuingorginization" (
	"id"	integer NOT NULL,
	"name"	varchar(255) NOT NULL,
	"api"	varchar(200) NOT NULL,
	"phone_number"	varchar(11) NOT NULL,
	"email"	varchar(255) NOT NULL,
	"address"	text NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "authtoken_token" (
	"key"	varchar(40) NOT NULL,
	"created"	datetime NOT NULL,
	"user_id"	bigint NOT NULL UNIQUE,
	FOREIGN KEY("user_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("key")
);
CREATE TABLE IF NOT EXISTS "logs_useraction" (
	"id"	integer NOT NULL,
	"time_stamp"	datetime NOT NULL,
	"action"	text NOT NULL,
	"user_id_id"	bigint NOT NULL,
	FOREIGN KEY("user_id_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cards_cards" (
	"id"	integer NOT NULL,
	"date_expiring"	date NOT NULL,
	"date_issued"	date NOT NULL,
	"verified"	bool NOT NULL,
	"issuing_organization_id"	bigint NOT NULL,
	"user_id_id"	bigint NOT NULL,
	"card_id"	varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("issuing_organization_id") REFERENCES "organization_issuingorginization"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "otp_tokens_useractivation" (
	"id"	integer NOT NULL,
	"otp"	varchar(20) NOT NULL,
	"date_used"	datetime,
	"valied"	bool NOT NULL,
	"user_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "mailing_service_tokenmailing" (
	"id"	integer NOT NULL,
	"email"	varchar(255) NOT NULL,
	"subject"	text NOT NULL,
	"message"	text NOT NULL,
	"sent"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "mailing_service_generalmail" (
	"id"	integer NOT NULL,
	"email"	varchar(255) NOT NULL,
	"subject"	text NOT NULL,
	"message"	text NOT NULL,
	"sent"	datetime NOT NULL,
	"sent_by_id"	bigint NOT NULL,
	FOREIGN KEY("sent_by_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "organization_issuingorginizationotp" (
	"id"	integer NOT NULL,
	"name"	varchar(255) NOT NULL,
	"api"	varchar(200) NOT NULL,
	"phone_number"	varchar(11) NOT NULL,
	"email"	varchar(255) NOT NULL,
	"address"	text NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cards_cardsotp" (
	"id"	integer NOT NULL,
	"card_id"	varchar(255) NOT NULL UNIQUE,
	"type"	varchar(10) NOT NULL,
	"first_name"	varchar(255) NOT NULL,
	"last_name"	varchar(255) NOT NULL,
	"from_date"	date NOT NULL,
	"to_date"	date NOT NULL,
	"email"	varchar(254) NOT NULL,
	"phone_number"	varchar(11) NOT NULL,
	"approved"	bool NOT NULL,
	"reason_for_visit"	text NOT NULL,
	"approved_by_id"	bigint,
	"issuing_organization_id"	bigint NOT NULL,
	"requested_by_id"	bigint NOT NULL,
	"date_approved"	date,
	FOREIGN KEY("issuing_organization_id") REFERENCES "organization_issuingorginizationotp"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("requested_by_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("approved_by_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "logs_cardslogs" (
	"id"	integer NOT NULL,
	"time_stamp"	datetime NOT NULL,
	"device"	varchar(100) NOT NULL,
	"action"	text NOT NULL,
	"device_ip"	char(39),
	"card_id"	bigint NOT NULL,
	"user_id_id"	bigint NOT NULL,
	"device_os"	varchar(100) NOT NULL,
	"uuid"	char(32),
	FOREIGN KEY("card_id") REFERENCES "cards_cards"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "logs_errorlogging" (
	"id"	integer NOT NULL,
	"code"	varchar(255) NOT NULL,
	"error_type"	varchar(255) NOT NULL,
	"error_details"	text NOT NULL,
	"time_field"	time NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "otp_tokens_cardtoken" (
	"id"	integer NOT NULL,
	"otp"	varchar(20) NOT NULL,
	"officer"	integer,
	"date_used"	datetime,
	"valied"	bool NOT NULL,
	"card_id_id"	bigint NOT NULL,
	"card_owner_id"	bigint NOT NULL,
	"date_issued"	datetime NOT NULL,
	"date_expiring"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("card_owner_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("card_id_id") REFERENCES "cards_cards"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "otp_tokens_cardverify" (
	"id"	integer NOT NULL,
	"otp"	varchar(20) NOT NULL,
	"date_used"	datetime,
	"valied"	bool NOT NULL,
	"card_id_id"	bigint NOT NULL,
	"card_owner_id"	bigint NOT NULL,
	"date_issued"	datetime NOT NULL,
	"date_expiring"	datetime NOT NULL,
	FOREIGN KEY("card_id_id") REFERENCES "cards_cards"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("card_owner_id") REFERENCES "user_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "user_user" (
	"id"	integer NOT NULL,
	"last_login"	datetime,
	"first_name"	varchar(40) NOT NULL,
	"last_name"	varchar(40) NOT NULL,
	"date_joined"	datetime NOT NULL,
	"email"	varchar(60) NOT NULL UNIQUE,
	"password"	varchar(244) NOT NULL,
	"admin"	bool NOT NULL,
	"confirm_email"	bool NOT NULL,
	"confirm_email_date"	datetime NOT NULL,
	"staff"	bool NOT NULL,
	"superuser"	bool NOT NULL,
	"active"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2021-10-06 22:47:54.736448');
INSERT INTO "django_migrations" VALUES (2,'contenttypes','0002_remove_content_type_name','2021-10-06 22:47:54.877436');
INSERT INTO "django_migrations" VALUES (3,'auth','0001_initial','2021-10-06 22:47:55.154141');
INSERT INTO "django_migrations" VALUES (4,'auth','0002_alter_permission_name_max_length','2021-10-06 22:47:55.263543');
INSERT INTO "django_migrations" VALUES (5,'auth','0003_alter_user_email_max_length','2021-10-06 22:47:55.386091');
INSERT INTO "django_migrations" VALUES (6,'auth','0004_alter_user_username_opts','2021-10-06 22:47:55.482209');
INSERT INTO "django_migrations" VALUES (7,'auth','0005_alter_user_last_login_null','2021-10-06 22:47:55.573966');
INSERT INTO "django_migrations" VALUES (8,'auth','0006_require_contenttypes_0002','2021-10-06 22:47:55.631808');
INSERT INTO "django_migrations" VALUES (9,'auth','0007_alter_validators_add_error_messages','2021-10-06 22:47:55.716148');
INSERT INTO "django_migrations" VALUES (10,'auth','0008_alter_user_username_max_length','2021-10-06 22:47:55.784007');
INSERT INTO "django_migrations" VALUES (11,'auth','0009_alter_user_last_name_max_length','2021-10-06 22:47:55.870321');
INSERT INTO "django_migrations" VALUES (12,'auth','0010_alter_group_name_max_length','2021-10-06 22:47:55.963606');
INSERT INTO "django_migrations" VALUES (13,'auth','0011_update_proxy_permissions','2021-10-06 22:47:56.081078');
INSERT INTO "django_migrations" VALUES (14,'auth','0012_alter_user_first_name_max_length','2021-10-06 22:47:56.195487');
INSERT INTO "django_migrations" VALUES (15,'user','0001_initial','2021-10-06 22:47:56.430839');
INSERT INTO "django_migrations" VALUES (16,'admin','0001_initial','2021-10-06 22:47:56.643408');
INSERT INTO "django_migrations" VALUES (17,'admin','0002_logentry_remove_auto_add','2021-10-06 22:47:56.762027');
INSERT INTO "django_migrations" VALUES (18,'admin','0003_logentry_add_action_flag_choices','2021-10-06 22:47:56.908601');
INSERT INTO "django_migrations" VALUES (19,'organization','0001_initial','2021-10-06 22:47:57.008181');
INSERT INTO "django_migrations" VALUES (20,'sessions','0001_initial','2021-10-06 22:47:57.257890');
INSERT INTO "django_migrations" VALUES (21,'authtoken','0001_initial','2021-10-06 22:51:11.849505');
INSERT INTO "django_migrations" VALUES (22,'authtoken','0002_auto_20160226_1747','2021-10-06 22:51:12.037188');
INSERT INTO "django_migrations" VALUES (23,'cards','0001_initial','2021-10-09 21:47:15.967319');
INSERT INTO "django_migrations" VALUES (24,'logs','0001_initial','2021-10-09 21:47:16.235062');
INSERT INTO "django_migrations" VALUES (25,'cards','0002_alter_cards_card_id','2021-10-20 22:59:10.700447');
INSERT INTO "django_migrations" VALUES (26,'otp_tokens','0001_initial','2021-10-20 22:59:11.302275');
INSERT INTO "django_migrations" VALUES (27,'otp_tokens','0002_alter_cardtoken_officer','2021-10-20 22:59:11.385782');
INSERT INTO "django_migrations" VALUES (28,'mailing_service','0001_initial','2021-10-21 19:43:25.535267');
INSERT INTO "django_migrations" VALUES (29,'organization','0002_issuingorginizationotp','2021-11-15 23:20:01.587985');
INSERT INTO "django_migrations" VALUES (30,'cards','0003_cardsotp','2021-11-15 23:20:01.937041');
INSERT INTO "django_migrations" VALUES (31,'cards','0004_alter_cardsotp_date_approved','2021-11-15 23:20:02.075748');
INSERT INTO "django_migrations" VALUES (32,'cards','0005_alter_cardsotp_options','2021-11-15 23:20:02.204618');
INSERT INTO "django_migrations" VALUES (33,'logs','0002_auto_20211030_0042','2021-11-15 23:20:02.377931');
INSERT INTO "django_migrations" VALUES (34,'logs','0003_errorlogging','2021-11-15 23:20:02.470130');
INSERT INTO "django_migrations" VALUES (35,'otp_tokens','0003_auto_20211028_1545','2021-11-15 23:20:02.698756');
INSERT INTO "django_migrations" VALUES (36,'otp_tokens','0004_auto_20211028_1927','2021-11-15 23:20:02.851324');
INSERT INTO "django_migrations" VALUES (37,'otp_tokens','0005_alter_cardtoken_date_expiring','2021-11-15 23:20:03.123664');
INSERT INTO "django_migrations" VALUES (38,'otp_tokens','0006_auto_20211028_1942','2021-11-15 23:20:03.338412');
INSERT INTO "django_migrations" VALUES (39,'otp_tokens','0007_auto_20211030_0042','2021-11-15 23:20:03.526492');
INSERT INTO "django_migrations" VALUES (40,'otp_tokens','0008_auto_20211031_1623','2021-11-15 23:20:03.665843');
INSERT INTO "django_migrations" VALUES (41,'otp_tokens','0009_auto_20211105_1112','2021-11-15 23:20:03.812675');
INSERT INTO "django_migrations" VALUES (42,'otp_tokens','0010_auto_20211107_1833','2021-11-15 23:20:03.947663');
INSERT INTO "django_migrations" VALUES (43,'otp_tokens','0011_auto_20211107_1910','2021-11-15 23:20:04.100669');
INSERT INTO "django_migrations" VALUES (44,'otp_tokens','0012_auto_20211107_1915','2021-11-15 23:20:04.258127');
INSERT INTO "django_migrations" VALUES (45,'otp_tokens','0013_auto_20211107_1921','2021-11-15 23:20:04.416627');
INSERT INTO "django_migrations" VALUES (46,'otp_tokens','0014_auto_20211107_1927','2021-11-15 23:20:04.582841');
INSERT INTO "django_migrations" VALUES (47,'otp_tokens','0015_auto_20211107_1946','2021-11-15 23:20:04.742618');
INSERT INTO "django_migrations" VALUES (48,'otp_tokens','0016_auto_20211107_2012','2021-11-15 23:20:04.905271');
INSERT INTO "django_migrations" VALUES (49,'otp_tokens','0017_auto_20211108_1916','2021-11-15 23:20:05.080215');
INSERT INTO "django_migrations" VALUES (50,'otp_tokens','0018_auto_20211108_2008','2021-11-15 23:20:05.240900');
INSERT INTO "django_migrations" VALUES (51,'otp_tokens','0019_auto_20211115_2239','2021-11-15 23:20:05.433465');
INSERT INTO "django_migrations" VALUES (52,'otp_tokens','0020_auto_20211115_2319','2021-11-15 23:20:05.604055');
INSERT INTO "django_migrations" VALUES (53,'user','0002_auto_20211107_1946','2021-11-15 23:20:06.070017');
INSERT INTO "django_migrations" VALUES (54,'user','0003_user_active','2021-11-15 23:20:06.303393');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (5,'sessions','session');
INSERT INTO "django_content_type" VALUES (6,'organization','issuingorginization');
INSERT INTO "django_content_type" VALUES (7,'user','user');
INSERT INTO "django_content_type" VALUES (8,'authtoken','token');
INSERT INTO "django_content_type" VALUES (9,'cards','cards');
INSERT INTO "django_content_type" VALUES (10,'logs','cardslogs');
INSERT INTO "django_content_type" VALUES (11,'logs','useraction');
INSERT INTO "django_content_type" VALUES (12,'otp_tokens','useractivation');
INSERT INTO "django_content_type" VALUES (13,'otp_tokens','cardverify');
INSERT INTO "django_content_type" VALUES (14,'otp_tokens','cardtoken');
INSERT INTO "django_content_type" VALUES (15,'mailing_service','tokenmailing');
INSERT INTO "django_content_type" VALUES (16,'mailing_service','generalmail');
INSERT INTO "django_content_type" VALUES (17,'cards','cardsotp');
INSERT INTO "django_content_type" VALUES (18,'logs','errorlogging');
INSERT INTO "django_content_type" VALUES (19,'organization','issuingorginizationotp');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (14,4,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (15,4,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (16,4,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (17,5,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (18,5,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (19,5,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (20,5,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (21,6,'add_issuingorginization','Can add issuing orginization');
INSERT INTO "auth_permission" VALUES (22,6,'change_issuingorginization','Can change issuing orginization');
INSERT INTO "auth_permission" VALUES (23,6,'delete_issuingorginization','Can delete issuing orginization');
INSERT INTO "auth_permission" VALUES (24,6,'view_issuingorginization','Can view issuing orginization');
INSERT INTO "auth_permission" VALUES (25,7,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (26,7,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (27,7,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (28,7,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (29,8,'add_token','Can add Token');
INSERT INTO "auth_permission" VALUES (30,8,'change_token','Can change Token');
INSERT INTO "auth_permission" VALUES (31,8,'delete_token','Can delete Token');
INSERT INTO "auth_permission" VALUES (32,8,'view_token','Can view Token');
INSERT INTO "auth_permission" VALUES (33,9,'add_cards','Can add cards');
INSERT INTO "auth_permission" VALUES (34,9,'change_cards','Can change cards');
INSERT INTO "auth_permission" VALUES (35,9,'delete_cards','Can delete cards');
INSERT INTO "auth_permission" VALUES (36,9,'view_cards','Can view cards');
INSERT INTO "auth_permission" VALUES (37,10,'add_cardslogs','Can add cards logs');
INSERT INTO "auth_permission" VALUES (38,10,'change_cardslogs','Can change cards logs');
INSERT INTO "auth_permission" VALUES (39,10,'delete_cardslogs','Can delete cards logs');
INSERT INTO "auth_permission" VALUES (40,10,'view_cardslogs','Can view cards logs');
INSERT INTO "auth_permission" VALUES (41,11,'add_useraction','Can add user action');
INSERT INTO "auth_permission" VALUES (42,11,'change_useraction','Can change user action');
INSERT INTO "auth_permission" VALUES (43,11,'delete_useraction','Can delete user action');
INSERT INTO "auth_permission" VALUES (44,11,'view_useraction','Can view user action');
INSERT INTO "auth_permission" VALUES (45,12,'add_useractivation','Can add user activation');
INSERT INTO "auth_permission" VALUES (46,12,'change_useractivation','Can change user activation');
INSERT INTO "auth_permission" VALUES (47,12,'delete_useractivation','Can delete user activation');
INSERT INTO "auth_permission" VALUES (48,12,'view_useractivation','Can view user activation');
INSERT INTO "auth_permission" VALUES (49,13,'add_cardverify','Can add card verify');
INSERT INTO "auth_permission" VALUES (50,13,'change_cardverify','Can change card verify');
INSERT INTO "auth_permission" VALUES (51,13,'delete_cardverify','Can delete card verify');
INSERT INTO "auth_permission" VALUES (52,13,'view_cardverify','Can view card verify');
INSERT INTO "auth_permission" VALUES (53,14,'add_cardtoken','Can add card token');
INSERT INTO "auth_permission" VALUES (54,14,'change_cardtoken','Can change card token');
INSERT INTO "auth_permission" VALUES (55,14,'delete_cardtoken','Can delete card token');
INSERT INTO "auth_permission" VALUES (56,14,'view_cardtoken','Can view card token');
INSERT INTO "auth_permission" VALUES (57,15,'add_tokenmailing','Can add token mailing');
INSERT INTO "auth_permission" VALUES (58,15,'change_tokenmailing','Can change token mailing');
INSERT INTO "auth_permission" VALUES (59,15,'delete_tokenmailing','Can delete token mailing');
INSERT INTO "auth_permission" VALUES (60,15,'view_tokenmailing','Can view token mailing');
INSERT INTO "auth_permission" VALUES (61,16,'add_generalmail','Can add general mail');
INSERT INTO "auth_permission" VALUES (62,16,'change_generalmail','Can change general mail');
INSERT INTO "auth_permission" VALUES (63,16,'delete_generalmail','Can delete general mail');
INSERT INTO "auth_permission" VALUES (64,16,'view_generalmail','Can view general mail');
INSERT INTO "auth_permission" VALUES (65,17,'add_cardsotp','Can add cards otp');
INSERT INTO "auth_permission" VALUES (66,17,'change_cardsotp','Can change cards otp');
INSERT INTO "auth_permission" VALUES (67,17,'delete_cardsotp','Can delete cards otp');
INSERT INTO "auth_permission" VALUES (68,17,'view_cardsotp','Can view cards otp');
INSERT INTO "auth_permission" VALUES (69,18,'add_errorlogging','Can add error logging');
INSERT INTO "auth_permission" VALUES (70,18,'change_errorlogging','Can change error logging');
INSERT INTO "auth_permission" VALUES (71,18,'delete_errorlogging','Can delete error logging');
INSERT INTO "auth_permission" VALUES (72,18,'view_errorlogging','Can view error logging');
INSERT INTO "auth_permission" VALUES (73,19,'add_issuingorginizationotp','Can add issuing orginization otp');
INSERT INTO "auth_permission" VALUES (74,19,'change_issuingorginizationotp','Can change issuing orginization otp');
INSERT INTO "auth_permission" VALUES (75,19,'delete_issuingorginizationotp','Can delete issuing orginization otp');
INSERT INTO "auth_permission" VALUES (76,19,'view_issuingorginizationotp','Can view issuing orginization otp');
INSERT INTO "organization_issuingorginization" VALUES (1,'NIMC','https://www.nimc.gov.ng/api','08032178634','hello@nimc.gov.ng','Wuse Zone 6');
INSERT INTO "organization_issuingorginization" VALUES (2,'FRSC','https://www.frsc.gov.ng/api','08032178634','hello@frsc.gov.ng','No. 4 Maputo Street. Zone 3, Wuse, Abuja, Nigeria');
INSERT INTO "organization_issuingorginization" VALUES (5,'Nigeria Immigration Service','https://immigration.gov.ng/api','08032122634','hello@immigration.gov.ng','Nnamdi Azikiwe Airport Road Sauka, Garki, Abuja.');
INSERT INTO "authtoken_token" VALUES ('baadf39ed853f32ca91d7da5c5c4606016f494c4','2021-10-06 23:12:19.041950',1);
INSERT INTO "logs_useraction" VALUES (1,'2021-10-10 18:18:42.522403','User Edited Organization (FRSC)',1);
INSERT INTO "logs_useraction" VALUES (2,'2021-10-10 18:26:13.535975','User Created Organization (Nigeria Immigration Service)',1);
INSERT INTO "logs_useraction" VALUES (3,'2021-10-10 22:22:06.450893','User viewed the list of organization',1);
INSERT INTO "logs_useraction" VALUES (4,'2021-10-10 22:29:18.113355','User viewed the list of organization',1);
INSERT INTO "logs_useraction" VALUES (5,'2021-10-10 22:39:17.833510','User viewed the list of organization',1);
INSERT INTO "logs_useraction" VALUES (6,'2021-10-10 23:01:49.405865','User created a new card (1290873UND)',1);
INSERT INTO "logs_useraction" VALUES (7,'2021-10-19 19:38:29.661666','User viewed the list of organization',1);
INSERT INTO "logs_useraction" VALUES (8,'2021-10-19 19:47:16.341262','User edited his card (1290873UND)',1);
INSERT INTO "cards_cards" VALUES (1,'2024-09-23','2019-08-22',0,1,1,'1290873UND');
INSERT INTO "otp_tokens_useractivation" VALUES (1,'4474',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (2,'6966',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (3,'6511',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (4,'7614',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (5,'0916',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (6,'4365',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (7,'6182',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (8,'3124',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (9,'1106',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (10,'7998',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (11,'1773',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (12,'4817',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (13,'5387',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (14,'3100',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (15,'3723',NULL,0,1);
INSERT INTO "otp_tokens_useractivation" VALUES (16,'3636',NULL,0,1);
INSERT INTO "mailing_service_tokenmailing" VALUES (1,'idowujohn9@gmail.com','User Activation Token','Hi ''.$name.'',
        
          Welcome to Mobile Identity and thank you for signing up! Please click
          the button below to verify your account. Your login details are:
          Username: Your email address writeidowu@outlook.com
          Password: The password you have chosen
          Remember to read our Terms of Use and Privacy Policy. If you have any
          issues accessing the platform, please contact us at
          hello@codedtee.com.
          
          Activate my account
        
        
        Yours sincerely,The Mobile Identity team','2021-10-21 23:16:52.115931');
INSERT INTO "mailing_service_tokenmailing" VALUES (2,'writeidowu@outlook.com','User Activation Token','Hi Jane Doe,
        
          Welcome to Mobile Identity and thank you for signing up! Please click
          the button below to verify your account. Your login details are:
          Username: Your email address writeidowu@outlook.com
          Password: The password you have chosen
          Remember to read our Terms of Use and Privacy Policy. If you have any
          issues accessing the platform, please contact us at
          hello@codedtee.com.
          
          Activate my account
        
        
        Yours sincerely,The Mobile Identity team','2021-10-21 23:38:29.229088');
INSERT INTO "mailing_service_tokenmailing" VALUES (3,'writeidowu@outlook.com','User Activation Token','<html>
  <head> </head>

  <body>
    <div
      style="
        margin: auto;
        width: 60vw;
        color: black;
        box-shadow: 1px 4px 1px 1px #00000057;
      "
    >
      <div
        style="
          width: 60vw;
          padding: 20px 10px 10px 10px;
          background-color: #fff;
        "
      >
        <div>
          <img
            style="margin-left: 2rem"
            src="http://openforum.ng/img/OpenForumLogo.png"
            height="160"
            alt="The Open Forum"
            class="CToWUd"
          />
        </div>
      </div>
      <div
        style="width: 60vw; padding: 0px 20px 10px 10px; background-color: #fff"
      >
        <span style="font-weight: bold; margin-left: 50px; display: block"
          >Hi Jane Doe,</span
        >
        <span style="margin-left: 50px; display: block">
          Welcome to Mobile Identity and thank you for signing up! Please click
          the button below to verify your account. Your login details are:<br />
          Username: Your email address writeidowu@outlook.com<br />
          Password: The password you have chosen<br />
          Remember to read our Terms of Use and Privacy Policy. If you have any
          issues accessing the platform, please contact us at
          hello@codedtee.com.
          <br /><br /><br />
          <a
            style="
              background-color: #ea4639;
              color: #ffffff;
              padding: 15px 30px;
              border-radius: 6px;
            "
            href="https://https://nameless-retreat-73704.herokuapp.com/api/one-time-pass/account-activation//5387''"
            target="_blank"
            >Activate my account</a
          >
        </span>
        <br /><br />
        <span
          style="
            padding: 10px 10px 20px 0px;
            margin-left: 50px;
            display: block;
            font-weight: bold;
          "
          >Yours sincerely,<br />The Mobile Identity team</span
        >
      </div>
    </div>
  </body>
</html>','2021-10-21 23:44:23.351101');
INSERT INTO "mailing_service_tokenmailing" VALUES (4,'writeidowu@outlook.com','User Activation Token','<html>
  <head> </head>

  <body>
    <div
      style="
        margin: auto;
        width: 60vw;
        color: black;
        box-shadow: 1px 4px 1px 1px #00000057;
      "
    >
      <div
        style="
          width: 60vw;
          padding: 20px 10px 10px 10px;
          background-color: #fff;
        "
      >
        <div>
          <img
            style="margin-left: 2rem"
            src="http://openforum.ng/img/OpenForumLogo.png"
            height="160"
            alt="The Open Forum"
            class="CToWUd"
          />
        </div>
      </div>
      <div
        style="width: 60vw; padding: 0px 20px 10px 10px; background-color: #fff"
      >
        <span style="font-weight: bold; margin-left: 50px; display: block"
          >Hi Jane Doe,</span
        >
        <span style="margin-left: 50px; display: block">
          Welcome to Mobile Identity and thank you for signing up! Please click
          the button below to verify your account. Your login details are:<br />
          Username: Your email address writeidowu@outlook.com<br />
          Password: The password you have chosen<br />
          Remember to read our Terms of Use and Privacy Policy. If you have any
          issues accessing the platform, please contact us at
          hello@codedtee.com.
          <br /><br /><br />
          <a
            style="
              background-color: #ea4639;
              color: #ffffff;
              padding: 15px 30px;
              border-radius: 6px;
            "
            href="https://https://nameless-retreat-73704.herokuapp.com/api/one-time-pass/account-activation//3723''"
            target="_blank"
            >Activate my account</a
          >
        </span>
        <br /><br />
        <span
          style="
            padding: 10px 10px 20px 0px;
            margin-left: 50px;
            display: block;
            font-weight: bold;
          "
          >Yours sincerely,<br />The Mobile Identity team</span
        >
      </div>
    </div>
  </body>
</html>','2021-10-21 23:58:07.852892');
INSERT INTO "mailing_service_tokenmailing" VALUES (5,'idowujohn9@outlook.com','User Activation Token','<html>
  <head> </head>

  <body>
    <div
      style="
        margin: auto;
        width: 60vw;
        color: black;
        box-shadow: 1px 4px 1px 1px #00000057;
      "
    >
      <div
        style="
          width: 60vw;
          padding: 20px 10px 10px 10px;
          background-color: #fff;
        "
      >
        <div>
          <img
            style="margin-left: 2rem"
            src="http://openforum.ng/img/OpenForumLogo.png"
            height="160"
            alt="The Open Forum"
            class="CToWUd"
          />
        </div>
      </div>
      <div
        style="width: 60vw; padding: 0px 20px 10px 10px; background-color: #fff"
      >
        <span style="font-weight: bold; margin-left: 50px; display: block"
          >Hi Jon Doe,</span
        >
        <span style="margin-left: 50px; display: block">
          Welcome to Mobile Identity and thank you for signing up! Please click
          the button below to verify your account. Your login details are:<br />
          Username: Your email address idowujohn9@outlook.com<br />
          Password: The password you have chosen<br />
          Remember to read our Terms of Use and Privacy Policy. If you have any
          issues accessing the platform, please contact us at
          hello@codedtee.com.
          <br /><br /><br />
          <a
            style="
              background-color: #ea4639;
              color: #ffffff;
              padding: 15px 30px;
              border-radius: 6px;
            "
            href="https://https://nameless-retreat-73704.herokuapp.com/api/one-time-pass/account-activation//3636''"
            target="_blank"
            >Activate my account</a
          >
        </span>
        <br /><br />
        <span
          style="
            padding: 10px 10px 20px 0px;
            margin-left: 50px;
            display: block;
            font-weight: bold;
          "
          >Yours sincerely,<br />The Mobile Identity team</span
        >
      </div>
    </div>
  </body>
</html>','2021-10-22 00:14:37.338449');
INSERT INTO "user_user" VALUES (1,NULL,'Jane','Doe','2021-10-06 23:11:50.747414','writeidowu@outlook.com','pbkdf2_sha256$260000$lSocuLwcz5FvBeKzbZMpRl$eBus4VHE3pJEiTtAvpzZhXDh9MruGfbZOYo33rZ5D4c=',0,0,'2021-11-15 23:20:05.915315',0,0,1);
INSERT INTO "user_user" VALUES (2,NULL,'Jon','Doe','2021-10-22 00:14:33.171864','idowujohn9@outlook.com','pbkdf2_sha256$260000$0V9eVBwWIudy2Y5Ks47B4m$DEGrXzzDdsg3ZZJ19HZpmGPgGhAbH34WNU4atZnnHkg=',0,0,'2021-11-15 23:20:05.915315',0,0,1);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "logs_useraction_user_id_id_fe189cf7" ON "logs_useraction" (
	"user_id_id"
);
CREATE INDEX IF NOT EXISTS "cards_cards_issuing_organization_id_b4b933dc" ON "cards_cards" (
	"issuing_organization_id"
);
CREATE INDEX IF NOT EXISTS "cards_cards_user_id_id_02349c5b" ON "cards_cards" (
	"user_id_id"
);
CREATE INDEX IF NOT EXISTS "otp_tokens_useractivation_user_id_aba201cd" ON "otp_tokens_useractivation" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "mailing_service_generalmail_sent_by_id_d174cadc" ON "mailing_service_generalmail" (
	"sent_by_id"
);
CREATE INDEX IF NOT EXISTS "cards_cardsotp_approved_by_id_dbb7d4de" ON "cards_cardsotp" (
	"approved_by_id"
);
CREATE INDEX IF NOT EXISTS "cards_cardsotp_issuing_organization_id_483a0dad" ON "cards_cardsotp" (
	"issuing_organization_id"
);
CREATE INDEX IF NOT EXISTS "cards_cardsotp_requested_by_id_9d26bd1a" ON "cards_cardsotp" (
	"requested_by_id"
);
CREATE INDEX IF NOT EXISTS "logs_cardslogs_card_id_4cde5b4c" ON "logs_cardslogs" (
	"card_id"
);
CREATE INDEX IF NOT EXISTS "logs_cardslogs_user_id_id_7b2798ae" ON "logs_cardslogs" (
	"user_id_id"
);
CREATE INDEX IF NOT EXISTS "otp_tokens_cardtoken_card_id_id_0b5dd2ad" ON "otp_tokens_cardtoken" (
	"card_id_id"
);
CREATE INDEX IF NOT EXISTS "otp_tokens_cardtoken_card_owner_id_e52b2571" ON "otp_tokens_cardtoken" (
	"card_owner_id"
);
CREATE INDEX IF NOT EXISTS "otp_tokens_cardverify_card_id_id_6a933a9d" ON "otp_tokens_cardverify" (
	"card_id_id"
);
CREATE INDEX IF NOT EXISTS "otp_tokens_cardverify_card_owner_id_7c0da39c" ON "otp_tokens_cardverify" (
	"card_owner_id"
);
COMMIT;
