class dummy:
    def __enter__(self):
        print('Entering')
        return 'Entering Return'
    def __exit__(self ,type, value, traceback):
        print('exiting',type,value,traceback)
        return False

with dummy() as s:
    print(s)


