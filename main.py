import pymysql as sql
import os
import re

if __name__ == '__main__':
    path='./'
    files = [f for f in os.listdir(path) if '.txt' in f]
    for data_txt in files:
        country = re.split('.txt', data_txt)[0]
        try:
            cnx = sql.connect(db="Facebook", host='127.0.0.1', port=3306, user='root', passwd='root', local_infile=True)
            cursor = cnx.cursor()

            #create database
            # SHOW GLOBAL VARIABLES LIKE 'local_infile';
            # SET GLOBAL local_infile = true;
            create_database = "CREATE DATABASE IF NOT EXISTS Facebook CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
            cursor.execute(create_database)
            cnx.commit()

            #create table
            create_sql = "CREATE TABLE IF NOT EXISTS Facebook.te_fb_lake ( " \
                       "id int(11) NOT NULL AUTO_INCREMENT, " \
                       "phone_no varchar(250) DEFAULT NULL, " \
                       "user_id int(11) DEFAULT NULL, " \
                       "fname varchar(250) DEFAULT NULL, " \
                       "lname varchar(250) DEFAULT NULL, " \
                       "gender varchar(20) DEFAULT NULL, " \
                       "city1 varchar(250) DEFAULT NULL, " \
                       "city2 varchar(250) DEFAULT NULL, " \
                       "relationship varchar(50) DEFAULT NULL, " \
                       "company varchar(200) DEFAULT NULL, " \
                       "seen varchar(20) DEFAULT NULL, " \
                       "email varchar(200) DEFAULT NULL, " \
                       "country varchar(100) DEFAULT NULL, " \
                       "PRIMARY KEY (id) );"
            cursor.execute(create_sql)
            cnx.commit()

            # Load data
            load_sql = "LOAD DATA LOCAL INFILE '{file}' INTO TABLE Facebook.te_fb_lake " \
                                                                "CHARACTER SET utf8mb4 " \
                                                                "FIELDS TERMINATED BY ':' " \
                                                                "OPTIONALLY ENCLOSED BY '\"' " \
                                                                "(@phone_no, @user_id, @fname, @lname, @gender, @city1, @city2, @relationship, @company, @seen, @email, @country) " \
                                                                "set id = NULL, " \
                                                                "phone_no = if(@phone_no = '', NULL, @phone_no), " \
                                                                "user_id = if(@user_id = '', NULL, @user_id), " \
                                                                "fname = if(@fname = '', NULL, @fname), " \
                                                                "lname = if(@lname = '', NULL, @lname), " \
                                                                "gender = if(@gender = '', NULL, @gender), " \
                                                                "city1 = if(@city1 = '', NULL, @city1), " \
                                                                "city2 = if(@city2 = '', NULL, @city2), " \
                                                                "relationship = if(@relationship = '', NULL, @relationship), " \
                                                                "company = if(@company = '', NULL, @company), " \
                                                                "seen = if(@seen = '', NULL, @seen), " \
                                                                "email = if(@email = '', NULL, @email), " \
                                                                "country='{country}' ;".format(file=str(path+data_txt), country=country)
            cursor.execute(load_sql)
            cnx.commit()
            cursor.close()
        except Exception as e:
            cnx.rollback()
            print("SQl error: " + str(e.with_traceback()))
            if (cnx.open):
                cnx.close()
