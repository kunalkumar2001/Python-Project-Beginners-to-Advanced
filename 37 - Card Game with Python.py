class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    
    values = [None, None, "2","3","4","5","6","7",
              "8","9","10","Jack","QUeen", "King","Ace"]
    
    def __init__(self,v,s):
        self.value = v
        self.suit = s
        
    def __lt__(self,other):
        if self.value != other.value:
            return self.value < other.value
        return self.suit < other.suit
    
    def __gt__(self, other):
        if self.value != other.value:
            return self.value > other.value
        return self.suit > other.suit
    
    def __repr__(self):
        return f"{self.values[self.value]} of {self.suits[self.suit]}"   
    
    
if __name__ == "__main__":
    c1 = Card(14, 0)
    c2 = Card(13, 2)   

    print(c1)
    print(c2)
    print("c1 > c2 :", c1 > c2)
       