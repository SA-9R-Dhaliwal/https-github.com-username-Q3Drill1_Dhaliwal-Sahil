# Seatworkk 2 - Second Quarter
from pyscript import display, document


def intrams_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value

    if registration != 'registered':
        display(f'Not eligible: student is not registered for Intrams. Ask your PE teacher regarding the online registraton.', target='output')
    elif clearance != 'cleared':
        display(f'Not eligible: medical clearance required. Go to the clinic and secure your clearance.', target='output')
    elif section == 'emerald':
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "Place the image tag here"
    elif section == 'ruby':
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "Place the image tag here"
    elif section == 'sapphire':
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "Place the image tag here"
    else: 
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "Place the image tag here"