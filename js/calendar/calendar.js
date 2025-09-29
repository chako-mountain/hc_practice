


const today = new Date(); // 今日の日付を取得
let lastDayOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0); // 当月の翌月の0日を取得
let firstDayOfMonth = new Date(today.getFullYear(), today.getMonth() , 1);

console.log(lastDayOfMonth.getDate());
console.log(lastDayOfMonth.getDay());
console.log(firstDayOfMonth.getDay());

const args = process.argv
const thirdArg = args[2];

console.log("3番目の引数は:", thirdArg);

if (thirdArg === "-m"){

    // if not (0<=args[3]<=12)

    const currentYear = new Date().getFullYear();

    want_to_month = args[3]

    lastDayOfMonth = new Date(currentYear, want_to_month,0);
    firstDayOfMonth = new Date(currentYear,want_to_month-1,1);



}


function create_calendar(begin_day,how_many_day) {

    week_day_administrator = begin_day + 1 

    beginneg_number = 1 + begin_day*3

    console.log("beginneg_number")
    console.log(beginneg_number)

    console.log("日 月 火 水 木 金 土")

    process.stdout.write(" ".repeat(beginneg_number) + "1");



    if (week_day_administrator === 7) {
        console.log()
        week_day_administrator = 0;
    }


    for (i= 2 ; i <= how_many_day; i++){

        if (i >= 0 && i < 10) {
            if (week_day_administrator === 6) {
                week_day_administrator = 0

                process.stdout.write(" ".repeat(2) + i);
                
                console.log()

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

create_calendar(firstDayOfMonth.getDay(),lastDayOfMonth.getDate())

