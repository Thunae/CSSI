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

console.log(dataObject);
const firstGifRating = dataObject.data["0"].rating;
const data = dataObject.data;
const button = document.querySelector('button');
button.addEventListener('click', ()=>{
  for(var j = 0; j < (data.length); j++){
    var p = document.createElement("img");
    p.src = dataObject.data[j].source;
    console.log(dataObject.data[j].source);
    document.body.appendChild(p);
  }
});
console.log(data.length);
// var link = dataObject.data["0"].source
// var pic1 = document.createElement("img");
// pic1.src = link;
// document.body.appendChild(pic1);
