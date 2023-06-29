const send_to_topic = (name, topic, value) => {
    post("/api/topic/pub", { topic: topic, value: value });
}

const send_from_input = (name, topic, input_id) => {
    send_to_topic(name, topic, document.getElementById(input_id).value);
}

const toggle_topic = (name, toggle_display, toggle_values, topic) => {
    let btn = document.getElementById(name);
    if ("toggle_current_index" in btn.dataset) {
        btn.dataset.toggle_current_index = parseInt(btn.dataset.toggle_current_index) + 1;
        if (btn.dataset.toggle_current_index > toggle_display.length - 1) btn.dataset.toggle_current_index = 0;
    }
    else btn.dataset.toggle_current_index = 1;
    btn.innerText = toggle_display[btn.dataset.toggle_current_index];
    send_to_topic(name, topic, toggle_values[btn.dataset.toggle_current_index])
}