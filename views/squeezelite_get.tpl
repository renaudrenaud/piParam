<!DOCTYPE html>
<html>
    <head>
        <link href="/media/examples/link-element-example.css" rel="stylesheet">
        <title>Audiofolies-Squeezelite</title>
    </head>

    <body>
        <h2>Squeezlite local parameters</h2>
        <p>
            <hr>
            % for oneline in squeezefile:
                <li>{{oneline}}</li>
            % end
        </p>
        <hr>
        <h2>Squeezelite detected output</h2>
        <p>
        <table>
            
                % for player in squeezeplayers:
                <tr>
                    <td>{{player[0]}}</td><td>{{player[1] or "none"}}</td>
                    % end
                </tr>
        </table>
        </p>
        <form method="POST" action="/squeezelite">
            enter the dac name: <input name="dac_name" type="text" />
            <input type="submit" />
          </form>'
    </body>
</html>