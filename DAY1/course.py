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
name=input("enter the course name:")
duration=int(input("enter the duration:"))
trainer=input("enter the trainer name:")
technologies=input("enter the technologies:")
start_date=input("enter the start date:")
end_date=input("enter the end date:")
c=Course(name,duration,trainer,technologies,start_date,end_date)
c.display()     