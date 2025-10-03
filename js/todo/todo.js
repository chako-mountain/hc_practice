
let msg = document.getElementById("msg");

let checkButton = document.getElementById('checkButton');
checkButton.addEventListener('click', create_todo_lists);

index = 0;
checked_task = 0;
task_count = 0;


function create_todo_lists() {
    
    index +=1;

    task_count += 1;
    
    let lists = document.createElement("div");
    lists.setAttribute("id",index);
    




    
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";  // これでチェックボックスになります
    checkbox.setAttribute("class","checkbox");
    // checkbox.setAttribute("id",index);

    checkbox.addEventListener("click", () => {
        // console.log("チェックボックスがクリックされた");
        console.log(index);

        // checkbox = document.getElementById(index);
        if (checkbox.checked) {
            console.log("チェックされました");
            checked_task += 1;
            console.log(checked_task);

        } else {
            console.log("チェックが外されました");
            checked_task -= 1;
            console.log(checked_task);
        }

        document.getElementById("checked_tasks").innerHTML = checked_task;
        document.getElementById("not_checked_tasks").innerHTML = index-checked_task;
        





    });
    lists.appendChild(checkbox);




    
    let nametext = document.getElementById("contents");
    const textSpan = document.createElement("span");
    textSpan.innerText = nametext.value;
    lists.appendChild(textSpan);



    

    const delete_button = document.createElement("button")
    // delete_button.value = "削除";
    delete_button.innerText = "削除"
    delete_button.setAttribute("id","delete");


    delete_button.addEventListener("click", (event) => {
    // console.log("チェックボックスがクリックされた");
        console.log(index);

        const parent = event.target.parentElement; // ボタンの親要素を取得
        // const parentId = parent.id; // 親要素の id を取得

        parent.remove();

        // delete_element = document.getElementById(index);
        // delete_element.remove();

        // task_count -= 1;



 

    });


    lists.appendChild(delete_button); 


    const edit_button = document.createElement("button")
    // edit_button.value = "編集";
    edit_button.innerText = "編集"
    edit_button.setAttribute("id","edit");


    delete_button.addEventListener("click", (event) => {

        const form = document.createElement("form");
        form.setAttribute("id", index); // 必要ならIDなどを設定
        
        const input = document.createElement("input");
        input.setAttribute("type", "text");

        form.appendChild(input);

    });


    lists.appendChild(edit_button);



    const hr = document.createElement("hr");
    lists.appendChild(hr);

    document.body.appendChild(lists);


    task_sum = document.getElementById("task_sum");
    task_sum.innerHTML = task_count;



    // task_sum = document.getElementById("checked_tasks");
    // task_sum.innerHTML = checked_task;





}




// checkButton = document.getElementsByClassName("checkbox");

// checkButton.addEventListener("click",() => {
//     create_todo_lists();
//     all_tasks = document.getElementById("all_tasks");

//     all_tasks.innerHTML = index;
// })

// checkbox = document.querySelectorAll(".checkbox");
// console.log("called");
// console.log(checkButton);

// checkbox.forEach((box) => {
//     box.addEventListener("click",()=> {
//         console.log("チェックボックスがクリックされた");
//     });
// });