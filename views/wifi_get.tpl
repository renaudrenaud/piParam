<!DOCTYPE html>
<html>
    <head>
        <style>
            body {
              font-family: 'Courier New', monospace;
            }
            </style>
        <title>Audiofolies-Squeezelite</title>
    </head>

    <body>
        <h2>Wifi detected params</h2>
        <p>
            <hr>
            % for one_ssid in wifi_detected:
                {{one_ssid}}<br>
            % end
        </p>
        <hr>
        
        <form method="POST" action="/squeezelite">
            wifi_name: <input name="enter the DAC name" type="text" />
            <input type="submit" />
          </form>'
    </body>
</html>