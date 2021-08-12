def make_division_by (a) : 
    def division (b):
        return b/a
    return  division


def run() :
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

if __name__ == "__main__" :
    run()