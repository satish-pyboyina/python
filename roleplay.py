class Character:
    def __init__(self,name,hp,level):
        self.name = name
        self.hp = hp
        self.level = level

    # @property
    # def hp(self):
    #     return self.hp

class NPC(Character):
    def __init__(self,name,hp,level):
        super().__init__(name,hp,level)
        # Character.__init__(self,name,hp,level)
        # Character.__init__(self,name=name,hp=hp,level=level)
    
    @classmethod
    def speak(cls):
        print("I heard there were monsters running around last night!")
        return cls

# villager = Character("bob",100,12)
villager = NPC("bob",100,12)
print(villager.name)
print(villager.hp)
print(villager.level)
villager.speak()