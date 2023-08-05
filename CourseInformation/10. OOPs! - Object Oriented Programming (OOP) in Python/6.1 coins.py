import random

class Coin:
    def __init__(self, rare =False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "£{} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))
    

class One_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.01,
                "clean_colour":"bronze",
                "rusty_colour":"brownish",
                "num_edges" : 1,
                "diameter": 20.3,
                "thickness": 1.52,
                "mass":3.56,
            }
        super().__init__(**data)

class Two_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.02,
                "clean_colour":"bronze",
                "rusty_colour":"brownish",
                "num_edges" : 1,
                "diameter": 25.9,
                "thickness": 1.85,
                "mass":7.12,
            }

        super().__init__(**data)

class Five_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.05,
                "clean_colour":"silver",
                "rusty_colour": None,
                "num_edges" : 1,
                "diameter": 18.0,
                "thickness": 1.77,
                "mass":3.25,
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Ten_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.10,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 1,
                "diameter": 24.5,
                "thickness": 1.85,
                "mass":6.50,
            }

        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour
        
class Twenty_Pence(Coin):
    def __init__(self):
        
        data = {"original_value":0.20,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 7,
                "diameter": 21.4,
                "thickness": 1.7,
                "mass":5.00,
            }

        super().__init__(**data)
    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Fifty_Pence(Coin):
    def __init__(self):
        
        data = {"original_value":0.50,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 7,
                "diameter": 27.3,
                "thickness": 1.78,
                "mass":8.00,
            }

        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour   


class One_Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour" : "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness":3.15,
            "mass": 9.5
            }
        super().__init__(**data)

class Two_Pound(Coin):
    def __init__(self):
        data = {"original_value":2.00,
                "clean_colour":"gold & silver",
                "rusty_colour":"greenish",
                "num_edges" : 1,
                "diameter": 28.4,
                "thickness": 2.50,
                "mass":12.00,
            }

        super().__init__(**data)
    
    
coins = [One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(), Twenty_Pence(),
             Fifty_Pence(), One_Pound(), Two_Pound()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                           coin.num_edges, coin.mass]

    string = "{} - Colour: {}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)

    
{"threads":[{"position":0,"start":0,"end":2490,"connection":"open"},{"position":2491,"start":2491,"end":4980,"connection":"idle"}],"url":"https://att-b.udemycdn.com/2018-07-09_00-02-48-45f49d10d62ae6f187d48e791f2cbe3e/original.py?secure=qK-gjmB91t57NYhpSGYnlA%3D%3D%2C1617441097&filename=coins.py","method":"GET","port":443,"downloadSize":4980,"headers":{"date":"Sat, 03 Apr 2021 04:45:15 GMT","content-type":"text/plain","content-length":"4980","connection":"close","x-amz-id-2":"+Xr+xpluS0DI0wgHwdSNubQkScclwnt1IY4HLSHcQwTlbTaTZ48beSHizMYt4wMHXG68SWTnmW4=","x-amz-request-id":"F432E3E31863D542","x-amz-replication-status":"COMPLETED","last-modified":"Mon, 09 Jul 2018 00:02:49 GMT","etag":"\"0a213ae0827bf366118bfd42adb0170f\"","x-amz-meta-qqfilename":"coins.py","x-amz-version-id":"lkVIl_a8jHXPrUxOhSXiUmgPgVYdOX1R","x-edge-ip":"185.152.65.83","x-edge-location":"pragueCZ","server":"CDN77-Turbo","cache-control":"max-age=31536000","content-disposition":"attachment; filename=\"coins.py\"","x-77-nzt":"Abk73AGyNKT/WffoAA==","x-77-nzt-ray":"BPQIZFGWrLs=","x-cache-lb":"HIT","x-age-lb":"15267673","x-77-pop":"frankfurtDE","x-77-cache":"HIT","accept-ranges":"bytes"}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  