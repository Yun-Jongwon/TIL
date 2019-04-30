// 반복

// let i = 0
// while (i<10) {

//     console.log(i)
//     i++
// }

// // 반복 2- for
// for (let j=0; j<10; j++){
//     console.log(j)
// }
// // 반복 3 - for of
// for (let number of [1,2,3,4,5]){//const 선언 가능 
//     console.log(number)
// }








// // Array(배열)
// const numbers=[1,2,3,4]

// console.log(numbers[0])
// console.log(numbers[-1]) // 음수값 인덱스는 불가능
// numbers.length // 배열 길이
// numbers.reverse()// 배열뒤집기
// numbers.push('a') //배열 길이가 출력됨
// numbers.pop()
// numbers.unshift('a') //앞에다가 넣기
// numbers.shift() // 맨 앞에 있는 원소 빼내기
// numbers.includes(1) // 배열에 값이 있는지 확인 -->있으면 True
// numbers.indexOf('a')// 값의 인덱스 찾기 , 여러 개 있으면 가장 앞에 있는 값의 인덱스, 없의면 -1 리턴
// numbers.join()// 배열을 string, 기본은 쉼표가 사이에 들어감
// numbers.slice(2,4)// 배열 자르기, 숫자 하나만 넣으면 그 인덱스 부터 끝까지

// //object(phython의 dictionary)
// const me={
//     name: 'nwith',
//     'phonenumber':'01012345678',
//     appleProducts:{
//         ipad:true,
//         iphone:'x'

//     }
// }



// me.appleProducts// .으로도 불러 올 수 있음


// //JSON -Java Script Object Notation(JS 객체 표기법)

// JSON.stringify()//Object->JSON String
// JSON.parse()// JSON String -> Object

// const jsonData = JSON.stringify(me)
// const parseData=JSON.parse(jsonData)
// typeof jsonData





//함수 
// 방법1.선언식
function add (num1, num2){
    return num1+num2
}
console.log('add: '+add(1,2))

// 방법2. 표현식
const sub=function(num1,num2){
    return num1 - num2
}
console.log('sub: '+sub(3,4))

// Arrow Function
const mul=(num1,num2)=>{
    return num1*num2
}



let square = (num) =>{
    return num**2
}
// return 문 한줄이면 {}& return 생략가능
square = (num) => num**2
// () 에 들어오는 인자가 한개면 () 도 생략 가능. 0개일때는 생략 불가능
square=num =>num**2

square=() =>'No args'
// object return 할 때는 중괄호가 함수 중괄호로 인식하기 때문에 중괄호까지는 써 주기
let returnObject=() => { {key:'value'}}


//함수 기본인자 설정
const sayHello=(name='noName') => `hi ${name}`

sayHello('john')
sayHello()

//익명함수
function (num) {return num**3}
(num) => {return num ** 0.5 }//제곱근

//익명함수 즉시 호출

(function (num) {return num**3})(3)