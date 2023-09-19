#challenge 2.2

#define the base class player 
class Player:
 def play(self):
  print("The player is playing     cricket.")
#define the derived class batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")
#define derived class Bowler 
class Bowler(Player):
  def play(self) :
    print("The bowler is bowling.") 
#Creating object of batsman and bowler classes 
batsman=Batsman() 
bowler=Bowler()  
#call the play() method for each object
batsman.play() 
bowler.play()