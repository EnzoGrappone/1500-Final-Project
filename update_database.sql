INSERT INTO car_type(type_id,model,car_year,manufacturing_country,msrp) VALUES
 ('T1','230i',2024,'Mexico',39200)
,('T2','M240i',2024,'Mexico',50100)
,('T3','M2',2024,'Mexico',64900)
,('T4','330i',2024,'Mexico',47500)
,('T5','M340i',2024,'Germany',61600)
,('T6','M3 Competition',2024,'Germany',85300)
,('T7','430i',2024,'Germany',52700)
,('T8','430i Convertible',2024,'Germany',58700)
,('T9','430i GranCoupe',2024,'Germany',51200)
,('T10','M440i',2024,'Germany',66250)
,('T11','M4 Competition',2024,'Germany',88300)
,('T12','i4 M50',2024,'Germany',70700)
,('T13','530i',2024,'Germany',60500)
,('T14','540i',2024,'Germany',65200)
,('T15','i5 M60',2024,'Germany',84100)
,('T16','M5',2023,'Germany',119500)
,('T17','740i',2024,'Germany',99400)
,('T18','760i',2024,'Germany',121300)
,('T19','i7 M70',2023,'Germany',168500)
,('T20','840i',2024,'Germany',90800)
,('T21','850i',2023,'Germany',106300)
,('T22','M8',2024,'Germany',138800)
,('T23','X1 M35i',2024,'Germany',50350)
,('T24','iX1',2024,'Germany',51200)
,('T25','X2 M35i',2024,'Germany',42450)
,('T26','X3 xDrive30i',2024,'United States',49500)
,('T27','X3 M40i',2024,'United States',64100)
,('T28','iX3',2024,'United States',51200)
,('T29','X3M',2024,'United States',85300)
,('T30','X4 xDrive30i',2024,'United States',55300)
,('T31','X4 M40i',2024,'United States',66700)
,('T32','X4M',2024,'United States',79100)
,('T33','X5 xDrive40i',2024,'United States',65700)
,('T34','X5 M60i',2024,'United States',90000)
,('T35','X5M',2024,'United States',124800)
,('T36','X6 xDrive40i',2024,'United States',74500)
,('T37','X6 M60i',2024,'United States',94300)
,('T38','X6M',2024,'United States',129700)
,('T39','X7 M60i',2024,'United States',110900)
,('T40','XM',2023,'United States',159000)
,('T41','Z4 sDrive30i',2024,'Austria',57150)
,('T42','Z4 M40i',2024,'Austria',72900);


INSERT INTO new_inventory(vin,type_id,color) VALUES
 ('4T1BF1FK9CU602278','T1','Blue')
