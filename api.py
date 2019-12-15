import requests


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


file = open("./ip_hosts.txt", "r")
ips = file.readlines()


def host_extractor(ip):
    # We'll develop this method later in order to get all hosts addresses and use them in the project
    ip2 = str(ip).replace("\n", "")
    host_ip = str(ip2) + ":19999"
    return host_ip


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
        alarms = alarms_details.get("info")

        info = info_req.json()
        server_name = info["mirrored_hosts"]
        for items in alarms_details:
            if alarms_details[items]["status"] == "CRITICAL":
                print(color.BOLD, color.GREEN, "\n", "We have bellow errors for host " + host +
                      " in the section of: " + items, ":", color.END)
                alarms = alarms_details[items]["info"]
                print(color.BOLD, color.RED, alarms, color.END, "\n")

    except Exception as e:
        if alarm_req != "":
            data = alarm_req.json()
            alarms_details = data["alarms"]
            alarms = alarms_details.get("info")

            for items in alarms_details:
                if alarms_details[items]["status"] == "CRITICAL":
                    print(color.BOLD,color.GREEN,"\n", "We have bellow errors for host " + host +
                          " in the section of: " + items, ":", color.END)
                    alarms = alarms_details[items]["info"]
                    print(color.BOLD, color.RED, alarms, color.END, "\n")

        print(color.PURPLE ,color.BOLD,"Exception happend: ",color.END, color.CYAN, str(e)
              , " **Alaram method result:" , str(alarm_req)
                 , " and info method result:" , str(info_req), color.END)

file.close()
