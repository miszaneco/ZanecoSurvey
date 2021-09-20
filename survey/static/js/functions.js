const Worst = document.getElementById('Worst')
const Poor = document.getElementById('Poor')
const Fair = document.getElementById('Fair')
const Good = document.getElementById('Good')
const Excellent = document.getElementById('Excellent')

const array = [Worst, Poor, Fair, Good, Excellent]

const setStars = (selection) => {
    switch(selection)
    {
        case 'Worst':{
            Worst.classList.add('checked')
            Poor.classList.remove('checked')
            Fair.classList.remove('checked')
            Good.classList.remove('checked')
            Excellent.classList.remove('checked')
        }
        
        case 'Poor':{
            Worst.classList.add('checked')
            Poor.classList.add('checked')
            Fair.classList.remove('checked')
            Good.classList.remove('checked')
            Excellent.classList.remove('checked')
        }
        
        case 'Fair':{
            Worst.classList.add('checked')
            Poor.classList.add('checked')
            Fair.classList.add('checked')
            Good.classList.remove('checked')
            Excellent.classList.remove('checked')
        }

        case 'Good':{
            Worst.classList.add('checked')
            Poor.classList.add('checked')
            Fair.classList.add('checked')
            Good.classList.add('checked')
            Excellent.classList.remove('checked')
        }

        // case 'Excellent':{
        //     Worst.classList.add('checked')
        //     Poor.classList.add('checked')
        //     Fair.classList.add('checked')
        //     Good.classList.add('checked')
        //     Excellent.classList.add('checked')
        // }
    }
}

array.forEach(item=>item.addEventListener('mousedown', (event)=>{
    setStars(event.target.id)
}))


function get_rate(iRate)
  {
    // var iRate = document.getElementById("rate").value;
    
    alert(iRate);
    
    switch(iRate)
    {
      case 1:
        rate = 'Worst';
        break;
      
      case 2:
        rate = 'Poor';
        break;
      
      case 3:
        rate = 'Fair';
        break;

      case 4:
        rate = 'Good';
        break;

      case 5:
        rate = 'Excellent';
        break;

      default:
    }
  }