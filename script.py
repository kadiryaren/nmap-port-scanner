import json 
import subprocess
import sys

args = sys.argv

p = args[args.index("-p")+1]
u = args[args.index("-u")+1]
s = args[args.index("-s")+1]

EXAMPLE_OUTPUT = """Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-29 17:35 Turkey Standard Time
Stats: 0:00:10 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Stats: 0:00:10 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Nmap scan report for testphp.vulnweb.com (44.228.249.3)
Host is up (0.030s latency).
rDNS record for 44.228.249.3: ec2-44-228-249-3.us-west-2.compute.amazonaws.com

PORT   STATE SERVICE
80/tcp open  http
| http-sql-injection:
|   Possible sqli for queries:
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/artists.php?artist=1%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/artists.php?artist=3%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/artists.php?artist=2%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/showimage.php?file=%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/listproducts.php?cat=1%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/listproducts.php?cat=4%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/listproducts.php?cat=3%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/listproducts.php?cat=2%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/listproducts.php?artist=1%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|     http://testphp.vulnweb.com:80/search.php?test=query%27%20OR%20sqlspider
|_    http://testphp.vulnweb.com:80/listproducts.php?artist=3%27%20OR%20sqlspider

Nmap done: 1 IP address (1 host up) scanned in 18.59 seconds"""


string = str(subprocess.check_output(f"nmap -p {p} --script {s} {u}", shell=True))

liste = []

for i in string.split('|'):
    if(i.strip()[:4] == 'http' or i.strip()[:4] == '_    '):
        if(i.strip() == 'http-sql-injection: \\n'):
            pass
        else:
            if(i.strip()[:4] == '_    '):
                liste.append(i.strip()[4:-2])
            else:
                liste.append(i.strip()[:-2])
                

if(len(liste) == 0):
    print("No Results")
    exit()

export_list = [{"Nmap command": f"nmap -p {p} --script {s} {u}" }]

for url in liste:
    export_list.append({"Url": url})

with open('json_data.json', 'w') as outfile:
    json.dump(export_list, outfile)

