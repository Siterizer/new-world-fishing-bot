class LastResults:
    def __init__(self):
      self.data = []
      self.data+='1'
    def add(self,val):
        if len(self.data)==20:
            self.data=self.data[1:]+[val]
        else:
            self.data+=[val]

    def is_full_of(self, val):
        return self.data.count(val) == len(self.data)

    def get_last_value(self):
        return self.data[-1]

    def get_one_before_last_value(self):
        return self.data[-2]

    def are_too_much_pauses(self):
        return self.data[-7:].count('3') + self.data[-7:].count('4') == len(self.data)
