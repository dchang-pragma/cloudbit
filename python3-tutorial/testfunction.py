def ask_ok(prompt='provide input', retries=4, reminder='Please try again!'):
    while retries>0:
        ok = input(prompt)
        
        if ok in ('y', 'ye', 'yes'):
        		retries = retries - 1
        		print(retries)
        		continue
            
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        #retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        
        print(reminder)
    print('Ok you quit')
ask_ok('Do you really want to quit?',2)