,('1HGCM82633A123456','T1','Grey')
,('5NPE34AF5FH006783','T1','Grey')
,('5TFTU4GN0BX045914','T1','White')
,('1FDNF20L14EB49659','T2','Purple')
,('2FMZA53431BB56187','T4','Silver')
,('3GTRKVE35AG234455','T4','Grey')
,('1G11C5SA0DF201911','T4','Grey')
,('1FDKF37G8VEC89629','T5','White')
,('5XYKW4A71FG663316','T6','Green')
,('3TMJU4GN9DM180986','T7','Red')
,('1FTFX1EF6DFB84713','T7','White')
,('5UXKU2C53F0F17335','T8','White')
,('JTHCK262165031859','T9','Red')
,('KNADE223896560197','T9','Blue')
,('KLAJC52Z71K692677','T9','Blue')
,('1GNFK16307R434394','T10','Black')
,('JF1GH61669G814080','T10','Grey')
,('5TEUX4ENXAZ726555','T11','Yellow')
,('5GAEV23788J175003','T12','Blue')
,('2HGFB2F94CH381732','T14','Silver')
,('JTEBU5JR5E5138498','T14','Silver')
,('1FTSE34L36DA33561','T14','Silver')
,('1C4NJDEB6ED824928','T14','Black')
,('KMHCG35G7YU024201','T14','Grey')
,('2FMZA5347YBB97609','T14','Red')
,('2FDKF38G0RCA71968','T15','Blue')
,('1GNEC13Z05R230029','T16','White')
,('1G1ZD5E07CF137383','T17','Black')
,('1G6KD54YX5U257017','T18','Black')
,('1C6RR7FT6ES418251','T19','Blue')
,('1FMCU93198KA16462','T20','White')
,('1FMCU0JXXEUC07133','T20','White')
,('4GTJ7C1391J718070','T21','White')
,('1GNFK13508R177812','T24','Black')
,('3C6UR5HJ9EG213069','T24','Grey')
,('JKAVN2D126A027543','T24','Grey')
,('1HGCM56886A078932','T25','Grey')
,('3VWDZ7AJXBM362552','T25','Grey')
,('3C6TR5FT0DG653325','T26','Grey')
,('KMHDH4AE2BU166782','T26','White')
,('KMHTC6AD8DU191170','T27','Green')
,('1C4NJDBB6DD287576','T28','Black')
,('JTLZE4FE8CJ041885','T30','White')
,('4T1BF1FK8CU179144','T30','White')
,('5TBBT44104S419438','T35','Black')
,('3VWCT71K16M056240','T35','Black')
,('1FAFP53U17A199572','T37','Purple')
,('1FMEU6DE5AUB39002','T37','White')
,('1FTPX14538FB26125','T38','Silver');



INSERT INTO used_inventory(vin,brand,model,car_year,color,mileage,car_condition,warranty_status,price) VALUES
 ('JH4CU2F68DC012523','Audi','A6',2017,'Silver',90003,'Good','0 Year',25800)
,('1GKFK63867J255396','Alfa Romeo','Giulia',2019,'red',20010,'Good','0 Year',35000)
,('1FAFP58UX4A120551','BMW','330ci',2006,'Silver',112004,'Good','0 Year',12999)
,('5FYD4FV108B043585','BMW','520i',2011,'White',102304,'Good','0 Year',22033)
,('YV1MC67268J014522','BMW','XM',2023,'Black',30001,'Good','2 Years',80000)
,('WBANB53517CP04587','BMW','X5 xDrive40i',2021,'White',50200,'Good','0 Year',45000)
,('3VWCM31Y05M304180','Ford','Focus RS',2020,'Blue',102504,'Good','0 Year',35000)
,('3B7KC23642M213805','GMC','Yukon',2018,'Red',130300,'Medium','0 Year',21000)
,('1N4AL21E28N402642','Honda','CRV',2020,'Red',100003,'Good','0 Year',26000)
,('1J8HG48K36C284509','Honda','Civic TypeR',2022,'Grey',50200,'Good','1 Year',40020)
,('WDDGF56X79R047880','Honda','Pilot',2019,'White',110003,'Good','0 Year',23000)
,('1FAHP2F87DG266058','Jaguar','F-Pace',2020,'Green',130003,'Medium','0 Year',23000)
,('5TDZT34A54S233491','Jaguar','F-Type',2022,'Green',60200,'Good','0 Year',55000)
,('3GTP2WE33BG204868','KIA','Telluride',2022,'White',140003,'Good','0 Year',23000)
,('1FTWF32Y85EB95627','Land Rover','Velar',2018,'Grey',130103,'Good','0 Year',41020)
,('1B3CB4HA4AD656189','Land Rover','Vogue',2016,'White',110203,'Good','0 Year',55000)
,('WP0AA29964S689342','Mini','Cooper S',2014,'Red',150003,'Medium','0 Year',21000)
,('4S3BE686047216403','Mini','Clubman JCW',2022,'Grey',60300,'Good','0 Year',26000)
,('1FTFW1ET6EKF07983','Tesla','Model S',2020,'Red',100203,'Good','0 Year',23000)
,('3GSCL33P39S555162','Tesla','Model X',2020,'Blue',110202,'Good','0 Year',24000);

