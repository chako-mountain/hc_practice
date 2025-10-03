
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

        result = window.confirm("本当に削除しますか？");

        if(result) {

            const parent = event.target.parentElement; // ボタンの親要素を取得
        // const parentId = parent.id; // 親要素の id を取得

             parent.remove();

        // delete_element = document.getElementById(index);
        // delete_element.remove();

        // task_count -= 1;

        }

        



 

    });


    lists.appendChild(delete_button); 


    const edit_button = document.createElement("button")
    // edit_button.value = "編集";
    edit_button.innerText = "編集"
    edit_button.setAttribute("id","edit");
    edit_state = "no_edit"


    edit_button.addEventListener("click", (event) => {

        

        if(edit_state == "no_edit"){

            id = event.target.parentElement.id;

            text_contents = document.getElementById(id).querySelector("span").innerHTML;
            console.log(text_contents);

            document.getElementById(id).querySelector("span").innerHTML = ""





            const form = document.createElement("form");
            form.style.display = "inline"; 
            form.setAttribute("class", id); 
    
            
            const input = document.createElement("input");
            input.setAttribute("type", "text");
            input.value = text_contents;

            form.appendChild(input);

            document.getElementById(id).querySelector("span").replaceWith(form);

            // event.target.parentElement.appendChild(form);

            edit_button.innerText = "更新"

            edit_state = "on_edit";
            console.log(edit_state);

        }

        else {
            console.log("else is called");
            id = event.target.parentElement.id;
            text_contents = document.getElementById(id).querySelector("form").querySelector("input").value;
            console.log(text_contents);

            

            // span.replaceWith(form);

            // document.getElementById(id).querySelector("form").remove();

            // document.getElementById(id).querySelector("span").innerHTML = text_contents;

            new_content = document.createElement("span");
            new_content.innerHTML = text_contents;

            document.getElementById(id).querySelector("form").replaceWith(new_content);

            edit_state = "no_edit";

            edit_button.innerText = "編集"




        }

    });





    // edit_button.addEventListener("click", (event) => {
    //     const parent = event.target.parentElement;

    //     // 既に form があるか確認（＝編集モードかどうか）
    //     const existingForm = parent.querySelector("form");
    //     const span = parent.querySelector("span");

    //     if (!existingForm && span) {
    //         // 編集モードに入る

    //         const text_contents = span.innerText;

    //         // フォームを作って span を置き換える
    //         const form = document.createElement("form");
    //         const input = document.createElement("input");
    //         input.type = "text";
    //         input.value = text_contents;

    //         form.appendChild(input);
    //         span.replaceWith(form);  // span を form に置き換える

    //     } else if (existingForm) {
    //         // 編集完了：form → span に戻す
    //         const inputValue = existingForm.querySelector("input").value;

    //         const newSpan = document.createElement("span");
    //         newSpan.innerText = inputValue;

    //         existingForm.replaceWith(newSpan);  // form を span に置き換える
    //     }
    // });


    // edit_button.addEventListener("click", (event) => {
    //     const parent = event.target.parentElement;  // 編集ボタンの親div
        
    //     const existingForm = parent.querySelector("form.edit-form");
        
    //     if (existingForm) {
    //         // フォームが既にある => 編集完了として値を反映する
            
    //         const input = existingForm.querySelector("input[type='text']");
    //         const newValue = input.value.trim();
            
    //         // フォームを削除
    //         existingForm.remove();
            
    //         // spanがあれば更新、なければ新規作成して親に追加
    //         let textSpan = parent.querySelector("span");
    //         if (!textSpan) {
    //             textSpan = document.createElement("span");
    //             parent.insertBefore(textSpan, event.target); // 編集ボタンの前に追加
    //         }
    //         textSpan.innerText = newValue;
            
    //     } else {
    //         // 編集フォームがない => 新規にフォームを表示
            
    //         const textSpan = parent.querySelector("span");
    //         if (!textSpan) return; // テキストがなければ何もしない
            
    //         const text_contents = textSpan.innerText;
            
    //         // spanをフォームに置き換える
    //         const form = document.createElement("form");
    //         form.setAttribute("class", "edit-form");
            
    //         const input = document.createElement("input");
    //         input.setAttribute("type", "text");
    //         input.value = text_contents;
            
    //         form.appendChild(input);
    //         textSpan.replaceWith(form);
    //     }
    // });



    lists.appendChild(edit_button);



    const hr = document.createElement("hr");
    lists.appendChild(hr);
    // parent.insertBefore(form, hr);

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