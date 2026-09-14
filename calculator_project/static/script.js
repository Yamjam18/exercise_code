function addNumber(num){
    let display = document.getElementById("display");

    if(display.value === "0"){
        display.value = num;
    } else {
        display.value += num;
    }
}

function addOperator(op){
    let display = document.getElementById("display");

    display.value += op;
}

function clearDisplay(){
    document.getElementById("display").value = "0";
}

function toggleSign(){
    let display = document.getElementById("display");

    if(display.value.startsWith("-")){
        display.value = display.value.slice(1);
    } else {
        display.value = "-" + display.value;
    }
}

function percentage(){
    let display = document.getElementById("display");

    let value = parseFloat(display.value);

    display.value = value / 100;
}

function deleteLast(){
    let display = document.getElementById("display");

    if(display.value.length === 1){
        display.value = "0";
    } else {
        display.value = display.value.slice(0, -1);
    }
}

function calculate(){

    let expression = document.getElementById("display").value;

    fetch("/calculate", {
        method: "POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            expression: expression
        })
    })
    .then(response => response.json())
    .then(data =>{
        document.getElementById("display").value = data.result;
    });
}