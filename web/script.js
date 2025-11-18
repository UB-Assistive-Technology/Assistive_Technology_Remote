// Power button 
document.querySelector('.power-btn').addEventListener('click', function powerButtonHandler(){
    eel.send_data("P");
});

// Volume buttons
document.querySelector('.volume-plus-btn').addEventListener('click', function volumePlusHandler(){
    eel.send_data("+");
});

document.querySelector('.volume-minus-btn').addEventListener('click', function volumeMinusHandler(){
    eel.send_data("-");
});

// Channel buttons 
document.querySelector('.channel-up-btn').addEventListener('click', function channelUpHandler(){
    eel.send_data("U");
});

document.querySelector('.channel-down-btn').addEventListener('click', function channelDownHandler(){
    eel.send_data("D");
});
