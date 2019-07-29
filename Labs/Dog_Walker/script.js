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

// Task 1
const dogName1 = "Steve";
const dogType1 = "beagle";

// Complete Task 1 Below
console.log("I will walk " + dogName1 + " " + "at 12 PM");


const dogName2 = "Joe";
const dogType2 = "bulldog";

// Complete Task 2 Below
if(dogType2 === "corgi"){
  console.log("I will walk " + dogName2 + " " + "at 12 PM today.");
}else{
  console.log("I will walk " + dogName2 + " " + "at 1 PM today.");
}


const dogName3 = "Lola";
const dogType3 = "poodle";
printMsg(dogName3, dogType3);

function favDog(name){
  if((name == "spike") || (name == "jeremy") || (name == "lola") || (name == "peaches") || ("steve")){
    return true;
  }else{
    return false;
  }
}
function printMsg(name, dogType){
  console.log("I will walk " + name + " at " + getTime(dogType));
}
function getTime(dogType){
  if((dogType == "corgi") || (dogType == "beagle")){
    return "12pm";
  }
  else if((dogType3 == "bulldog")){
    return "1pm";
  } else {
    return "2pm";
  }
}

// Complete Task 3 Below
