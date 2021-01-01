function displayLengthFilter() {
    if (document.getElementById('choice_yes').checked) {
        document.getElementById('lengthBox').style.display = 'block';
    }
    else {
        document.getElementById('lengthBox').style.display = 'none';
    }
}

function displayAlphabetFilter() {
    if (document.getElementById('alphachoice_yes').checked) {
        document.getElementById('alphaBox').style.display = 'block';
    }
    else {
        document.getElementById('alphaBox').style.display = 'none';
    }
}
