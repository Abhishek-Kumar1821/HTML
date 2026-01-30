
//Header title change
var headerTitle = document.getElementById('header-title');
headerTitle.textContent = "Ajit Kumar Sharma";
//tagline change
var tagline = document.getElementById('tagline');
tagline.textContent = "Department of BCA";
//Header border style change
var header = document.getElementById('header');
header.style.borderBottom = "5px solid #F00";
//list item modifications
var items = document.getElementsByClassName('list-item');
//text change
items[0].textContent = "BCA";
items[1].textContent = "Physics";

//style change

items[0].style.backgroundColor = "yellow";
items[1].style.color = "red";

//All li background


var li = document.getElementsByTagName('li');
for (var i = 0; i < li.length; i++) {
    li[i].style.backgroundColor = "lightyellow";
};
    