INSERT INTO customer(first_name,last_name,customer_email) VALUES
 ('Thomas','Lawrance','thomas.lawrance@gmail.com')
,('Jane','Donohue','Jane.Donohue@gmail.com')
,('Michael','Lee','michael.lee@gmail.com')
,('Emily','Davis','emily.davis@outlook.com')
,('David','Lawrance','david.lawrance@gmail.com')
,('Sarah','Wilson','sarah.wilson@gmail.com')
,('Daniel','Martinez','daniel.martinez@gmail.com')
,('Jessica','Taylor','jessica.taylor@gmail.com')
,('Matthew','Anderson','matthew.anderson@gmail.com')
,('Ashley','Waltson','ashley.thomas@gmail.com')
,('Christopher','Gao','christopher.gao@gmail.com')
,('Amanda','Clark','amanda.clark@outlook.com')
,('Joshua','Hernandez','joshua.hernandez@gmail.com')
,('Brittany','Robinson','brittany.robinson@icloud.com')
,('Ethan','Lewis','ethan.lewis@gmail.com')
,('Samantha','Walker','samantha.walker@gmail.com')
,('Brandon','King','brandon.king@outlook.com')
,('Megan','Hall','megan.hall@gmail.com')
,('Andrew','Scott','andrew.scott@gmail.com')
,('Jennifer','Young','jennifer.young@gmail.com')
,('Ryan','Falcone','ryan.falcone@gmail.com')
,('Elizabeth','Adams','elizabeth.adams@gmail.com')
,('Joseph','Baker','joseph.baker@outlook.com')
,('Lauren','Berry','lauren.berry@gmail.com')
,('Tyler','Harris','tyler.harris@outlook.com');

INSERT INTO cust_contact(customer_email,phone_number,address,DOB) VALUES
 ('thomas.lawrance@gmail.com','(412) 123-4567','123 Maple Street, Pittsburgh, PA 1520','1985-03-01')
,('Jane.Donohue@gmail.com','(717) 234-5678','456 Oak Avenue, Harrisburg, PA 17101','1990-07-15')
,('michael.lee@gmail.com','(215) 345-6789','789 Pine Road, Philadelphia, PA 19101','1982-10-23')
,('emily.davis@outlook.com','(610) 456-7890','321 Cedar Lane, Allentown, PA 18101','1995-04-10')
,('david.lawrance@gmail.com','(814) 567-8901','654 Birch Drive, Erie, PA 16501','1988-02-28')
,('sarah.wilson@gmail.com','(570) 678-9012','987 Elm Street, Scranton, PA 18501','1992-06-12')
,('daniel.martinez@gmail.com','(717) 789-0123','159 Spruce Avenue, Lancaster, PA 17601','1984-08-03')
,('jessica.taylor@gmail.com','(610) 890-1234','753 Maple Boulevard, Bethlehem, PA 18001','1989-05-25')
,('matthew.anderson@gmail.com','(717) 901-2345','852 Oak Circle, York, PA 17401','1991-11-17')
,('ashley.thomas@gmail.com','(814) 012-3456','456 Pine Court, Altoona, PA 16601','1986-09-07')
,('christopher.gao@gmail.com','(610) 123-4567','369 Birch Street, Reading, PA 19601','1983-01-22')
,('amanda.clark@outlook.com','(610) 234-5678','951 Cedar Drive, Easton, PA 18042','1990-12-09')
,('joshua.hernandez@gmail.com','(570) 345-6789','147 Elm Avenue, Wilkes-Barre, PA 18701','1987-04-21')
,('brittany.robinson@icloud.com','(717) 456-7890','258 Spruce Street, York, PA 17401','1993-10-05')
,('ethan.lewis@gmail.com','(717) 567-8901','369 Maple Lane, Harrisburg, PA 17101','1981-02-16')
,('samantha.walker@gmail.com','(570) 678-9012','951 Oak Boulevard, Scranton, PA 18501','1985-06-08')
,('brandon.king@outlook.com','(412) 789-0123','147 Pine Circle, Pittsburgh, PA 15201','1989-08-14')
,('megan.hall@gmail.com','(814) 890-1234','258 Birch Court, Erie, PA 16501','1992-12-24')
,('andrew.scott@gmail.com','(610) 901-2345','369 Cedar Drive, Allentown, PA 18101','1984-03-30')
,('jennifer.young@gmail.com','(610) 012-3456','951 Spruce Avenue, Bethlehem, PA 18001','1988-09-11')
,('ryan.falcone@gmail.com','(610) 123-4567','147 Elm Boulevard, Reading, PA 19601','2003-11-29')
,('elizabeth.adams@gmail.com','(814) 234-5678','258 Pine Street, Altoona, PA 16601','1991-05-04')
,('joseph.baker@outlook.com','(215) 345-6789','369 Maple Court, Philadelphia, PA 19101','1983-01-15')
,('lauren.berry@gmail.com','(717) 456-7890','951 Birch Lane, Lancaster, PA 17601','1990-07-19')
,('tyler.harris@outlook.com','(610) 567-8901','147 Oak Drive, Easton, PA 18042','1987-10-26');

