
#& Create a class loginin, add followers, class instagram which inherits from class login and add followers
class Login:
    def login(self):
        while True:
            user=input("Enter your username: ")
            if user==self.USERNAME:
                pasw=input("Enter your password: ")
                if pasw==self.PASSWORD:
                    print("Logged in successfully")
                    break
                else:
                    print("Wrong password")
            else:
                print("Wrong username")


class Followers:
    def add_followers(self):
        self.FOLLOWERS+=1
        print("Followers added",self.FOLLOWERS)

    def remove_followers(self):
        self.FOLLOWERS-=1
        print("Followers removed")

class Instagram(Login,Followers):
    founded_year=2010
    CEO="MR ABC"
    def __init__(self,username,password,followers,following,noofpost):
        self.USERNAME=username
        self.PASSWORD=password
        self.FOLLOWERS=followers
        self.FOLLOWING=following
        self.NOOFPOST=noofpost
    def display(self):
        print("Username: ",self.USERNAME)
        print("Password: ",self.PASSWORD)
        print("Followers: ",self.FOLLOWERS)
        print("Following: ",self.FOLLOWING)
        print("No of posts: ",self.NOOFPOST)

obj1=Instagram("Rahul","Rahul@123",10,10,0)
obj2=Instagram("Preksha","Preksha@123",10,10,0)
obj1.login()
obj1.add_followers()
obj1.display()