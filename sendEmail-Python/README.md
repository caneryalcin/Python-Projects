# sendEmail-Python
This project aims to sending an email to gmail.

---

When you run the code if you didn't set password for application in gmail it will give you a failure.Follow the steps of link in below.

https://support.google.com/mail/?p=BadCredentials

After you set password and run the code again if you don't take any failure you will receive an email to your gmail.

----
## Run Python script at startup in Ubuntu

Run the following commands on terminal

make sure you have permission to run.
```
chmod +x /etc/rc.local

chmod +x /path/to/your_script.py
```
---

```
nano /etc/rc.local
```
and write your path to your python script to the end like example in below
```
python /path/to/your_script.py

exit 0
```
