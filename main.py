from pyscript import display, document

def get_name(e):
    document.getElementById('div1').innerHTML = ''

    first_name= ["pocholo", "arkin", "lara", "liam" "comanda", "san agustin", "estrada", "lao"]
    last_name= ["comanda", "san agustin", "estrada", "lao"]

    name_first = document.getElementById('fname').value.lower().strip()
    first_name_checker = name_first in first_name

    name_last = document.getElementById('lname').value.lower().strip()
    last_name_checker = name_last in last_name

    

    display_message = ('Sorry you are not registered to this club', f' Welcome {name_first}  {name_last} to the ICT club')

    display(display_message[first_name_checker], target='div1')

    # FUNCTION
def finding_nickname(e):
    # Variables
    document.getElementById('result').innerHTML = " "
    type = document.getElementById('country')
    #This will get the value assigned to the country on the dropdown menu
    nickname = type.value
    #This will display the nickname
    display(nickname,  target='result')

def non_metal_value(e):
    document.getElementById('result').innerHTML = " "
    non_metal_v = document.getElementById('dictionary').value   

    non_metal = {
        'H':'Symbol: H Element: Hydrogen Atomic Number: 1 Atomic Mass: 1.008',
        'C':'Symbol: C  Element: Carbon Atomic Number: 6 Atomic Mass: 12.011',
        'N':'Symbol: N Element: Nitrogen Atomic Number: 7  Atomic Mass: 14.007',
        'F':'Symbol: F Element: Flourine  Atomic Number: 9 Atomic Mass: 18.998403162',
        'Ne':'Symbol: Ne Element: Neon  Atomic Number: 10 Atomic Mass: 20.1797',
        'I':'Symbol: I Element: Iodine  Atomic Number: 53 Atomic Mass: 126.90447',
        'Ar':'Symbol: Ar Element: Argon  Atomic Number: 18 Atomic Mass: 39.948 '
        
        

        }
  
    

    
    display_message = non_metal.get(non_metal_v, 'Sorry, please type a valid element')

    display(display_message, target='result')




    



