const setColor = document.querySelector(".page-content")

setColor.addEventListener("click", (evt) => {
  const color = evt.target.className;
  document.body.classList = "";
  document.body.classList.add(color);
})