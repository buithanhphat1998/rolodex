class Contact:
    f_name: str
    l_name: str
    phone: str
    address: str
    city: str
    zip: str

    def __init__(self,fn,ln,ph,addr,city,zip):
        self.f_name = fn
        self.l_name = ln
        self.phone = ph
        self.address = addr
        self.city = city
        self.zip = zip
    def __lt__(self, other):
        if(self.l_name == other.l_name):
            if(self.f_name < other.f_name):
                return True
            else: 
                return False
        else:
            return True if self.l_name < other.l_name else False
    def __str__(self):
        info = f"""{self.l_name}
{self.f_name}
{self.phone}
{self.address}
{self.city}
{self.zip}
"""
        return info
    def __repr__(self):
        return f'{self.f_name},{self.l_name},{self.phone},{self.address},{self.city},{self.zip}\n'
