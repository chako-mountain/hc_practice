// console.log("hello");

// const { createElement } = require("react");

// function todo_contents_cubmit() {
//     let contents = document.getElementById("todo_contents");

//     console.log(contents.value);

// }

// todo_contents_cubmit();


// const button = document.getElementById("add-button");
// button.addEventListener("click", function () {
//   console.log("ボタンがクリックされました！");
// });

// function butotnClick(){
//   msg.innerText = 'お名前は' + nameText.value + 'さんですね';
// }

// let nameText = document.getElementById("contents");
let msg = document.getElementById("msg");

let checkButton = document.getElementById('checkButton');
checkButton.addEventListener('click', create_todo_lists);

index = 0;


function create_todo_lists() {
    
    index +=1;
    
    let lists = document.createElement("div");
    lists.setAttribute("id",index);
    

    document.body.appendChild(lists);
    
    contents = document.getElementById(index);
    let nameText = document.getElementById("contents");
    contents.innerText = nameText.value
    
    const hr = document.createElement("hr");
    lists.appendChild(hr);

    

    const delete_button = document.createElement("button")
    document.body.appendChild(delete_button);
    delete_button.value = "削除";
    delete_button.setAttribute("id","delete");

    const edit_button = document.createElement("button")
    document.body.appendChild(edit_button);
    edit_button.value = "削除";
    edit_button.setAttribute("id","edit");


    

    


    

    

}


