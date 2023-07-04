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
    let text_item = document.getElementById(data.item);
    if (!text_item.dataset["origin"]) text_item.dataset.origin = text_item.innerText;
    if (data.item) {
        switch (text_item.dataset.update_method){
            case 'rewrite':
                text_item.innerText = data.data
                break;
            case 'add':
                text_item.innerText = text_item.dataset.origin + data.data
                break;
            case 'counter':
                // !!! //
                text_item.innerText = parseInt(text_item.innerText) + parseInt(data.data);
                break;
            case 'counter_add':
                if (text_item.innerText === text_item.dataset.origin)
                    text_item.innerText = text_item.dataset.origin + data.data;
                else
                    text_item.innerText = text_item.dataset.origin + (parseInt(text_item.innerText.replace(text_item.dataset.origin, "")) + parseInt(data.data));
        }
    }
        
});