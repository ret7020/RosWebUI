const send_to_topic = (topic, value) => {
    console.log(topic);
    console.log(value);
    post("/api/topic/pub", { topic: topic, value: value });
}

const send_from_input = (topic, input_id) => {
    send_to_topic(topic, document.getElementById(input_id).value);
}