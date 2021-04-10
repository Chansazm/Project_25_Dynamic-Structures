import enum

class Gas_choices(enum.Enum):
   Regular = 1
   Unleaded = 2
   Super_Unleaded = 3
   
class Gasoline:
    def gas_cost(self,litres,gasoline_Kinds,Carwash):
        gasoline_Kinds = {"Regular 1": "K16.25", "Unleaded 2": "K17.23" ,"Super_Unleaded 3": "K19.50"}
        
        for kind in gasoline_Kinds:
            if gasoline_Kinds[kind] == Gas_choices.Regular:
                return gasoline_Kinds[kind] * litres
            elif gasoline_Kinds[kind] == Gas_choices.Unleaded:
                return gasoline_Kinds[kind] * Gas_choices.Super_Unleaded
            else:
                return gasoline_Kinds[kind] * Gas_choices.Unleaded
        return  
        
class Car_Wash:
    def Car_Wash_Cost(self,gasoline_purchased,carwash = False):
        Car_wash_Fees = 0
        if gasoline_purchased >= 200.00:
            Car_wash_Fees = 40.00
        else:
            Car_wash_Fees = 70.00
        return Car_wash_Fees

class Customer:
    def Customer_Statement(self,CustomerID, Date, Time, Costs,Car_Washed = False):
        Costs = 0
        if Car_Washed == True:
            return Car_Wash
        print(CustomerID,Date,Time, Car_Wash.car_wash_Fees)




    
        
        