class dog:
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

gr = dog("Golden Retriever", "Light Brown")
husky = dog("Husky", "Grey")

print("Breed of Dog: ", gr.breed)
print("Colour of Breed: ", gr.colour)
print("Breed of Dog: ", husky.breed)
print("Colour of Dog: ", husky.colour)