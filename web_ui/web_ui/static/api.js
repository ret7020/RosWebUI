async function post(endpoint, data){
    return await fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'applciation/json',
            'Accept': 'applciation/json'
        },
        body: JSON.stringify(data)
    })
}