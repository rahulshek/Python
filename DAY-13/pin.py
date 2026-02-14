pin1=int(input("Enter pin: "))
pin=str(pin1)


for i in range(len(pin)-2):
    if len(pin)==4:
        if (pin[i]==pin[i+1]==pin[i+2]) or (pin[i+1]==pin[i+2]== pin[i+3]):
            print("Repeating Numbers in the PIN")
            break
        elif (int(pin[i])+1==int(pin[i+1])==int(pin[i+2])-1) or (int(pin[i+1])+1==int(pin[i+2])==int(pin[i+3])-1):
            
            print("Sequence of numbers in the pin")
            break
        else:
            print('Valid Pin')
            break
    else:
      
      print("Invalid length")
      break
