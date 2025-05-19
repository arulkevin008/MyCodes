class school():
    def __init__(self):
        self.school=""
        self.section=""
        self.group=""
    def display(self):
        print("School:",self.school)
        print("Section:",self.section)
        print("Group:",self.group)

education = school()

education.school="Petit Seminaire"
education.section="12-B2"
education.group="Computer Science"

education.display()
        
        
