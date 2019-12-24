# Project Usage?

If you work in a monitoring role or any other parts of a technical team that works with NetData as a monitoring tool on your server(s), you might need sometimes just to see your NetData alarms which this simple program shows them all in one page(Terminal + log file).

**This program just collects _critical_ alarms**
## Requirement:

1- you need python3.x to be installed:
``` bash
apt update
apt install python3.6
```
2- You need pip3 to be installed:
``` bash
wget -P . https://bootstrap.pypa.io/get-pip.py
python3 ./get-pip.py
```
3- The packages you need to be installed: 
```
pip3 install requests
pip3 install ipaddress
```
## How to run the project:
When you run the project you have 2 ways to see the out put:
1. See a bunch of hosts' alarms
2. See single host's alarm
**If you want to check a number of hosts' alarms:**

```
You need to have a text file with the name of ` ip_hosts.txt ` beside the project(in the same directory) and put your servers IPs in that as it's shown in `ip_hosts_sample.txt`'s file, then after you ran the project, it will ask you to specify the host or hosts you want to see and you should type `all` in the terminal. in this way plus seeing the log in terminal, you will have a log file containing critical alarms.
In your terminal you will see warnings in **Yellow** and critical errors in **Red** 
```
**If you want to check a specific host's alarms:**
```
After you ran te project, it will ask you to enter the host('s) you want to see and you should just enter the ip of the host you want to investigate, it will show you warnings in **Yellow** and critical errors in **Red** . 
```

### Running Steps:
1- Clone the project:
``` bash
git clone https://github.com/Maziar110/netdata_alarms.git
```
2- Head to the project directory
``` bash
cd ./netdata_alarms
```
3- If you have all the requirement successfully installed, run the bellow command in the project's directory:
``` bash
python3 api.py
```
it prints out all critical alarms of the mentioned servers in the `ip_hosts.txt` file.

__

Let me know if there's any issue or furthur talk.
you can be in touch with me through:

[Linkedin](https://www.linkedin.com/in/maziar-shahsavanpour-a4210088/)

[Whatsapp](https://api.whatsapp.com/send?phone=+989156262067)