# CLASSES AND OBJECT-ORIENTED PROGRAMMING

# Let's create a custom Player class. A Player has:
    # DONE 2 instance attributes: NAME and LIFE
    # DONE 1 class attribute: STRENGTH = 3
    # DONE 2 class methods (aka functions): HIT and HEAL.
        # Players can gain health by using the heal function.
        # Players can hit other players by using the hit function.

class Player:
    dead = False
    def __init__(self, name, life):
        self.name = name
        self.life = life
        print("Welcome {0} to the game! {0} has {1} life.".format(self.name, self.life))

    strength = 2

    def heal(self, x):
        if not self.dead:
            self.life += x
            print("{0} healed {1} damage!".format(self.name, x))
        else:
            print("{0} is dead!".format(self.name))

    # When OTHER_PLAYER is HIT, they lose health equal to SELF.STRENGTH
    def hit(self, other_player):
        if not self.dead and not other_player.dead:
            other_player.life -= self.strength
            print("{0} hit {1}! {1} lost {2} health.".format(self.name, other_player.name, self.strength))
            if other_player.life <= 0:
                print("{0} died!".format(other_player.name))
                other_player.dead = True
        elif self.dead:
            print("{0} is dead!".format(self.name))
        else:
            print("{0} is dead!".format(other_player.name))



## Inheritance
# Let's create a class Archer that *inherits from the Player class. In other words, we're saying that an Archer IS a Player, just with extra functionality.

# Let's say that an Archer has less strength than a normal player, but that s(he) can SHOOT other players for 3 damage.
class Archer(Player):  # Contrast this with the way we declared the Player class above.

    strength = 1

    def shoot(self, other_player):
        if not self.dead and not other_player.dead:
            other_player.life -= 3
            print("{0} shot {1}! {1} lost 3 health.".format(self.name, other_player.name))
            if other_player.life <= 0:
                    other_player.dead = True
                    print("{0} died!".format(other_player.name))
        elif self.dead:
            print("{0} is dead!".format(self.name))
        else:
            print("{0} is dead!".format(other_player.name))