INSERT INTO department(department_id,department_name,department_size) VALUES
 ('D1','Sales',5)
,('D2','Mechanics',4)
,('D3','Finance',4)
,('D4','Management',3);

INSERT INTO emp_info(email,phone_number,address,DOB,salary) VALUES
 ('DB@gmail.com',14126789013,'1453 Elm Street Springfield IL 62704','1990-03-14',50000)
,('ava.mitchell@hotmail.com',14121234567,'982 Maple Avenue Columbus OH 43215','1987-07-08',55000)
,('noah.parker@gmail.com',14122345678,'63 Birchwood Lane Austin TX 78701','1995-01-22',75000)
,('olivia.harrison@gmail.com',14123456789,'2075 Sunset Boulevard Los Angeles CA 90028','1979-11-03',80000)
,('liam.turner@gmail.com',14124567890,'813 Oakwood Drive Denver CO 80203','1985-08-16',76000)
,('emma.brooks@gmail.com',14125678901,'49 Pinehurst Road Atlanta GA 30303','1992-10-29',65000)
,('sophia.morgan@gmail.com',14126789012,'552 Beacon Street Boston MA 02108','1988-06-12',60000)
,('lucas.bennett@gmail.com',12137890123,'1317 Willow Creek Court Miami FL 33101','1999-04-27',85000)
,('amelia.walker@gmail.com',17388901234,'398 Cedar Hill Way Seattle WA 98101','1980-12-05',75000)
,('ethan.reed@gmail.com',12239012345,'2409 Valley View Drive Phoenix AZ 85001','1993-05-20',45000)
,('harper.foster@gmail.com',13210123456,'88 Highland Avenue San Francisco CA 94103','1986-09-09',50000)
,('jackson.hughes@gmail.com',14261234568,'1162 Gardenia Circle Nashville TN 37203','1995-02-15',42000)
,('henry.carter@gmail.com',15642345679,'760 Riverbend Drive Dallas TX 75201','1978-07-30',70000)
,('mia.richardson@gmail.com',14123456780,'305 Magnolia Street Charleston SC 29401','1983-10-06',55000)
,('audrey.cooper@gmail.com',13224567891,'1017 Laurel Avenue Minneapolis MN 55401','1997-03-25',60000)
,('samuel.grant@gmail.com',14525678902,'2258 Sycamore Road Portland OR 97201','1989-06-10',75000);

INSERT INTO employee(employee_id, first_name,last_name,department_id,email) VALUES
 ('E1','Damion','Briley','D1','DB@gmail.com')
