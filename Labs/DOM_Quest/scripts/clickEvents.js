// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("Running Click Events Script");
const box1 = document.querySelector('#box1');
const box2 = document.querySelector('#box2');
const box3 = document.querySelector('#box3');
const box4 = document.querySelector('#box4');
const box5 = document.querySelector('#box5');
const box6 = document.querySelector('#box6');
console.log(box6.style.color);
const boxes = document.querySelectorAll('.box');
boxes.forEach((box)=>{
  box.addEventListener('click', (event) => {
      var colorBox = window.getComputedStyle(box, null).getPropertyValue("background-color");
      console.log(colorBox);
      box1.style.backgroundColor = colorBox;
      box2.style.backgroundColor = colorBox;
      box3.style.backgroundColor = colorBox;
});
});
