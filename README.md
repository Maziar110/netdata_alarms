# What this project does?

If you work in a monitoring role or any other parts of a technical team that works with NetData as a monitoring tools on your server(s), you might need sometimes just to see your NetData alarms.
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
3- you need request package to be installed: 
```
pip3 install requests
```
## How to run the project:
You need to have a text file with the name of ` ip_hosts.txt ` beside the project(in the same directory) and put your servers IPs in that as it's shown in `ip_hosts_sample.txt`'s file, the project will add :19999(default port of netdata- which you can manualy change in the code by yourself) at the end of the file and so on.
### Steps:
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