,('E2','Ava','Mitchell','D1','ava.mitchell@hotmail.com')
,('E3','Noah','Parker','D1','noah.parker@gmail.com')
,('E4','Olivia','Harrison','D1','olivia.harrison@gmail.com')
,('E5','Liam','Turner','D1','liam.turner@gmail.com')
,('E6','Emma','Brooks','D2','emma.brooks@gmail.com')
,('E7','Sophia','Morgan','D2','sophia.morgan@gmail.com')
,('E8','Lucas','Bennett','D2','lucas.bennett@gmail.com')
,('E9','Amelia','Walker','D2','amelia.walker@gmail.com')
,('E10','Ethan','Reed','D3','ethan.reed@gmail.com')
,('E11','Harper','Foster','D3','harper.foster@gmail.com')
,('E12','Jackson','Hughes','D3','jackson.hughes@gmail.com')
,('E13','Henry','Carter','D3','henry.carter@gmail.com')
,('E14','Mia','Richardson','D4','mia.richardson@gmail.com')
,('E15','Audrey','Cooper','D4','audrey.cooper@gmail.com')
,('E16','Samuel','Grant','D4','samuel.grant@gmail.com');

INSERT INTO service(service_id,customer_email,type_id,license_plate_number,color,service_type,appointment_date,employee_id) VALUES
 ('SE1','david.lawrance@gmail.com','T5','NUW-3445','Orange','Oil & Filter Change','2024-12-18','E10')
,('SE2','amanda.clark@outlook.com','T4','HTC-5787','Blue','Maintenance','2024-12-18','E12')
,('SE3','tyler.harris@outlook.com','T17','ECY-1212','Red','Maintenance','2024-12-18','E10')
,('SE4','andrew.scott@gmail.com','T2','SJU-2423','Black','Maintenance','2024-12-20','E11')
,('SE5','joshua.hernandez@gmail.com','T2','WHAT','Grey','Maintenance','2024-12-20','E13')
,('SE6','sarah.wilson@gmail.com','T3','YWO-1303','White','Oil & Filter Change','2024-12-23','E10')
,('SE7','brandon.king@outlook.com','T8','NXA-5818','Blue','Oil & Filter Change','2024-12-23','E11')
,('SE8','joshua.hernandez@gmail.com','T10','WHAT','White','Wheel Alignment','2024-12-29','E13')
,('SE9','thomas.lawrance@gmail.com','T11','AMG-335','Red','Maintenance','2024-12-29','E12')
,('SE10','Jane.Donohue@gmail.com','T12','ESW-9931','White','Maintenance','2025-01-18','E12')
,('SE11','jessica.taylor@gmail.com','T13','MCN-5245','Grey','Oil & Filter Change','2025-01-28','E10')
,('SE12','david.lawrance@gmail.com','T19','NUW-3445','Orange','Transmission inspection','2025-02-10','E13')
,('SE13','elizabeth.adams@gmail.com','T20','ZDF-6647','Green','State Inspection','2025-08-18','E11')
,('SE14','matthew.anderson@gmail.com','T3','OYI-6151','Grey','State Inspection','2025-08-18','E11')
,('SE15','jessica.taylor@gmail.com','T22','REV-5153','Blue','State Inspection','2025-08-18','E11');

INSERT INTO sale(sale_id,customer_email,vin,sale_date,sale_price,employee_id) VALUES
 ('SA1','thomas.lawrance@gmail.com','1J4FA24117L197804','2024-9-2',73100,'E2')
