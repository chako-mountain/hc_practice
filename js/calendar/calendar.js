

const today = new Date(); // 今日の日付を取得
const lastDayOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0); // 当月の翌月の0日を取得
const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth() , 1);

console.log(lastDayOfMonth.getDate());
console.log(lastDayOfMonth.getDay());
console.log(firstDayOfMonth.getDay());

function create_calendar(begin_day,how_many_day) {

    week_day_administrator = begin_day // 2

    beginneg_number = 1 + begin_day*3

    console.log("beginneg_number")
    console.log(beginneg_number)

    console.log("日 月 火 水 木 金 土")

    process.stdout.write(" ".repeat(beginneg_number) + "1");

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
                week_day_administrator += 1



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
                console.log()
                process.stdout.write(" ".repeat(1) + i);



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

// console.log("日 月 火 水 木 金 土")
// console.log(" ".repeat(7) + "1")

// process.stdout.write(" ".repeat(4) + "1");
// process.stdout.write('no line break');