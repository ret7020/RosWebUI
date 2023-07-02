async function post(endpoint, data){
    return await fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(data)
    })
}

const socket = new WebSocket('ws://' + location.host + '/ws');
socket.addEventListener('message', ev => {
    let data = JSON.parse(ev.data);
    if (data.item) document.getElementById(data.item).innerText = data.data

});