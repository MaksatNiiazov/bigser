const button = document.querySelector('.expand-text button');
const text = document.querySelector('.expand-text p');

// Function to calculate the number of lines
function countLines(element) {
    const lineHeight = parseFloat(getComputedStyle(element).lineHeight);
    const height = element.clientHeight;
    const numberOfLines = Math.ceil(height / lineHeight);
    return numberOfLines;
}

// Check the number of lines on page load
const numberOfLines = countLines(text);

// Hide the button if there are 10 or fewer lines
if (numberOfLines <= 10) {
    button.style.display = 'none';
}

button.addEventListener('click', () => {
    text.classList.toggle('active');
    if (text.classList.contains('active')) {
        button.textContent = 'Скрыть';
    } else {
        button.textContent = 'Читать больше';
    }
});
