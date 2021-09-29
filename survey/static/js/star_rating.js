// console.log('Set Stars')
document.getElementById('rate_type').style.visibility = 'hidden'

const Worst = document.getElementById('Worst')
const Poor = document.getElementById('Poor')
const Fair = document.getElementById('Fair')
const Good = document.getElementById('Good')
const Excellent = document.getElementById('Excellent')

const array = [Worst, Poor, Fair, Good, Excellent]

array.forEach(item=>item.addEventListener('click', (event)=>{
  // console.log(event.target.id)
  setStars(event.target.id)
}))

const setStars = (selection) => {
  document.getElementById('rate_type').value = selection
  console.log(selection)
    
  Poor.classList.remove("checked")
  Fair.classList.remove("checked")
  Good.classList.remove("checked")
  Excellent.classList.remove("checked")

  switch (selection)
  {
    case 'Worst': {
      Worst.classList.add("checked")
      document.getElementById('rate').value = 1
      return
    }
    
    case 'Poor': {
      document.getElementById('rate').value = 2
      Worst.classList.add('checked')
      Poor.classList.add('checked')
      return
    }
    
    case 'Fair': {
      document.getElementById('rate').value = 3
      Worst.classList.add('checked')
      Poor.classList.add('checked')
      Fair.classList.add('checked')
      return
    }

    case 'Good':{
      document.getElementById('rate').value = 4
      Worst.classList.add('checked')
      Poor.classList.add('checked')
      Fair.classList.add('checked')
      Good.classList.add('checked')
      return
    }

    case 'Excellent':{
      document.getElementById('rate').value = 5
      Worst.classList.add('checked')
      Poor.classList.add('checked')
      Fair.classList.add('checked')
      Good.classList.add('checked')
      Excellent.classList.add('checked')
      return
    }
  }
}