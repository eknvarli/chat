const userName = JSON.parse(document.getElementById('json-username').textContent)
const roomName = JSON.parse(document.getElementById('json-roomname').textContent)
const messageForm = document.querySelector('#send-message-form')

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + roomName
    + '/'
)

chatSocket.onmessage = (e) => {
    console.log('onmessage')

    const data = JSON.parse(e.data)

    var currentDate = new Date()
    var options = {
        year: 'numeric',
        month: 'short', 
        day: 'numeric', 
        hour: 'numeric', 
        minute: 'numeric', 
        hour12: true 
    }

    var formattedDate = currentDate.toLocaleString('en-US', options);

    if (data.message) {
        let html = '<div class="message-item"><span id="username"><strong>'
        html += data.username
        html += '</strong> &nbsp; <small class="text-secondary">'
        html += formattedDate
        html += '</small></span><br><span id="message">'
        html += data.message
        html += '</span><br></div>'

        document.querySelector('.room-messages').innerHTML += html
    } else {
        alert('The message was empty.')
    }
}

// message submit event
messageForm.addEventListener('submit', (e) => {
    e.preventDefault()

    const messageInput = document.querySelector('#send-message-input')
    const message = messageInput.value

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName
    }))

    messageInput.value = ''
    return false
})