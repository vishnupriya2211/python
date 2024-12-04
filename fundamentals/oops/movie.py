class Movie:
    id:int
    title:str
    rating:int
    director:str
    run_time:int
    genre:str

    def __init__(self,id,title,rating,director,run_time,genre):
     self.title=title
     self.id=id
     self.rating=rating
     self.director=director
     self.run_time=run_time
     self.genre=genre
     
    def display_Movie(self):

        print(self.id,self.title,self.rating,self.run_time,self.director)



faculity_instace2=Movie(100,"Kalki",5,"Nag Ashwin",100,50000)


faculity_instace2.display_Movie()