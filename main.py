class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, n_name):
        self.name = n_name
        print("Name:", self.name)
    def change_age(self, n_age):
        self.age = n_age
        print("Age:", self.age)
    def add_track(self, tracks):
        self.tracks.append(tracks)
        print("Tracks:", self.tracks)
    def get_score(self):
        print("Score:", self.score)

Bob = Student(name="Bob", age=26, tracks=["FE, BE"],score = 20.90)
    
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()



