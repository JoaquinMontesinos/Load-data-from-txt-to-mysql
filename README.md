# Load data from .txt to mysql database

Taking advantage of the repercussion that the facebook security breach has had (Facebook Leak 2019), I did a superficial analysis of the data found on the network.

At first glance, I used commands from the terminal. 

```
  wc spain.txt -- 10.894.206
  grep @ spain.txt | wc -- 75.636
  grep -w female spain.txt | wc -- 4.964.218
  grep relationship spain.txt | wc -- 393.081
  head -10 spain.txt
```

Originally, we found the data in .txt files with separation ':' between columns and some of the columns as empty. Each line has the following data:
- Phone number
- Facebook ID (http://facebook.com/profile.php?id={Facebook})
- Username
- UserSurname
- City and country
- Email
- Civil status
- Job

As my computer had difficulties in opening the document flat + 2gb, I thought about how to load large files in a mysql database.
Originally I thought of a simple ```INSERT INTO``` but it took longer than desired, so I decided to use the ```LOAD DATA LOCAL INFILE``` function, since it inserts data from large files faster. There are lines that do not have all the information so, I did a little cleaning within the data load function.

For the test file, I have used totally anonymous data, since the purpose of this test is educational for data analysis and insertion. 

We all have the concern of finding our mobile phone number in this leak. From now on, all those affected in the breach, we must be careful with the sms and phishing campaigns that reach our phones. 
