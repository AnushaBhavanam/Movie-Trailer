import AnuMovies
import fresh_tomatoes
Awe=AnuMovies.AnuMovieTrailers("Awe!","Indian Telugu-language psychological thriller film ",
                                "https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj4lLWe1d7gAhUPS48KHY93D4MQjRx6BAgBEAU&url=https%3A%2F%2Fwww.mirchi9.com%2Fgallery%2Fawe-movie-posters%2F&psig=AOvVaw2TBQ3X4mEirxfaWFi6kIrm&ust=1551451148251406",
                                "https://www.youtube.com/watch?v=xOEscQChX7M")
UTurn=AnuMovies.AnuMovieTrailers("U-Turn","A Mystery Thriller ","https://www.thenewsminute.com/sites/default/files/styles/news_detail/public/samantha-uturn.jpg?itok=AE2rb1hZ",
                                   "https://www.youtube.com/watch?v=HG7Lv384yTU")
Robo=AnuMovies.AnuMovieTrailers("Robo2.O","Indian Tamil-language science fiction action film",
                                   "https://pbs.twimg.com/media/Dm4dMDjUUAAx0U4.jpg","https://www.youtube.com/watch?v=2wvq8hdGdAw")
MeesayaMurukku=AnuMovies.AnuMovieTrailers("MeesayaMurukku","Indian Tamil language romantic comedy film",
                                          "https://cdn4.gsc.com.my/WebLITE/Applications/MovieManagement/uploaded/pics/2017/Meesaya_Murukku/Meesaya_Murukku_Keyart_500.jpg",
                                          "https://www.youtube.com/watch?v=lZaG3tNbJaU")
TwoFour=AnuMovies.AnuMovieTrailers("24"," Indian Tamil-language science fiction thriller","https://4.bp.blogspot.com/-AstlqP09O28/VtvRPgim-1I/AAAAAAAAS3s/Uyhdmgl1a9o/s1600/24%2BTelugu%2BMovie%2BFirst%2BLook%2BPosters1.jpg",
                              "https://www.youtube.com/watch?v=c6sadq8BhMc")
Dangal=AnuMovies.AnuMovieTrailers("Dangal","Indian Hindi-language biographical sports drama film","https://i.ytimg.com/vi/-HB7CyVVL0E/maxresdefault.jpg",
                                  "https://www.youtube.com/watch?v=Muxd-6_guUU")
Avatar=AnuMovies.AnuMovieTrailers("Avatar2"," Upcoming American epic science fiction film",
                                  "https://i.ytimg.com/vi/GonL7BKVbp4/maxresdefault.jpg","https://www.youtube.com/watch?v=pt4Okk_2I04")
Insidious=AnuMovies.AnuMovieTrailers("Insidious: The Last Key","American super natural horror film ",
                                     "https://horrorhorns.files.wordpress.com/2018/01/tjwayeunddw.jpg?w=604",
                                     "https://www.youtube.com/watch?v=acQyrwQyCOk")
Premam=AnuMovies.AnuMovieTrailers("Premam"," Indian Malayalam-language romantic comedy film","https://www.filmibeat.com/ph-big/2016/09/premam_147446094340.jpg",
        "https://www.youtube.com/watch?v=eEH2ba3VGjc")
movies=[Awe,UTurn,Robo,MeesayaMurukku,TwoFour,Dangal,Avatar,Insidious,Premam] 
fresh_tomatoes.open_movies_page(movies)

