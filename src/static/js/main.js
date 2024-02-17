
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event){
            var data = JSON.parse(event.data)
            var table = document.getElementById('myTable')
            table.innerHTML = ''
            var text = document.getElementById('message')
            text.innerHTML = ''
            buildTable(data)
            message(data)
            }

            function buildTable(data){
                var table = document.getElementById('myTable')
                for (var i = 0; i < data['bulls_list'].length; i++){
                    var line = `<tr class='tr'>
                                <td class='player_try'> ${data['player_try_list'][i]}</td>
                                <td class='bulls'> ${data['bulls_list'][i]}</td>
                                <td class='cows'> ${data['cows_list'][i]}</td>
                           </tr>`
                           table.innerHTML += line}
               }

            function message(data){
                if (data['message']) {
                var message = document.getElementById('message')
                message.innerHTML = data['message']
            }
            }
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
            const give_up = function() {
                ws.send('give up')
            }
            const new_game = function() {
                ws.send('new game')
            }