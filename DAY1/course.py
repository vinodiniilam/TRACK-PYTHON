
class Course:
    def __init__(self,name,duration,trainer,technologies,start_date,end_date):
        self.name=name
        self.duration=duration
        self.trainer=trainer
        self.technologies=technologies
        self.start_date=start_date
        self.end_date=end_date
    def display(self):
        print("Name:", self.name)
        print("Duration:", self.duration)
        print("Trainer:", self.trainer)
        print("Technologies:", self.technologies)
        print("Start Date:", self.start_date)
        print("End Date:", self.end_date)
    def is_covered(self,tech):
        if tech in self.technologies:   
            print(tech+" is covered in the course")
        else:
            print(tech+" is not covered in the course")
    def no_of_tech(self):
        print("number of technologies is :", len(self.technologies))        
c=Course("python full stack",3,"salman sir",["python","sql","html","css"],"15th june","15 december")
c.display() 
c.is_covered("python")
c.is_covered("JAVA")
c.no_of_tech()