,('SA2','Jane.Donohue@gmail.com','1FTFW1ET7BFC86432','2024-9-2',61500,'E2')
,('SA3','michael.lee@gmail.com','1B3ES56C85D129197','2024-9-4',60350,'E3')
,('SA4','emily.davis@outlook.com','1GCRKTE71DZ213906','2024-9-10',110400,'E2')
,('SA5','david.lawrance@gmail.com','4T4BF1FK3CR212265','2024-9-12',116300,'E4')
,('SA6','sarah.wilson@gmail.com','WDBRF61J33F380547','2024-9-12',57500,'E3')
,('SA7','daniel.martinez@gmail.com','1N4AA5AP0BC842113','2024-9-15',61200,'E3')
,('SA8','jessica.taylor@gmail.com','4T1BE46K88U290594','2024-9-15',75700,'E4')
,('SA9','matthew.anderson@gmail.com','3FADP4CJ3EM114092','2024-9-16',57500,'E5')
,('SA10','ashley.thomas@gmail.com','1FALP6246VH105040','2024-9-29',75700,'E1')
,('SA11','christopher.gao@gmail.com','KL4CJASB3EB718341','2024-10-1',95300,'E4')
,('SA12','amanda.clark@outlook.com','1GCCT19X138174045','2024-10-2',57500,'E1')
,('SA13','joshua.hernandez@gmail.com','2D8GV572X6H147601','2024-10-10',75700,'E5')
,('SA14','brittany.robinson@icloud.com','1N4AL21E07N415727','2024-10-12',134800,'E4')
,('SA15','ethan.lewis@gmail.com','JF2SJAFC8FH415656','2024-10-12',57500,'E3')
,('SA16','samantha.walker@gmail.com','1G11C5SA5DF105742','2024-10-12',59500,'E3')
,('SA17','brandon.king@outlook.com','3GTP2VE78DG306733','2024-10-12',120900,'E1')
,('SA18','megan.hall@gmail.com','JNKCV54E67M945621','2024-10-15',59500,'E4')
,('SA19','andrew.scott@gmail.com','1HGCP2F30CA016205','2024-10-16',89100,'E5')
,('SA20','jennifer.young@gmail.com','3GCUKRECXEG218078','2024-10-17',94100,'E4')
,('SA21','ryan.falcone@gmail.com','1FTRW08L92KC72610','2024-10-17',70500,'E1')
,('SA22','elizabeth.adams@gmail.com','3C6JR6AT1EG188687','2024-10-18',94100,'E5')
,('SA23','joseph.baker@outlook.com','2B6KB31Z1SK571813','2024-10-18',120900,'E4')
,('SA24','lauren.berry@gmail.com','WDDKK5KF8CF178411','2024-10-19',82900,'E1')
,('SA25','tyler.harris@outlook.com','1G2ZM587074152345','2024-10-28',68700,'E1');

ALTER TABLE cust_contact ADD password VARCHAR(20);

UPDATE cust_contact
SET password = 'P@ssword123!'
WHERE customer_email = 'thomas.lawrance@gmail.com';

UPDATE cust_contact
SET password = 'SecureP@ssw0rd!'
WHERE customer_email = 'Jane.Donohue@gmail.com';

UPDATE cust_contact
SET password = 'MyP@ssw0rd42'
WHERE customer_email = 'michael.lee@gmail.com';

UPDATE cust_contact
SET password = 'Passw0rd#Safe'
WHERE customer_email = 'emily.davis@outlook.com';

UPDATE cust_contact
SET password = 'Str0ngPass!'
WHERE customer_email = 'david.lawrance@gmail.com';

UPDATE cust_contact
SET password = 'P@ssMeN0w!'
WHERE customer_email = 'sarah.wilson@gmail.com';

UPDATE cust_contact
SET password = 'KeepIt$afe!'
WHERE customer_email = 'daniel.martinez@gmail.com';

UPDATE cust_contact
SET password = 'N0tSoE@sy1'
WHERE customer_email = 'jessica.taylor@gmail.com';

UPDATE cust_contact
SET password = 'EasyP@ss123'
WHERE customer_email = 'matthew.anderson@gmail.com';

UPDATE cust_contact
SET password = 'Pr0tectM3!'
WHERE customer_email = 'ashley.thomas@gmail.com';

UPDATE cust_contact
SET password = 'SecureMe#42'
WHERE customer_email = 'christopher.gao@gmail.com';

