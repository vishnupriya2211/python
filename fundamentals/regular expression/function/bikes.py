def bikes(**kwargs):

    print(kwargs.get("bike"))
    print(kwargs.get("price"))
    print(kwargs.get("cc"))
          

bikes(bike="hunter 350",price="200000",cc="350")
bikes(bike="GT 650",price="400000",cc="650")
