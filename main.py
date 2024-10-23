class India:
    def capital(self):
        print('New Delhi is the capital of India')
    def type(self):
        print('India is a developing country')

class USA:
    def capital(self):
        print('Washington DC is the capital of USA')
    def type(self):
        print('USA is a developed country')

I1=India()
U1=USA()
for c in (I1,U1):
    c.capital()
    c.type()