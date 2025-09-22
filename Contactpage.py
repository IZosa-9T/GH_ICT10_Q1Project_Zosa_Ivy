from pyscript import display

location = ['O3 Eisenhower St., Greenhills, San Juan City, Metro Manila, Philippines.', '10 Topaz, 5th floor, room 501' ] # list
numbers = ['(000)-000-000', '(02) 8722 9720'] # list
emails = ['zosa.ia@obmontessori.edu.ph', 'gh10topaz26@obmontessori.edu.ph']
business_hours = '9 : 00 am - 6 : 00 pm' # script

display(f'{location[0]}', target='contactlocation')
display(f'{location[1]}', target='contactlocation')
display(f'{numbers[0]}', target='phonenumbers')
display(f'{numbers[1]}', target='phonenumbers')
display(f'{emails[0]}', target='email')
display(f'{emails[1]}', target='email')

display(f'{business_hours}', target='businesshours')