UPDATE cust_contact
SET password = 'SaveMyP@ss!'
WHERE customer_email = 'amanda.clark@outlook.com';

UPDATE cust_contact
SET password = 'L3tMeIn@123'
WHERE customer_email = 'joshua.hernandez@gmail.com';

UPDATE cust_contact
SET password = 'Acc3ssM3Now!'
WHERE customer_email = 'brittany.robinson@icloud.com';

UPDATE cust_contact
SET password = 'P@ssW0rthy!'
WHERE customer_email = 'ethan.lewis@gmail.com';

UPDATE cust_contact
SET password = 'UnCr@ckable1'
WHERE customer_email = 'samantha.walker@gmail.com';

UPDATE cust_contact
SET password = 'S@feGuard42'
WHERE customer_email = 'brandon.king@outlook.com';

UPDATE cust_contact
SET password = 'VaultMe@#1'
WHERE customer_email = 'megan.hall@gmail.com';

UPDATE cust_contact
SET password = 'MyS3cur3Key'
WHERE customer_email = 'andrew.scott@gmail.com';

UPDATE cust_contact
SET password = 'E@syT0R3m3mber'
WHERE customer_email = 'jennifer.young@gmail.com';

UPDATE cust_contact
SET password = 'P@ssSafety1'
WHERE customer_email = 'ryan.falcone@gmail.com';

UPDATE cust_contact
SET password = 'H1d3MyK3y!'
WHERE customer_email = 'elizabeth.adams@gmail.com';

UPDATE cust_contact
SET password = 'M3morableP@ss!'
WHERE customer_email = 'joseph.baker@outlook.com';

UPDATE cust_contact
SET password = 'Sh@rpM3mory!'
WHERE customer_email = 'lauren.berry@gmail.com';

UPDATE cust_contact
SET password = 'TightK3y@123'
WHERE customer_email = 'tyler.harris@outlook.com';

ALTER TABLE emp_info ADD password VARCHAR(20);

UPDATE emp_info
SET password = 'T0p$3cur3'
WHERE email = 'DB@gmail.com';

UPDATE emp_info
SET password = 'P@ssW0rd87'
WHERE email = 'ava.mitchell@hotmail.com';

UPDATE emp_info
SET password = 'P@rk3rKey!'
WHERE email = 'noah.parker@gmail.com';

UPDATE emp_info
SET password = 'H@rris0n$'
WHERE email = 'olivia.harrison@gmail.com';

UPDATE emp_info
SET password = 'T3rn0ver!'
WHERE email = 'liam.turner@gmail.com';

UPDATE emp_info
SET password = 'E!mm4S@fe'
WHERE email = 'emma.brooks@gmail.com';

UPDATE emp_info
SET password = 'M0rg@n123'
WHERE email = 'sophia.morgan@gmail.com';

UPDATE emp_info
SET password = 'L0ck$M3N'
WHERE email = 'lucas.bennett@gmail.com';

UPDATE emp_info
SET password = 'W@lker$afe'
WHERE email = 'amelia.walker@gmail.com';

UPDATE emp_info
SET password = 'R3edR0ad!'
WHERE email = 'ethan.reed@gmail.com';

UPDATE emp_info
SET password = 'F0st3r@Key'
WHERE email = 'harper.foster@gmail.com';

UPDATE emp_info
SET password = 'Hug3s#123'
WHERE email = 'jackson.hughes@gmail.com';

UPDATE emp_info
SET password = 'C@rt3r$afe'
WHERE email = 'henry.carter@gmail.com';

UPDATE emp_info
SET password = 'R!chards3c'
WHERE email = 'mia.richardson@gmail.com';

UPDATE emp_info
SET password = 'C0operK3y'
WHERE email = 'audrey.cooper@gmail.com';

UPDATE emp_info
SET password = 'Gr@nt@cess'
WHERE email = 'samuel.grant@gmail.com';
