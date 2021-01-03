class Mother:
    # def __init__(self,eye_color, hair_color, hair_type):
    #     self.eye_color = eye_color
    #     self.hair_color = hair_color
    #     self.hair_type = hair_type
    eye_color = "brown"
    hair_color = "dark brown"
    hair_type = "curley"

class Father:
    # def __init__(self,eye_color, hair_color, hair_type):
    #     self.eye_color = eye_color
    #     self.hair_color = hair_color
    #     self.hair_type = hair_type
    eye_color = "blue"
    hair_color = "blond"
    hair_type = "straight"


class Child(Mother,Father):
    # def __init__(self,eye_color, hair_color, hair_type):
    #     super().__init__(eye_color, hair_color, hair_type)
    pass

tony = Child()

print(tony.eye_color)