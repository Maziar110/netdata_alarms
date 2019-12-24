import requests
from ipaddress import ip_address


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def host_extractor(ip):
    # We'll develop this method later in order to get all hosts addresses and use them in the project
    ip2 = str(ip).replace("\n", "")
    host_ip = str(ip2) + ":19999"
    return host_ip


def ipEntered(val):
    try:
        return ip_address(val)
    except ValueError:
        print(color.BOLD, color.RED, "Not a valid IP address", color.END)
        return "false"


def Alarm_extractor(alarms_details):
    warning = []
    critical = []
    for items in alarms_details:
        if alarms_details[items]["status"] == "CRITICAL":
            error = alarms_details[items]["info"]
            value = alarms_details[items]["value"]
            alarm = "Error in " + items + ": " + error + " The value is: " + str(value)
            critical.append(alarm)
        elif alarms_details[items]["status"] == "WARNING":
            error = alarms_details[items]["info"]
            alarm = "Error in " + items + ": " + error
            warning.append(alarm)
    return (warning, critical)


def bulk_check():
    file = open("./ip_hosts.txt", "r")
    ips = file.readlines()
    log = open("./netdata.log", "w")
    alarm_req = ""
    info_req = ""

    for ip in ips:

        # To set host automatically, uncomment bellow line:
        host = host_extractor(ip)

        alarms_url = "http://" + host + "/api/v1/alarms"
        info_url = "http://" + host + "/api/v1/info"

        try:
            alarm_req = requests.get(url=alarms_url)
            info_req = requests.get(url=info_url)
            data = alarm_req.json()
            alarms_details = data["alarms"]
        except Exception as e:
            print(color.PURPLE, color.BOLD, "Exception happend: ", color.END, color.CYAN, str(e)
                  , " **Alaram method result:", str(alarm_req))
        try:
            info = info_req.json()
            server_name = info["mirrored_hosts"]
        except Exception as e:
            print(color.PURPLE, color.BOLD, "Exception happend: ", color.END, color.CYAN, str(e)
                  , " and info method result:", str(info_req), color.END)

        try:
            alarms = Alarm_extractor(alarms_details)
            print(color.BOLD, color.BLUE, "Critical errors and Warnings in ", server_name, " with IP: ", host,
                  " is(are):", color.END)
            for warning in alarms[0]:
                print(color.YELLOW, warning, color.END)
            for critical in alarms[1]:
                print(color.RED, critical, color.END)
                log.write("host: " + host +" " +critical+ "\n")
        except Exception as e:
            print(e)

    file.close()
    log.close()


def single_check(ip):
    server_name = ""
    alarm_req = ""
    info_req = ""
    host = host_extractor(ip)

    alarms_url = "http://" + host + "/api/v1/alarms"
    info_url = "http://" + host + "/api/v1/info"

    try:
        alarm_req = requests.get(url=alarms_url)
        info_req = requests.get(url=info_url)
        data = alarm_req.json()
        alarms_details = data["alarms"]
    except Exception as e:
        print(color.PURPLE, color.BOLD, "Exception happend: ", color.END, color.CYAN, str(e)
              , " **Alaram method result:", str(alarm_req))
    try:
        info = info_req.json()
        server_name = info["mirrored_hosts"]
    except Exception as e:
        print(color.PURPLE, color.BOLD, "Exception happend: ", color.END, color.CYAN, str(e)
              , " and info method result:", str(info_req), color.END)
    try:
        alarms = Alarm_extractor(alarms_details)
        print(color.BOLD, color.BLUE, "Critical errors and Warnings in ", server_name, " with IP: ", host, " is(are):",
              color.END)
        for warning in alarms[0]:
            print(color.YELLOW, warning, color.END)
        for critical in alarms[1]:
            print(color.RED, critical, color.END)
    except Exception as e:
        print(e)


user_input = input("Please input your host address- **all** for bulk and **<ip>** to specify desired host IP:")

if str(user_input) == "all":
    bulk_check()

else:
    ip = ipEntered(str(user_input))
    if ip == "false":
        print(color.BOLD, color.BLUE, "Please enter a valid IP")
    else:
        single_check(ip)
