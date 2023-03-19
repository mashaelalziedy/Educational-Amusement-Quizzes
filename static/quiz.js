
function shuffle(array) {
    let currentIndex = array.length,  randomIndex;

    // While there remain elements to shuffle
    while (currentIndex != 0) {

        // Pick a remaining element
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element
        [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }

    return array;
}

function func(ques, ans, rightAns){
    return ques, ans, rightAns;
}


let questions = [];
for (let i = 0; i < 10; i++){
    if (i==0){
        let answers = [ans[i*(i+1) + i], ans[i*(i+1) + (i+1)], ans[i*(i+1) + (i+2)], ans[i*(i+1) + (i+3)]];
        newAns = shuffle(answers);
        questions.push({
            id: i+1,
            question: ques[i],
            answer: rightAns[i],
            options: [
                newAns[0],
                newAns[1],
                newAns[2],
                newAns[3]
              ]
          });
    }
    else if(i==1){
        let answers = [ans[i*(i+1) + (i+1)], ans[i*(i+1) + (i+2)], ans[i*(i+1) + (i+3)], ans[i*(i+1) + (i+4)]];
        newAns = shuffle(answers);
        questions.push({
            id: i+1,
            question: ques[i],
            answer: rightAns[i],
            options: [
                newAns[0],
                newAns[1],
                newAns[2],
                newAns[3]
              ] 
          });
    }
    else {
        let answers = [ans[i*3 + i], ans[i*3 +(i+1)], ans[i*3 +(i+2)], ans[i*3 +(i+3)]];
        newAns = shuffle(answers);
        questions.push({
          id: i+1,
          question: ques[i],
          answer: rightAns[i],
          options: [
            newAns[0],
            newAns[1],
            newAns[2],
            newAns[3]
            ] 
        });
    }
    };

let question_count = 0;
let points = 0;


window.onload = function(){
    show(question_count);
};

// console.log(questions[question_count].answer);

function show(count){
    let question = document.getElementById("questions");
    let[first, second, third, fourth] = questions[count].options;

    question.innerHTML = `<h2>${questions[count].question}</h2>
    <ul class="option_group">
    <li class="option">${first}</li>
    <li class="option">${second}</li>
    <li class="option">${third}</li>
    <li class="option">${fourth}</li>
    </ul>`;
    toggleActive();  
}

function toggleActive(){
    let option = document.querySelectorAll("li.option");
    for(let i=0; i < option.length; i++){
        option[i].onclick = function(){
            for(let i=0; i < option.length; i++){
                if(option[i].classList.contains("active")){
                    option[i].classList.remove("active");
                }
            }
            option[i].classList.add("active");
        }
    }
}
function next(){


let user_answer = document.querySelector("li.option.active").innerHTML;

if(user_answer == questions[question_count].answer){
    points += 1;
    sessionStorage.setItem("points",points);
}
if(question_count == questions.length -1){
    location.href = "score.html";
    countDagree = localStorage.getItem("count");
    if(countDagree != null){
        localStorage.removeItem('count');
        localStorage.setItem("count", points);
    }else{
        localStorage.setItem("count", points);
    }

    
}
console.log(points);

question_count++;
show(question_count);
}
let user_points = sessionStorage.getItem("points");

document.querySelector("span.points").innerHTML = user_points;

