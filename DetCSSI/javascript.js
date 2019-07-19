const button = document.querySelector('button');
button.addEventListener('mouseover', (event) => {
  button.innerHTML = 'Don\'t click!';
  button.classList.add('danger');
});
button.addEventListener('mouseout', (event) => {
  button.innerHTML = "Click Me!";
  button.classList.remove('danger');
});
const randomHexColor = () => {
  return '#' + ('000000' + Math.floor(Math.random() * 16777216)
    .toString(16))
    .slice(-6)
    .toUpperCase();
}
const box = document.querySelector('#box');
setInterval(() =>{
  box.style.backgroundColor = randomHexColor();
}, 100);

// document.addEventListener('mousemove', (event) => {
// box.style.backgroundColor = randomHexColor();
// });
