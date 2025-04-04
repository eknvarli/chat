var copyButton = document.querySelector('#copybutton')
copyButton.addEventListener('click', () => {
    var copyText = document.querySelector('#copylink')
    copyText.select()
    copyText.setSelectionRange(0, 99999)

    navigator.clipboard.writeText(copyText.value)
    alert('Link copied.')
})