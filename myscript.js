// Heading change using DOM
const heading = document.querySelector("#content h4");
heading.textContent = "Available Courses";

// Select all list items
const listItems = document.querySelectorAll(".list_item");

// Click event on each list item
listItems.forEach(item => {
  item.addEventListener("click", function () {
    alert("You selected: " + this.textContent);
    this.style.backgroundColor = "#aed6f1";
  });
});

// Form handling
const form = document.querySelector("form");
const input = document.querySelector("input[type='text']");
const ul = document.getElementById("items");

document.addEventListener('DOMContentLoaded', () => {
  // Heading change using DOM
  const heading = document.querySelector("#content h4");
  if (heading) heading.textContent = "Available Courses";

  // Select all list items and add click handlers
  const listItems = document.querySelectorAll(".list_item");
  listItems.forEach(item => {
    item.addEventListener("click", function () {
      alert("You selected: " + this.textContent.trim());
      this.style.backgroundColor = "#aed6f1";
    });
  });

  // Form handling
  const form = document.querySelector("form");
  const input = document.querySelector("input[type='text']");
  const ul = document.getElementById("items");

  if (form && input && ul) {
    form.addEventListener("submit", function (e) {
      e.preventDefault(); // stop page reload

      const value = input.value.trim();
      if (value !== "") {
        const newLi = document.createElement("li");
        newLi.className = "list_item";
        newLi.textContent = value;
        newLi.addEventListener("click", function () {
          alert("You selected: " + this.textContent);
          this.style.backgroundColor = "#aed6f1";
        });
        ul.appendChild(newLi);
        input.value = "";
        input.focus();
      }
    });
  }
});