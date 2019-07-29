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

console.log("script is running...");
function myAlarm(time){
  console.log("Hey Ryan, wake up! It's " + time);
}
function momAlarm(time){
  console.log("Hey Mom, wake up! It's " + time);
}
function familyAlarm(name, time){
  console.log("Hey " + name + " wake up! It's " + time);
}
function importantAlarm(message){
  var msg = message.toUpperCase();
  console.log(msg);
}
console.log(importantAlarm("Wake up"));
function snoozeAlarm(time1, time2){
  console.log("The alarm for " + time1 + " has been moved to " + time2);
}
console.log(snoozeAlarm(6, 8));
function extensionProblem(message, numberOfpeople){
  for (var i = 0; i < numberOfpeople; i++){
    console.log(message);
  }
}
extensionProblem("wake up", 25)
