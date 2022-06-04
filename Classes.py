""" Parent Class
The class from which we inherit called the Parent Class, Superclass, or Base Class.
"""

#Example: 1

'''
class Data_Scientist:
   def __init__(self, name, SQL):
      self.name = name
      self.SQL = SQL
   def knows_maths_stats(self):
      return True
   def knows_programming(self):
      return True
 
class Data_Analyst:
   def __init__(self, name, SQL):
      self.name = name
      self.SQL = SQL
   def knows_maths_stats(self):
      return True
   def knows_programming(self):
      return True 
 
class Data_Engineer:
   def __init__(self, name):
      self.name = name
      self.SQL = SQL
   def knows_maths_stats(self):
      return True
   def knows_programming(self):
      return True '''
    
class Data_Professional:
 def __init__(self, name, SQL):
    self.name = name
    self.SQL = SQL
 def knows_maths_stats(self):
    return True
 def knows_programming(self):
    return True

 class Data_Scientist(Data_Professional):
 def __init__(self, name, SQL):
    super().__init__(name, SQL)


dt_sci = Data_Scientist(“Mary Smith”, 9)
