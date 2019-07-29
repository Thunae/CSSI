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

let currentlily = 1;
const lilPad2 = document.querySelector('#lilypad2');
const lilPad1 = document.querySelector('#lilypad1');
const lilPad3 = document.querySelector('#lilypad3');
const lilPad4 = document.querySelector('#lilypad4');
const lilPad5 = document.querySelector('#lilypad5');
const frogger = document.querySelector('#frog');
hopCounter = 0;
function activatePad(name){
  name.classList.add('active');
}
function deActivate(name){
  name.classList.remove('active');
}
frogger.addEventListener('click', (event) => {
    console.log("hop");
    hopCounter++;
    if(hopCounter == 1){
      frogger.style.left = "33.5%";
      frogger.style.top = "22%";
      lilPad2.classList.add('active');
      lilPad1.classList.remove('active');
    }
    if(hopCounter == 2){
      activatePad(lilPad3);
      deActivate(lilPad2);
      frogger.style.left = "450px";
      frogger.style.top = "390px";
    }
    if(hopCounter == 3){
      activatePad(lilPad4);
      deActivate(lilPad3);
      frogger.style.left = "600px";
      frogger.style.top = "600px";
    }
    if(hopCounter == 4){
      activatePad(lilPad5);
      deActivate(lilPad4);
      frogger.style.left = "750px";
      frogger.style.top = "390px";
    }
});
var size = 80;
frogger.addEventListener('mouseover', (event) =>{
  frogger.style.height = size + "px";
  frogger.style.width = size + "px";
});
frogger.addEventListener('mouseout', (event) =>{
  frogger.style.height = "60px";
  frogger.style.width = "60px";
});

document.addEventListener('keydown', (event) =>{
  console.log(event);
  if(event.key === ' '){
    console.log("Spacebar pressed");
    frogger.style.left = "150px";
    frogger.style.top = "380px";
    deActivate(lilPad2);
    deActivate(lilPad3);
    deActivate(lilPad4);
    deActivate(lilPad5);
    activatePad(lilPad1);
    hopCounter = 0;
  }
});
