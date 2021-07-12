const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/ftp/'
);

const chunk_size = 1024;

chatSocket.onmessage = function(e) {
    console.log('receiving image from server')
    console.log(`e : ${typeof(e.data)}`)
    let div_box = document.getElementById('box');
    let num_user = document.getElementById('user-count');
    if (typeof(e.data) === 'string')
    {
        var message = JSON.parse(e.data);
        console.log(`message: ${JSON.stringify(message)}`);
        var node = document.createElement("P")
        var text = document.createTextNode(message.message + "\n");
        node.appendChild(text);
        div_box.appendChild(node); 

        document.querySelector('#user-count').innerHTML = "Users in room: " + message.count
    }
    else
    {
        let temp_image = e.data
        var uri = URL.createObjectURL(temp_image);
        var img = new Image();
        var br_tag = document.createElement('br');

        img.src = uri;
        // document.body.appendChild(img);
        let node1=document.createElement("a");
        node1.setAttribute("href", uri);
        node1.innerHTML = "some image";
        node1.setAttribute("download", "some image.jpg")
        div_box.appendChild(node1);
        div_box.appendChild(br_tag)
    }
 
}

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};


document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    let files = document.getElementById('file-input').files[0];
    console.log(`File: ${files}`)
    var reader = new FileReader();
    var rawdata = new ArrayBuffer();
    reader.loadend = function(){}
    reader.onload = function(e) {
        // send user data first to show who is sending data
        const messageInputDom = document.querySelector('#chat-message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message,
        }));

        rawData = e.target.result;
        // send image data
        chatSocket.send(rawData);

        alert("the File has been transferred.")

        document.getElementById('file-input').value=""
    }
    if (files!== undefined)
        reader.readAsArrayBuffer(files);
    else
    {
        const messageInputDom = document.querySelector('#chat-message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message,
        }));
        messageInputDom.value = '';      
    }
};