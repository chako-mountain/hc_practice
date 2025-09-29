


const today = new Date(); // 今日の日付を取得
const lastDayOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0); // 当月の翌月の0日を取得
const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth() , 1);

console.log(lastDayOfMonth.getDate());
console.log(lastDayOfMonth.getDay());
console.log(firstDayOfMonth.getDay());

const args = process.argv
const thirdArg = args[2];
// console.log("3番目の引数は:", thirdArg);

// if (thirdArg === "-m"){
//     want_to_month = args[3]

//     lastDayOfMonth = new Date(currentYear, want_to_month-1,0);
//     first




// }


function create_calendar(begin_day,how_many_day) {

    week_day_administrator = begin_day + 1 

    beginneg_number = 1 + begin_day*3

    console.log("beginneg_number")
    console.log(beginneg_number)

    console.log("日 月 火 水 木 金 土")

    process.stdout.write(" ".repeat(beginneg_number) + "1");

    const todayDate = today.getDate();

    if (week_day_administrator === 7) {
        console.log()
        week_day_administrator = 0;
    }


    for (i= 2 ; i <= how_many_day; i++){
        // console.log(" ".repeat(beginneg_number));
        // console.log(i)
        // console.log(" ".repeat(3))

        if (i >= 0 && i < 10) {
            if (week_day_administrator === 6) {
                week_day_administrator = 0

                process.stdout.write(" ".repeat(2) + i);
                
                console.log()

                
                // process.stdout.write(" ".repeat(1) + i);
                // week_day_administrator += 1
            }
            else if(week_day_administrator === 0) {
                process.stdout.write(" ".repeat(1) + i);
                week_day_administrator += 1
            }
            else{
                process.stdout.write(" ".repeat(2) + i);
                week_day_administrator += 1

            }
            
            

        }
        else {
            // if (week_day_administrator === 6) {
            //     week_day_administrator = 0
            //     console.log()

            // }

            // // if(week_day_administrator === 0) {
            // //     process.stdout.write(i);
            // //     week_day_administrator += 1
            // // }
            
            // process.stdout.write(" ".repeat(1) + i);
            // week_day_administrator += 1

            if (week_day_administrator === 6) {
                week_day_administrator = 0
                
                process.stdout.write(" ".repeat(1) + i);
                console.log()



            }

            else if(week_day_administrator === 0) {
                process.stdout.write(" ".repeat() + i);
                week_day_administrator += 1
            }
            else{
                process.stdout.write(" ".repeat(1) + i);
                week_day_administrator += 1

            }

        }

       



    }
    
    
}

create_calendar(lastDayOfMonth.getDay(),lastDayOfMonth.getDate())


create_calendar(6,30)

// console.log("日 月 火 水 木 金 土")
// console.log(" ".repeat(7) + "1")

// process.stdout.write(" ".repeat(4) + "1");
// process.stdout.write('no line break');





// const reset = "\x1b[0m";
// const bgWhite = "\x1b[47m";
// const fgBlack = "\x1b[30m";

// const todayDate = today.getDate();

// function writeDay(i, spaceCount) {
//     let dayStr = " ".repeat(spaceCount) + i;
//     if (i === todayDate) {
//         dayStr = bgWhite + fgBlack + dayStr + reset;
//     }
//     process.stdout.write(dayStr);
// }

// // ループ内の例
// if (week_day_administrator === 6) {
//     week_day_administrator = 0;
//     console.log();
//     writeDay(i, 1);  // スペース1つ＋日付出力（背景色判定含む）
//     week_day_administrator += 1;
// } else if (week_day_administrator === 0) {
//     writeDay(i, 1);
//     week_day_administrator += 1;
// } else {
//     writeDay(i, 2);
//     week_day_administrator += 1;
// }

// console.log(process.argv);

// // 実際の引数だけを取り出す（先頭2つを除く）
// const args = process.argv.slice(2);

// console.log("コマンドライン引数:", args);
