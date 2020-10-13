// forEach
// const colors = ['red', 'blue', 'green']

//인자로 주어진 함수를 배열의 요소 하나하나마다 실행
// colors.forEach(function (color) {
//     console.log(color)
// })
// colors.forEach(color => console.log(color))

// refactoring

// 리턴이 있는가?
// const result = colors.forEach(color => console.log(color))
// console.log(result) // undefined

// 실습 문제, images 배열안에 있는 정보를 통해 넓이를 구해서 areas에 저장하세요
// const images = [
//   { height: 10, width: 30 },
//   { height: 20, width: 90 },
//   { height: 54, width: 32 }
// ]

// const areas = []
// images.forEach(img => areas.push(img.height * img.width)) 
// console.log('areas',areas)

// map
// 인자로 주어진 함수의 결과(return)를 배열로 만들어서 return 해준다.
// const numbers = [1, 2, 3]

// const doubleNumbers = numbers.map(function (number) {
//   return number * 2
// })
// const doubleNumbers = numbers.map(number => number*2)
// console.log(doubleNumbers) // [ 2, 4, 6 ]



// refactoring

// 실습 - 각 요소를 제곱한 결과를 담는 배열 squared를 map을 통해 만드세요
// const newNumbers = [4, 9, 16]

// const squared = newNumbers.map(num => num**2)

// console.log(squared)

// filter
// 참 or 거짓으로 리턴을 받아 참인 요소들만 담아준다.
// const products = [
//   { name: 'cucumber', type: 'vegetable' },
//   { name: 'banana', type: 'fruit' },
//   { name: 'carrot', type: 'vegetable' },
//   { name: 'apple', type: 'fruit' },
// ]

// const fruits = products.filter(function (product) {
//   return product.type === 'fruit'
// })

// console.log('fruits',fruits)

// refactoring
// const fruits = products.filter(product => product.type === 'fruit')
// console.log('fruits',fruits)

// 실습 - numbers 중 50보다 큰 값만 모은 배열 filteredNumbers를 만드세요
// const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]
// const filteredNumbers = numbers.filter(num => num>50)
// console.log('filteredNumbers',filteredNumbers)

// reduce
// const tests = [1, 2, 3, 4]

// const sum = tests.reduce(function (total, x) {
//   return total + x
// }, 10)  // 여기서 0 생략 가능
// 지정되어있는 초기값(initialvalue)값을 넣는다.
// 입력된 배열의 첫 요소를 불러와 연산을 한다.
// 쭉 반복해서 끝까지 도달하면 이제 sum에 값이 저장
// 만약 초기값이 없다면 그냥 배열의 첫 요소를 불러와서 바로 시작

// console.log(sum)

// refactoring
// const sum = tests.reduce((total,x) => total+x,0)
// console.log(sum)

// 평균
// const sum = tests.reduce((total, x) => total + x, 0) / tests.length

// 실습 tests의 요소들 중 짝수들만 더한 값을 reduce로 만들어 주세요
// const tests = [1, 2, 3, 4, 6, 9, 10]
// const sum = tests.reduce(function (total, x) {
//     return x%2?total:total+x
//   }, 0)
// console.log(sum)

// const sum = tests.filter(x => x%2===0).reduce((total,x) => total+x,0)
// console.log(sum)

// 실습 - 주어진 baseUrl 문자열 뒤에 필수 요청 변수인 api 의 key — value 값을 key=value 의 형태로 더하여 요청 url을 만드세요. URL에서 요청 변수는 & 문자로 구분합니다.
// object의 key를 배열로 만들어 주는 기능이 js에 있습니다. 찾아보세요!
// const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'

// const api = {
//   'key': 'API_KEY',
//   'targetDt': '20200115'
// }

// const url = `${baseUrl}key=${api.key}&targetDt=${api.targetDt}`
// const url = Object.keys(api).reduce(function (total,x) {
//     return total+x+'='+api[x]+'&'
// }, baseUrl)

// const url = Object.keys(api).reduce((prev,next) => `${prev}&${next}=${api[next]}`,baseUrl)

// console.log(url)


// find
// 조건에 맞는 값을 찾아서 반환
// filter와는 다르게 여러개가 있어도 맨처음 조건을 충족하는 하나만 나온다.
// 조건을 충족 시키는것이 없다면 undefine 출력
// const avengers = [
//   { name: 'Tony Stark', age: 45 },
//   { name: 'Steve Rogers', age: 32 },
//   { name: 'Thor', age: 40 },
// ]

// const avenger = avengers.find(function (avenger) {
//   return avenger.name === 'Tony Stark'
// })

// console.log(avenger)

// refactoring
// const avenger = avengers.find(avenger => avenger.name === 'Tony Stark')

// some
// 조건을 충족하는 요소가 하나라도 있으면 True
// 전부다 조건을 위배하면 False
// const arr = [1, 2, 3, 4, 5]

// const result = arr.some(elem => elem % 2 === 0)  // true
// console.log(result)

// every
// 조건을 전부다 충족하면 True
// 하나라도 조건을 위배하면 False
// const arr = [1, 2, 3, 4, 5]

// const result2 = arr.every(elem => elem % 2 === 0)  // false