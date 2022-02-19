from queue import Empty


class Parking_garage():
   
    def __init__ (self,tickets,spaces,currentTicket):
       self.tickets = tickets
       self.spaces = spaces
       self.currentTicket = currentTicket

    def takeTicket(self):
        if self.tickets == []:
            print(" No more Tickets are available.Garage is full")
        else:
            allocate_ticket = self.tickets.pop()
            allocate_space = self.spaces.pop()
            print(F"Your ticket number is {allocate_ticket} and parking lot is {allocate_space}")
            self.currentTicket[allocate_ticket] = "not paid"
        
    def paymentTickets(self):
       user_pay = int (input("Enter your ticket number: "))
       
       if user_pay not in self.currentTicket:
           print("Ticket number is invalid. Please Buy Ticket first")
       else:
           self.payment = input("Enter your payment: ")
          
           if  self.payment:  
                print ("Your Payment is confirmed. You have 15 mins to leave.")
                self.currentTicket[user_pay] = "paid"
           else:
                print("Please do your Payment")    
       
    def returnTickets(self):
        user_return = int(input("Enter your ticket number "))
        if user_return not in self.currentTicket:
            print("Ticket number is invalid. ")
        elif self.currentTicket[user_return] == "paid":
            print("Thank you!! have a nice day")
            self.tickets.append(user_return)  
            self.spaces.append(user_return) 
        else:   
            print("Please go back and do your payment first")
    

parking = Parking_garage([1,2,3,4 ],[1,2,3,4],{})

def run():

    while True:
        response = input("Welcome!! to the Parking Garage. Do you want to buy/pay/leave/quit?  ")
    
        if response.lower() == 'buy':
            parking.takeTicket()
            print("Thanks for coming")
        elif response.lower() == 'pay':
            parking.paymentTickets()
        elif response.lower() == 'leave':
            parking.returnTickets() 
        elif response.lower() == 'quit':
            break  
        else:
            print("Invalid Input") 

run()           
