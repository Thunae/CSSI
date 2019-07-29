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
let positive = ["It is certain", "It is decidely so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it", "Most Likely", "Outlook Good", "Yes", "Signs Point to yes"];
let negative = ["Don't count on it", "My Reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"];
let nonCommittal = ["Reply Hazy", "Try Again", "Ask Again Later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"];
var answerNum;
const answer = document.querySelector('#answer');
function changeText(quote){
  answer.innerHTML = quote;
}
function chooseAnswer(){
  answerNum = Math.floor(Math.random() * 3) + 1;
  console.log(answerNum);
}
const ball = document.querySelector('#ball');
ball.addEventListener('click', (event) =>{
chooseAnswer();
var displayNum = 0;

if(answerNum == 1){
  //Positive Answer
  displayNum = Math.floor(Math.random() * positive.length);
  console.log(positive[displayNum]);
  changeText(positive[displayNum]);
} else if(answerNum == 2){
 //Negative Answer
 displayNum = Math.floor(Math.random() * negative.length);
 console.log(negative[displayNum]);
 changeText(negative[displayNum]);
} else if(answerNum == 3){
 //Indifferent Answer
 displayNum = Math.floor(Math.random() * nonCommittal.length);
 console.log(nonCommittal[displayNum]);
 changeText(nonCommittal[displayNum]);
}
});
