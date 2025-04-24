// let a = +prompt("input number");
// if (a==0) {
//    alert("=0");
// }
// else if(a>0){
//    alert(">0");
// }
// else {
//    alert("<0");
// }

// let day = prompt("введите дни недели");
// if (day == "понедельник") {
//   alert("Пн");
// } else if (day == "Вторник") {
//   alert("Вт");
// } else if (day == "Среда") {
//   alert("Ср");
// } else if (day == "Четверг") {
//   alert("Чт");
// } else if (day == "Пятница") {
//   alert("Пт");
// } else if (day == "Суббота") {
//   alert("Сб");
// } else if (day == "Воскресение") {
//   alert("Вс");
// } else {
//   alert("incorrect");
// }
// ==
// switch (day) { сравнение на равенство
//   case "понедельник":
//     alert("пн");
//     break;
//   case "Вторник":
//     alert("вт");
//     break;
// .........
//   default:
//     alert("incorrect");
// }

// let age = +prompt("input age");
// if (age > 120) {
//   alert("incorrect");
// } else if (age < 0) {
//   alert("incorrect");
// } else {
//   alert("correct");
// }

// let hours = +prompt("input hours");
// let minutes = +prompt("input minutes");
// let seconds = +prompt("input seconds");
// if (hours > 24) {
//   alert("incorrect");
// } if (hours < 0) {
//   alert("incorrect");
// } if (minutes > 60) {
//   alert("incorrect");
// } if (minutes < 0) {
//   alert("incorrect");
// } if (seconds > 60) {
//   alert("incorrect");
// } if (seconds < 0) {
//   alert("incorrect");
// } else {
//   alert("correct");
// }

// let a = +prompt("input a");
// let b = +prompt("input b");
// a > b ? alert("a") : alert("b")

// let a = +prompt("input a");
// let b = +prompt("input b");
// let sign = +prompt("input +-*/");
// switch (sign) {
//   case "+":
//     alert("a+b= ", a + b);
//     break;
//   case "-":
//     alert("a-b= ", a - b);
//     break;
//   case "*":
//     alert("a*b= ", a * b);
//     break;
//   case "/":
//     alert("a/b= ", a / b);
//     break;
//   default:
//     alert("incorrect");
// }

// let count=0;
// while (count < 10) {
//    console.log(count++);
// }

// let count = 0;
// do {
//    let num = +prompt("введите число");
//    count++;
// }while(num!=0) {
// console.log(count)
// }

// let symbol = "#";
// let a = +prompt("введите количество раз");
// while (a > 0) {
//    console.log(symbol);
//    a--;
// }

// let num = +prompt("введите число");
// while (num > 0) {
//   console.log(num--);
// }

let num = +prompt("введите число");
let num1 = +prompt("введите степень");
let s = 1;
while (s == num) {
  console.log((s *= num1));
}
