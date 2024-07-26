# iterator like range()

class myIter:
    def __init__(self, *arg):
        if len(arg) == 0:
            raise TypeError('my iter takes atleast one argument')
        elif len(arg) > 3:
            raise TypeError('my iter never takes more than 3 arguments')
        elif arg[0] >= arg[1]:
            raise TypeError('Start should be less than stop')
        elif type(arg[0]) != int or type(arg[1]) != int or type(arg[2]) != int:
            raise ValueError('All arguments should be int type')
        
        if len(arg) == 1:
            self.start = 1
            self.stop = arg[0]
            self.incri = 1
        elif len(arg) == 2:
            self.start = arg[0]
            self.stop = arg[1]
            self.incri = 1
        elif len(arg) == 3:
            self.start = arg[0]
            self.stop = arg[1]
            self.incri = arg[2]

    def __iter__(self):
        return self

    def __next__(self):
        x = self.start
        self.start += self.incri
        if x <= self.stop:
            return x
        else:
            print(f'Limit reached - {self.stop}')
            raise StopIteration
        

for i in myIter(1,20,1):
    print(i)

