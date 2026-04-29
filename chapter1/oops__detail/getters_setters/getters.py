'''
getters = get the values of the attribute

setters = set the values of the attribute

they protect the attribute by providing an indirect way to access them and modify them 

We can make the attributes non-public and still provide a way to work with them indirectly.
'''

'''
getters naming convenction:
get_+attribute

calling a getter
<object>.get_<attribute>()

For eg
get_name , get_address , get_color , get_age , get_id 
'''
class Movie:

    def __init__(self,title, rating):
        self._title = title 
        self.rating = rating  
    
    def get_title(self):
        return self._title


my_movie = Movie("Interstellar",10)

print(my_movie.get_title())






