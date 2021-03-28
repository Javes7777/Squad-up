console.log('hello world')

const TimerBox = document.getElementById('Timer-box')
console.log(TimerBox.textContent)
const countDownBox = document.getElementById('countdown-box')

console.log(TimerBox.textContent)
const TimerDate = Date.parse(TimerBox.textContent)
console.log(TimerDate)

setInterval(()=>{
    const now = new Date().getTime()
    console.log(now)

    const diff = TimerDate - now
    console.log(diff)

    const d = Math.floor(TimerDate/(1000*60*60*24) - (now/(1000*60*60*24)))
    const h = Math.floor(TimerDate/(1000*60*24) - (now/(1000*60*24)))
    console.log(h)
    //console.log(countDownBox.textContent)
}, 1000)