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
    

    // document.body.appendChild(lists);
    
    // contents = document.getElementById(index);
    // let nameText = document.getElementById("contents");
    // contents.innerText = nameText.value;


    
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";  // これでチェックボックスになります
    checkbox.setAttribute("class","checkbox");
    checkbox.setAttribute("id",index);
    lists.appendChild(checkbox);




    
    let nametext = document.getElementById("contents");
    const textSpan = document.createElement("span");
    textSpan.innerText = nametext.value;
    lists.appendChild(textSpan);



    

    const delete_button = document.createElement("button")
    // delete_button.value = "削除";
    delete_button.innerText = "削除"
    delete_button.setAttribute("id","delete");
    lists.appendChild(delete_button); 


    const edit_button = document.createElement("button")
    // edit_button.value = "編集";
    edit_button.innerText = "編集"
    edit_button.setAttribute("id","edit");
    lists.appendChild(edit_button);



    const hr = document.createElement("hr");
    lists.appendChild(hr);


    document.body.appendChild(lists);

    // contents = document.getElementById(index);
    // let nameText = document.getElementById("contents");
    // contents.innerText = nameText.value;

    

}







// function create_todo_lists() {
    
//     index +=1;
    
//     let lists = document.createElement("div");
//     lists.setAttribute("id", index);
    
//     let nameText = document.getElementById("contents");
//     lists.innerText = nameText.value;
    
//     // ボタンをdivの中に追加
//     const delete_button = document.createElement("button");
//     delete_button.innerText = "削除";
//     delete_button.classList.add("delete-button");  // classに変更
    
//     const edit_button = document.createElement("button");
//     edit_button.innerText = "編集";
//     edit_button.classList.add("edit-button");  // classに変更
    
//     lists.appendChild(delete_button);
//     lists.appendChild(edit_button);
    
//     const hr = document.createElement("hr");
//     lists.appendChild(hr);
    
//     document.body.appendChild(lists);
// }
checkButton = document.getElementsByClassName("checkbox");

checkButton.addEventListener("click",() => {
    create_todo_lists();
    all_tasks = document.getElementById("all_tasks");

    all_tasks.innerHTML = index;
}

)

