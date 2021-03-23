"""
This script to manage few things:
- wifi connection
- dac connection

"""

from bottle import route, run, get, post, template, static_file, request
import cgi
import subprocess

@get('/wifi')
def wifi():
    # using the check_output() for having the network term retrival
    result = subprocess.run(['nmcli','dev','wifi'], text=True,capture_output=True)
    
    wifi_list = []
    for ssid in result.stdout.split("\n"):
        wifi_list.append(ssid.replace(' ','.'))
   
    return template('wifi_get.tpl', wifi_detected = wifi_list)


@get('/squeezelite')
def squeezelite():
    """
    build the GET squeezelite page
    show the /etc/default/squezelite file
    propose to change the DAC

    """  
    
    # grab the squeezelite file
    f = open("/etc/default/squeezelite","r")
    file_lines = f.readlines()

    squeezelines = []
    for line in file_lines:
        # all_lines = all_lines + line + chr(13) + "<br>"
        squeezelines.append(line)
    f.close()

    # grab the list of detected output for squeezelite
    result = subprocess.run(['squeezelite', '-l'], text=True,capture_output=True)

    players=[]
    for line in result.stdout.split("\n"):
        if "-" in line:
            players.append(line.split("-"))

    return template('squeezelite_get.tpl', 
                     squeezefile = squeezelines,
                     squeezeplayers=players)

@post('/squeezelite')
def submit_squeezelite():
    dac_name=request.forms.get("dac_name")
    result = "whaa"
    return dac_name #+ dac_name

run(host='0.0.0.0', port=5151, debug=True, reloader=True)